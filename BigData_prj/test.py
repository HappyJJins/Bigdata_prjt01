import mysql.connector
import re

from konlpy.tag import Twitter
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

import pytagcloud
import webbrowser

from wordcloud import WordCloud

db = mysql.connector.connect(
    user='root', password='root', host='127.0.0.1', database='bigdata_prjt',
    port=3307,charset='utf8',autocommit=True)
cursor = db.cursor()
cursor.execute("SELECT * from crowling where category='politics' and date='20200421'")
data = cursor.fetchone()
# print(data[2])
politics=" ".join(set(data[2].split("|")))
politics=politics.split(" ")
# print(politics)

npolitics = []
p1 = re.compile(r'[[].*[]]|[(].*[)]')

for i in politics:
    npolitics.append(p1.sub("", i))
npolitics=str(npolitics)

def showGraph(wordInfo):
    
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)
    
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

    plt.show()

def wordCloud(wordInfo):
    wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf', background_color='white',colormap = "Accent_r", width=1500, height=1000).generate_from_frequencies(wordInfo)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

nlp = Twitter()
nouns = nlp.nouns(npolitics)
count = Counter(nouns)  

wordInfo = dict()
for tags, counts in count.most_common(20):
    if (len(str(tags)) > 1):
        wordInfo[tags] = counts
        print ("%s : %d" % (tags, counts))
        
# showGraph(wordInfo)
wordCloud(wordInfo)


db.close()