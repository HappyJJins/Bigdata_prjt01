import tkinter
import tkinter.font
import webbrowser

from tkinter import *
from tkinter import ttk

from PIL import Image
import os
import pyglet
import PIL

window=tkinter.Tk()
window.title("크롤링 프로젝트")
window.geometry("800x600+200+100")
window.resizable(False,False)

#리스트박스 폰트
ListBox_Font = tkinter.font.Font(family = "굴림", size=14, weight = "normal")

#키워드 라벨 폰트
KeyWord_Font = tkinter.font.Font(family = "굴림", size=28, weight = "bold")

#요소별 제목 폰트
Content_Font = tkinter.font.Font(family = "굴림", size=14, weight = "bold")


#상단부분
def Cate(): 
    values=['전체', '정치', '사회', 'IT', '과학', '문화', '경제']  # 신문기사 내용 분류

    #상단부분 프레임
    Category_Frame = tkinter.Frame(window, relief="solid", bd=2, width= 820, height=150)
    Category_Frame.place(x=-10, y=-10)

    #카테고리 콤보박스 라벨
    Category_Combo_Label = tkinter.Label(Category_Frame, text="분야", font = Content_Font)
    Category_Combo_Label.place(x=140, y=40)

    #카테고리 콤보박스
    Category_ComboBox = tkinter.ttk.Combobox(Category_Frame, height=15, values=values)
    Category_ComboBox.place(x=80, y=70)
    Category_ComboBox.set("목록 선택")
    Category_ComboBox.get()



    #검색기간 라벨
    Category_Date_Label = tkinter.Label(Category_Frame, text="기간설정", font = Content_Font)
    Category_Date_Label.place(x=540, y=40)

    #검색기간 설정(Start에서 시작 End에서 끝)
    Category_Date_Start = tkinter.Entry(Category_Frame, width=10)
    Category_Date_Start.place(x=470, y=70)

    Category_Date=tkinter.Label(Category_Frame, text="~", font=20)
    Category_Date.place(x=540,y=70)

    Category_Date_End = tkinter.Entry(Category_Frame, width=10)
    Category_Date_End.place(x=558, y=70)

    #검색기간 설정
    Category_Date_Search = tkinter.Button(Category_Frame, text="검색", height=1)
    Category_Date_Search.place(x=640,y=67)

#Category_Date_Search 버튼을 누르면 하단부분 기간과 Category 설정한 분야의 뉴스가 나옴
#KeyWord_List 선택시 키워드에 해당하는 뉴스를 필터링해서 출력


#하단부분
def Main(): 
    #하단부분 프레임
    Main_Frame = tkinter.Frame(window, relief="solid", bd=1, width= 800, height=460)
    Main_Frame.place(x=0, y=140)

    # 라벨
    Main_List_Label = tkinter.Label(Main_Frame, text="뉴스 리스트", font = Content_Font)
    Main_List_Label.place(x=40, y=10)

    #뉴스리스트 프레임
    News_Word_Frame = tkinter.Frame(Main_Frame, relief="solid", bd=1, width= 500, height=385)
    News_Word_Frame.place(x=40, y=40)

    # #뉴스리스트 라벨
    # Main_ListBox = tkinter.Listbox(Main_Frame, selectmode='extended', height=19, width=50, font=ListBox_Font)
    # Main_ListBox.insert(0, "1번")
    # Main_ListBox.insert(1, "2번")
    # Main_ListBox.insert(2, "3번")
    # Main_ListBox.place(x=40, y=40)


    #키워드부분 라벨
    KeyWord_Label = tkinter.Label(Main_Frame, text="키워드", font=KeyWord_Font)
    KeyWord_Label.place(x=610, y=50)

    #키워드리스트
    KeyWord_ListBox = tkinter.Listbox(Main_Frame, relief="solid", bd=1, width= 20, height=16, font=ListBox_Font)
    KeyWord_ListBox.place(x=570, y=101)

    KeyWord_ListBox.insert(0, "전체 보여주기")
    KeyWord_ListBox.insert(1, "1번 키워드")
    KeyWord_ListBox.insert(2, "2번 키워드")
    KeyWord_ListBox.insert(3, "3번 키워드")


    window.mainloop()

if __name__ == "__main__":
    Cate()
    Main()
