import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def write_csv(nama_file, isi, tipe='w'):
    with open(nama_file, mode=tipe) as tbl:
        tbl_writer = csv.writer(tbl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in isi:
            tbl_writer.writerow(row)

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

# BoW using library
vectorizer = CountVectorizer(min_df=1, ngram_range=(1,1))
BoW_matrix = vectorizer.fit_transform(corpus)
write_csv("bow_lib.csv", BoW_matrix.toarray())

# calculating TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
feature_name = vectorizer.get_feature_names()

#print(tfidf_matrix)
write_csv("tfidf.csv", [feature_name])
write_csv("tfidf.csv", tfidf_matrix.toarray(), 'a')

# Clustering
kmeans = KMeans(n_clusters=5, random_state=0).fit(tfidf_matrix.todense())
write_csv("Kluster_label.csv", [kmeans.labels_])
for i in range(len(kmeans.labels_)):
    print("Doc %d =>> cluster %d" %(i+1, kmeans.labels_[i]))

