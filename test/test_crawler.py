import random
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest
from bs4 import BeautifulSoup

from crawler import getLinks

# class TestDomain():

#     def testUrl(self):
#         url = 'http://en.wikipedia.org/wiki/Monty_Python'
#         html = urlopen(url)
#         return BeautifulSoup(html, 'html.parser')


#     def contentExist(self):
#         bs = self.testUrl()
#         content = bs.find('div',{'id':'mw-content-text'})
#         if content is not None:
#             return True
#         return False

#     def getNextLink(self):
#         bs = self.testUrl()
#         links = bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
#         randomLink = random.SystemRandom().choice(links)
#         return 'https://wikipedia.org{}'.format(randomLink.attrs['href'])


#     def testPageProperties(self):
#         # while True:
#         for _ in range(1, 10):
#             self.contentExist()
#             self.getNextLink()
#         print('Done!')


# td = TestDomain()
# # print(td.contentExist())
# # print(td.getNextLink())
# print(td.testPageProperties())


# def test_url(url):
#     urlopen(url)

# with pytest.raises(ValueError):
#     test_url('www.google.com')

# with pytest.raises(URLError):
#     test_url('http://abc.co')

# with pytest.raises(HTTPError):
#     test_url('http://abc.co')


def test_links():
    getLinks('')                        # test ValueError
    getLinks('http://abc.co')           # test URLError
    getLinks('abc.co')                  # test ValueError
    getLinks('acb')                     # test ValueError
    getLinks('http://google.comma')     # test URLError
    getLinks('https://google.com')      # test working link
    getLinks('http://en.wikipedia.org/wiki/Monty_Pytho')  # test HTTPError


def test_contentExist():
    url = 'http://google.com'
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    except ValueError:
        return None
    # try:
    bs = BeautifulSoup(html, 'html.parser')
    if bs is not None:
        for link in bs.find_all('a', href=re.compile('^(http)')):
            if 'href' in link.attrs:
                print(link.attrs['href'])
    else:
        print("bs is None")
        # if link.attrs['href'] not in pages:
    # except AttributeError as err:
    #     print(err)
    # except UnboundLocalError as err:
    #     print(err)


# test_contentExist()
