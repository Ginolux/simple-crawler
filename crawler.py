import requests
from bs4 import BeautifulSoup
import re
import sys


class Crawler():

    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.links = set()


    def getPage(self):
        '''
        Return page's content as BeautifulSoup object
        '''
        try:
            req = requests.get(self.baseUrl)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')


    def crawl(self):
        '''
        Recursive function that retrieves a list of all internal 
        and external links found on each page
        '''
        bs = self.getPage()
        if bs is not None:
            for link in bs.find_all('a', href=re.compile('^(http)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in self.links:        # avoid duplicate link
                        newLink = link.attrs['href']        # We got new link
                        if newLink != None:       # check if href is not empty
                            print(newLink)
                            self.imageSrc(bs)     # function to print link of images found on each page
                        self.links.add(newLink)     # add new link to the set of links
                        if self.baseUrl in newLink:      # check if internal link or not to perform recursion
                            self.crawl()      # recursion on internal links
                        else:       # if link is external to the domain, no recursion. 
                            continue    # Go to next link.


    def imageSrc(self, bsObj):
        '''
        Retrieve static links such as images source from each page 
        visited by crawl function
        '''
        staticLinks = set()
        for image in bsObj.find_all('img'):
            if image['src'] not in staticLinks:     # avoid duplicate link
                newImageLink = image['src']
                if newImageLink != None:   # avoid broken links
                    print(newImageLink)
                    # print(self.getAbsoluteURL(self.baseUrl, newImageLink))
                    staticLinks.add(newImageLink)



if __name__ == "__main__":
    crawler = Crawler(sys.argv[1])  # provide URL as command line argument
    crawler.crawl()     # run crawler
