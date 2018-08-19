import requests
from bs4 import BeautifulSoup
import re
import sys


class Crawler():
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.links = set()


    def getPage(self):
        try:
            req = requests.get(self.baseUrl)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')


    def crawl(self):
        bs = self.getPage()
        if bs is not None:
            for link in bs.find_all('a', href=re.compile('^(http)')):
                if 'href' in link.attrs:
                    if link.attrs['href'] not in self.links:    # avoid duplicate link
                        newLink = link.attrs['href']    # We got new link
                        if newLink != None:     # check if href is not empty
                            print(newLink)
                            # function to print link of images found on each page
                            self.imageSrc(bs)
                        # add the new link to the set of links
                        self.links.add(newLink)
                        if self.baseUrl in newLink:      # check if internal link or not to perform recursion
                            self.crawl()      # recursion on internal links
                        else:       # if not internal link (external link)
                            continue


    def imageSrc(self, bsObj):
        staticLinks = set()
        for image in bsObj.find_all('img'):
            if image['src'] not in staticLinks:     # avoid duplicate link
                newImageLink = image['src']
                if newImageLink != None:   # avoid broken links
                    print(newImageLink)
                    # print(self.getAbsoluteURL(self.baseUrl, newImageLink))
                    staticLinks.add(newImageLink)


crawler = Crawler(sys.argv[1])
crawler.crawl()
