from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(baseUrl):
    global pages
    try:
        html = urlopen(baseUrl)
    except HTTPError:
        # print(err)
        return None
    except URLError:
        # print('*** Server not found! Dead url')
        return None
    except ValueError:
        print("The URL is not valid !\n The URL should start with: http:// or https://")
        exit()

    try:
        bs = BeautifulSoup(html, 'html.parser')
        if bs is not None:
            # for link in bs.find_all('a', href=re.compile('^(https://wiprodigital.com)')):
            for link in bs.find_all('a', href=re.compile('^(http)')):    
                if 'href' in link.attrs:
                    if link.attrs['href'] not in pages:
                        #We have encountered a new page
                        newPage = link.attrs['href']
                        if newPage != None:
                            print(newPage)
                            pages.add(newPage)
                            if baseUrl in newPage:
                                getLinks(newPage)
                            else:
                                continue

    except AttributeError as err:
        print(err)
    except UnboundLocalError as err:
        print(err)

    


getLinks('https://wiprodigital.com')
# getLinks('http://www.lkhl')

# imageLocation = bs.find('a', {'id': 'logo'}).find('img')['src']