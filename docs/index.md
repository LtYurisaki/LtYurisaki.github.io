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

*`Installing Beautiful Soup`

You might be looking for the documentation for [Beautiful Soup 3](https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html).. If so, you should know that Beautiful Soup 3 is no longer being developed, and that Beautiful Soup 4 is recommended for all new projects. If you want to learn about the differences between Beautiful Soup 3 and Beautiful Soup 4, see [Porting code to BS4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#porting-code-to-bs4).

	pip install beautifulsoup4

Remember to change the cmd directory on pip location. For ubuntu and Mac os can be seen [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

*`Installing Sastrawi`

Sastrawi can be installed via pip, by running the following commands in terminal/command prompt : 

	pip install Sastrawi


*`Installing Request`

The good news is that there are a few ways to install the Requests library. To see the full list of options at your disposal, you can view the official install documentation for Requests here.
You can make use of pip, easy_install, or tarball.If you’d rather work with source code, you can get that on GitHub, as well.
For the purpose of this guide, we are going to use pip to install the library. 
In your Python interpreter, type the following:

	pip install requests 


*`Installing Scikit-learn`

Scikit-learn requires:

Python (>= 2.7 or >= 3.4),
NumPy (>= 1.8.2),
SciPy (>= 0.13.3).

		Warning Scikit-learn 0.20 is the last version to support Python 2.7 and Python 3.4. Scikit-learn 0.21 will require Python 3.5 or newer.
		If you already have a working installation of numpy and scipy, the easiest way to install scikit-learn is 

using pip

	pip install -U scikit-learn

or conda:

	conda install scikit-learn


*`Installing Sqlite

Eternal link [here](http://www.sqlitetutorial.net/download-install-sqlite/)



## Web Crawling

Here’s an HTML document I’ll be using as an example throughout this document. It’s part of a story from Alice in Wonderland:

	html_doc = """
	<html><head><title>The Dormouse's story</title></head>
	<body>
	<p class="title"><b>The Dormouse's story</b></p>

	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>

	<p class="story">...</p>
	"""
Running the “three sisters” document through Beautiful Soup gives us a BeautifulSoup object, which represents the document as a nested data structure:

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_doc, 'html.parser')

	print(soup.prettify())
	# <html>
	#  <head>
	#   <title>
	#    The Dormouse's story
	#   </title>
	#  </head>
	#  <body>
	#   <p class="title">
	#    <b>
	#     The Dormouse's story
	#    </b>
	#   </p>
	#   <p class="story">
	#    Once upon a time there were three little sisters; and their names were
	#    <a class="sister" href="http://example.com/elsie" id="link1">
	#     Elsie
	#    </a>
	#    ,
	#    <a class="sister" href="http://example.com/lacie" id="link2">
	#     Lacie
	#    </a>
	#    and
	#    <a class="sister" href="http://example.com/tillie" id="link2">
	#     Tillie
	#    </a>
	#    ; and they lived at the bottom of a well.
	#   </p>
	#   <p class="story">
	#    ...
	#   </p>
	#  </body>
	# </html>
Here are some simple ways to navigate that data structure:

	soup.title
	# <title>The Dormouse's story</title>

	soup.title.name
	# u'title'

	soup.title.string
	# u'The Dormouse's story'

	soup.title.parent.name
	# u'head'

	soup.p
	# <p class="title"><b>The Dormouse's story</b></p>

	soup.p['class']
	# u'title'

	soup.a
	# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

	soup.find_all('a')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.find(id="link3")
	# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
	One common task is extracting all the URLs found within a page’s <a> tags:

	for link in soup.find_all('a'):
	    print(link.get('href'))
	# http://example.com/elsie
	# http://example.com/lacie
	# http://example.com/tillie
	Another common task is extracting all the text from a page:

	print(soup.get_text())
	# The Dormouse's story
	#
	# The Dormouse's story
	#
	# Once upon a time there were three little sisters; and their names were
	# Elsie,
	# Lacie and
	# Tillie;
	# and they lived at the bottom of a well.
	#
	# ...
Does this look like what you need? If so, read on.


## Let's put in on practice

first we put all library we need for on tops.

	import requests
	from bs4 import BeautifulSoup
	import sqlite3
	import csv
	from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
	from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
	from sklearn.feature_extraction.text import CountVectorizer
	from sklearn.feature_extraction.text import TfidfVectorizer
	from sklearn.cluster import KMeans

the import csv was used so we can easy to access the result, so:.

	def write_csv(nama_file, isi, tipe='w'):
	    with open(nama_file, mode=tipe) as tbl:
	        tbl_writer = csv.writer(tbl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	        for row in isi:
	            tbl_writer.writerow(row)

we put it on func so we can call it any time.

	def crawl(src):
	    global c
	    try :
	        page = requests.get(src)
	        soup = BeautifulSoup(page.content, 'html.parser')
	        kata = soup.findAll('tr')
	        penutur = soup.findAll(class_='firstHeading')

	        for i in range(len(kata)):
	            a = kata[i].getText()
	            b = penutur[0].getText()
	            conn.execute('INSERT INTO Kata(Katas, Penutur) VALUES ("%s", "%s")' %(a, b));

	    except ValueError:
	        print('Download selesai')

its the most basic we can use from beautiful soups.

	conn = sqlite3.connect('dbs.db')
	c = 1
	choice = input("Perbarui data? Y/T ").upper()
	if choice == "Y":
	    conn.execute('drop table if exists Kata')
	    conn.execute('''CREATE TABLE Kata
	             (Katas TEXT NOT NULL,
	             Penutur TEXT NOT NULL);''')
	    crawl("https://id.wikiquote.org/wiki/Plato")
	    crawl("https://id.wikiquote.org/wiki/William_Jones_(ahli_bahasa)")
	    crawl("https://id.wikiquote.org/wiki/Isaac_Asimov")
	    crawl("https://id.wikiquote.org/wiki/Edsger_Dijkstra")
	    crawl("https://id.wikiquote.org/wiki/Benjamin_Franklin")
	    crawl("https://id.wikiquote.org/wiki/Archimedes")
	    crawl("https://id.wikiquote.org/wiki/Albert_Einstein")
	    crawl("https://id.wikiquote.org/wiki/Marcus_Aurelius")
	    crawl("https://id.wikiquote.org/wiki/Jean-Paul_Sartre")
	    crawl("https://id.wikiquote.org/wiki/Epictetus")
	    crawl("https://id.wikiquote.org/wiki/Vladimir_Putin")
	    crawl("https://id.wikiquote.org/wiki/Xi_Jinping")
	    crawl("https://id.wikiquote.org/wiki/Abraham_Lincoln")
	    crawl("https://id.wikiquote.org/wiki/Adolf_Hitler")
	    crawl("https://id.wikiquote.org/wiki/Askar_Akayev")
	    crawl("https://id.wikiquote.org/wiki/Tsai_Ing-wen")
	    crawl("https://id.wikiquote.org/wiki/Shimon_Peres")
	    crawl("https://id.wikiquote.org/wiki/Tan_Malaka")
	    crawl("https://id.wikiquote.org/wiki/Betty_Smith")
	    crawl("https://id.wikiquote.org/wiki/Mark_Twain")
	    crawl("https://id.wikiquote.org/wiki/Petrus_Josephus_Zoetmulder")
	    cursor = conn.execute("SELECT * from Kata")
	    for row in cursor:
	        print(row)
	    conn.commit()

## Preproccesing

	def preprosesing(txt):
	    SWfactory = StopWordRemoverFactory()
	    stopword = SWfactory.create_stop_word_remover()

	    stop = stopword.remove(txt)
	    Sfactory = StemmerFactory()
	    stemmer = Sfactory.create_stemmer()

	    stem = stemmer.stem(stop)
	    return stem

	def countWord(txt):
	    d = dict()
	    for i  in txt.split():
	        if d.get(i) == None:
	            d[i] = txt.count(i)
	    return d

## Building VSM

	def add_row_VSM(d):
	    VSM.append([])
	    for i in VSM[0]:
	        if d.get(i) == None:
	            VSM[-1].append(0)
	        else :
	            VSM[-1].append(d.pop(i));
		
    for i in d:
        VSM[0].append(i)
        for j in range(1, len(VSM)-1):
            VSM[j].append(0)
        VSM[-1].append(d.get(i))

	print("Please Wait. Building VSM...")
	cursor = conn.execute("SELECT * from Kata")
	cursor = cursor.fetchall()
	pertama = True
	corpus = list()
	c=1
	for row in cursor:
	    #print ('Proses : %.2f' %((c/len(cursor))*100) + '%'); c+=1
	    txt = row[0]
	    cleaned = preprosesing(txt)
	    corpus.append(cleaned)
	    d = countWord(cleaned)
	    if pertama:
	        pertama = False
	        VSM = list((list(), list()))
	        for key in d:
	            VSM[0].append(key)
	            VSM[1].append(d[key])
	    else:
	        add_row_VSM(d)
	    #VSM[-1].append(row[2])
	    #VSM[-1].append(row[3])

	with open('tableview.csv', mode='w') as tbl:
	    tbl_writer = csv.writer(tbl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    for row in VSM:
	        tbl_writer.writerow(row)

	write_csv("bow_manual.csv", VSM)

## Counting Filtered Word

	# BoW using library
	vectorizer = CountVectorizer(min_df=1, ngram_range=(1,1))
	BoW_matrix = vectorizer.fit_transform(corpus)
	write_csv("bow_lib.csv", BoW_matrix.toarray())

## Calculating TF-IDF 

	# calculating TF-IDF
	vectorizer = TfidfVectorizer()
	tfidf_matrix = vectorizer.fit_transform(corpus)
	feature_name = vectorizer.get_feature_names()

	#print(tfidf_matrix)
	write_csv("tfidf.csv", [feature_name])
	write_csv("tfidf.csv", tfidf_matrix.toarray(), 'a')

## Clustering Result

	# Clustering
	kmeans = KMeans(n_clusters=5, random_state=0).fit(tfidf_matrix.todense())
	write_csv("Kluster_label.csv", [kmeans.labels_])
	for i in range(len(kmeans.labels_)):
	    print("Doc %d =>> cluster %d" %(i+1, kmeans.labels_[i]))

## Afterword

And with that, we just learned how to scrape data with Beautiful Soup which, in my opinion, is quite easy in comparison with regular expression and CSS selectors. And just so you are aware, this is just one of the ways of scraping data with Python.

And just to reiterate this important point: web scraping is legal in one context, and illegal in another. Before you scrape data from a webpage, it is strictly advisable to check the bot rules of a website by appending the robots.txt at the end of the URL, just like this: www.example.com/robots.txt. Your IP address may be restricted till further notice if you fail to do so. Hope you’ll use the skill you just learned appropriately, cheers!