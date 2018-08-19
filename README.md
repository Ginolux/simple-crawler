[![wercker status](https://app.wercker.com/status/924382abdf77d8e6c394c8525c8983ed/s/master "wercker status")](https://app.wercker.com/project/byKey/924382abdf77d8e6c394c8525c8983ed)
# simple-crawler
      
Simple-crawler is a simple web crawler written in python3 that traverses a single domain. It visits all pages within the domain but does not follow the links to external sites such as Google or Twitter.
The output is a site map of links such as the domain URLs, the external URLS and static content links.
      
      
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
      
* Then, run the 'crawler.py' script in the virtual environment activated in the build section. The script takes as argument the top-level page's URL (such as the home page's URL), and searches for a list of all links on the page. Every one of those links is then crawled recursively.  
Ex:
```
$ python crawler.py http://wiprodigital.com
```
       
* The output is a simple structured site map showing links to other pages under the same domain.
      
      
## Docker
The crawler can be built and run faster using the automated build docker repository 'ginolux/simple-crawler' attached to this github repository.

* To build and run the docker container, run this single command with your domain URL:  
Ex:
```
$ docker run --rm -it ginolux/simple-crawler  http://wiprodigital.com
```

The container will be automatically removed after execution.
      
      
## Potential trade-offs
### Exception handling
Due to the dynamic aspect of the web, exceptions should be well handle to avoid unexpected issue during crawling. The Web is dynamic with different type of contents. Therefore, fine grain exception handling mecanisms should be implemented in the crawler.
      
### Depth of the website
The script crawls the domain recursively starting from the top-level page such as the home page. A domain with more than a 1000 link deep will blow up the crawler because Python has a recursion limit of 1000.
To prevent this, a recursion counter can be implemented.
The recursion technique may not be suitable for extremely large sites such as wikipedia. 
      
### JavaScript
Nowadays, many websites are implemented in JavaScript to take advantage of the dynamic features provided by the language to the browser. A simple crawler like this fails to retrieve all the data from the site especially data manipulated by JavaScript. Selenium is a tool that can be used to interact with the JavaScript content to retrieve the missing data.
      
      
## Could be done with more time
### Retry failed links
Failed links with error code could be retry a second time, even third time because poor connection could lead to failing connection with the server.

### Database
At this point, the crawler only print the data collected to the terminal screen. To analyse the data further with more flexibility, is it better to use a database. With more time, URLs can be stored in a MySQL database for late analysis. 
      
### Crawling in parallel
Although web crawling is fast, in some situations parallel web crawling such as running parallel threads or processes can be benefit.
With more time, multithread/multiprocess crawler can be implemented.