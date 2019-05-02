# How To: Mining Web Data Using Beautiful Soup Scraping

This Tutorial was Authored by  [LtYurisaki](https://github.com/LtYurisaki/).

## Getting Started

Web mining is the application of data mining techniques to discover patterns from the World Wide Web. As the name proposes, this is information gathered by mining the web. It makes utilization of automated apparatuses to reveal and extricate data from servers and web2 reports, and it permits organizations to get to both organized and unstructured information from browser activities, server logs, website and link structure, page content and different sources.

The goal of Web structure mining is to generate structural summary about the Web site and Web page. Technically, Web content mining mainly focuses on the structure of inner-document, while Web structure mining tries to discover the link structure of the hyperlinks at the inter-document level. Based on the topology of the hyperlinks, Web structure mining will categorize the Web pages and generate the information, such as the similarity and relationship between different Web sites.

Web structure mining can also have another direction -- discovering the structure of Web document itself. This type of structure mining can be used to reveal the structure (schema) of Web pages, this would be good for navigation purpose and make it possible to compare/integrate Web page schemes. This type of structure mining will facilitate introducing database techniques for accessing information in Web pages by providing a reference schema.

Cited from  [Wikipedia](https://en.wikipedia.org/wiki/Web_mining).



## Crawling with Beautiful Soup

Beautiful Soup Documentation¶
"The Fish-Footman began by producing from under his arm a great letter, nearly as large as himself."
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

These instructions illustrate all major features of Beautiful Soup 4, with examples. I show you what the library is good for, how it works, how to use it, how to make it do what you want, and what to do when it violates your expectations.

The examples in this documentation should work the same way in Python 2.7 and Python 3.2.

You might be looking for the documentation for [Beautiful Soup 3](https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html).. If so, you should know that Beautiful Soup 3 is no longer being developed, and that Beautiful Soup 4 is recommended for all new projects. If you want to learn about the differences between Beautiful Soup 3 and Beautiful Soup 4, see [Porting code to BS4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#porting-code-to-bs4).

Cited from  [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).



## Overview


Simple yet, here the list of all thing you need for our web scraping session


* `Python ver 2.0 Above` - Main language we'll use.
* `Python pip` - For ease to install other python lib.
* `Beautiful soup library` - Most easy to use for web scraping(according to writters).
* `Sastrawi (or other equivalent local language dictionary) library` - Dictionary as base so our programs can recognize words to take or not.
* `Request library` - Put a URL and this will do the rest for you.
* `Sklearn library` - No need for confusing computation since sklearn will do it instead.
* `Sqlite (or other equivalent DBMS)` - We need to save our work don't we?.

## Installation

In order for our works, you'll need Python installed on your system, as well as the Python package manager, pip. You can check if you have these already installed from the command line:

    $ python --version
	Python 2.7.2
	$ pip --version
	pip 1.5.2


*`Installing Python`

[Install Python](https://www.python.org/) by downloading an installer appropriate for your system from [python.org](https://www.python.org/downloads/) and running it.

		Note

		If you are installing Python on Windows, be sure to check the box to have Python added to your PATH if the installer offers such an option (it's normally off by default).

*`Installing pip`

If you're using a recent version of Python, the Python package manager, pip, is most likely installed by default. If you need to install [pip](https://pip.readthedocs.io/en/stable/installing/) for the first time, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run the following command to install it:

	python get-pip.py

*`Installing pip`

If you're using a recent version of Python, the Python package manager, pip, is most likely installed by default. If you need to install [pip](https://pip.readthedocs.io/en/stable/installing/) for the first time, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Then run the following command to install it:

	python get-pip.py

