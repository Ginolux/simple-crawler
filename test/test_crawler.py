import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from crawler import Crawler

# def test_url(url):
#     urlopen(url)

# with pytest.raises(ValueError):
#     test_url('www.google.com')

# with pytest.raises(URLError):
#     test_url('http://abc.co')

# with pytest.raises(HTTPError):
#     test_url('http://abc.co')


# def test_links():
#     getLinks('')                        # test ValueError
#     getLinks('http://abc.co')           # test URLError
#     getLinks('abc.co')                  # test ValueError
#     getLinks('acb')                     # test ValueError
#     getLinks('http://google.comma')     # test URLError
#     getLinks('https://google.com')      # test working link
#     getLinks('http://en.wikipedia.org/wiki/Monty_Pytho')  # test HTTPError


def test_crawl():
    sites = ['',
            'http://abc.co',
            'abc.co',
            'acb',
            'http://www.google.comma',
            'https://google.com',
            'http://en.wikipedia.org/wiki/Monty_Pytho',
            'www.youtube.com',
            ' http://wiprodigital.com'
            ]

    for site in sites:
        crawler = Crawler(site)
        crawler.crawl()


