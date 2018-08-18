import os
import random
import re
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest
from bs4 import BeautifulSoup

from crawler import getLinks




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
