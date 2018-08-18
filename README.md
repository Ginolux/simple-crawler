[![wercker status](https://app.wercker.com/status/657de0605ebc00c5a973eed3e24c269c/s/master "wercker status")](https://app.wercker.com/project/byKey/657de0605ebc00c5a973eed3e24c269c)
# simple-crawler

## Overview

Simple-crawler is a simple web crawler written in python3 that traverses a single domain. It visits all pages within the domain but does not follow the links to external sites such as Google or Twitter.
The output is a site map of links such as the domain URLs, the external URLS and static content links.

## How to build and run the crawler
## Requirements
* The project is built with Python3
* The packages required to build and run the crawler are in the "requirements.txt" file

## Build
* You should first have Python3 installed on your system. To install Python3 on Linux Debian system, open the terminal and run:
```
$ sudo apt install python3 python3-devel
```
You now should build and run your project in a virtual environment. 
* First install 'virtualenv' package with:
```
$ pip install virtualenv
```
or 

```
$ sudo apt install virtualenv
```

* Then create a virtual environment:
Ex: 
```
$ virtualenv -p python3 venv
```

* Now activate your virtualenv by running:
```
$ source venv/bin/activate
```

* Install the required modules:
```
$ pip install -r requirements.txt
```

## Run
To run the crawler: 
* First clone the repository:
```
$ git clone git@github.com:Ginolux/simple-crawler.git
```

* Then, run the 'crawler.py' script in the virtual environment activated in the build section. The script takes as argument the top-level page's URL (such as the home page's URL), and search for a list of all links on the page. Every one of those links is then crawled recursively.
Ex:
```
$ python crawler.py http://wiprodigital.com
```

* The output is a simple structured site map showing links to other pages under the same domain.

## Docker
The crawler can be built and run faster using the automated built docker repository attached to this github repository.
* To build and run the docker container, run this single command with your domain URL:
Ex:
```
$ 
```
