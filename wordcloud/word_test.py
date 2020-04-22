from wordcloud import WordCloud
from matplotlib import pyplot
from collections import Counter
from konlpy.tag  import Okt
 

import tkinter
import tkinter.messagebox as box
import numpy as np
import pandas as pd
from io import StringIO
from datetime import datetime, timedelta
from tkinter.font import Font
import cv2


text = ''
with open("C:/Users/Hajin_2/python/python/BigData_prj/KoNLPy.txt", encoding="utf-8") as f:
    text = f.read()

nlp = Okt()

nouns = nlp.nouns(text)

words = []
for n in nouns:
    if len(n) > 1:
        words.append(n)

count = Counter(words)

most = count.most_common(100)

tags = {}
for n, c in most:
    tags[n] = c

wc = WordCloud(background_color='white',font_path="C:/Users/Hajin_2/python/python/BigData_prj/NanumBarunGothic.ttf",  width=300, height=300,
                scale=2.0, max_font_size=250)

gen = wc.generate_from_frequencies(tags)

pyplot.figure()
pyplot.imshow(gen, interpolation='bilinear')
wc.to_file("KoNLPy4.png")
pyplot.close()



# img = cv2.imread('C:/Users/Sean/project/MariaDB/KoNLPy4.png', cv2.IMREAD_COLOR)
# cv2.imshow('KoNLPy img2', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#@@@@@@@@@@@@@@@@@@@@@@@@

window = tkinter.Tk()
window.title("워드 클라우드")
window.geometry("610x610",)
window.resizable(False, False)



img2 = tkinter.PhotoImage(file = 'C:/Users/Hajin_2/python/python/BigData_prj/KoNLPy4.png')
small_img = tkinter.PhotoImage.subsample(img2, x = 4, y = 4)

label=tkinter.Label(window, text=' trend ', font = ('Arial' , 10), relief="solid",  image = img2) 
label.place( anchor="nw",)