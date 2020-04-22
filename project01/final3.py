from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import sqlite3

root = Tk()
root.title('Main Page')
root.geometry("400x400")
root.configure(bg='#D980FA')

Label(root, text = "An email has just sent by her!", font=('Helvetica',15,'bold'), fg='white', bg='#D980FA', pady=10).pack()
my_img = ImageTk.PhotoImage(Image.open('email3.gif'))
Label(image = my_img).pack()

def popup():
    response = messagebox.askyesno("Confirmation", "Are you sure?")
    if response == 1:
        # login = Tk()
        login=Toplevel()
        login.title("Login")
        login.geometry("280x215")
        login.configure(bg='#D980FA')
        
        def clkLogin():
            if id.get() == "kim1234" and pw.get() == "1q2w3e4r" :
                listPage = Toplevel()
                listPage.title('MailBox')
                listPage.geometry("350x500+100+100")
                listPage.resizable(False, False)

                frame1=Frame(listPage,  bd=1, height=50, bg="#AC58FA")
                frame1.pack(side="top", fill="both", expand=False)

                frame2=Frame(listPage, relief="flat", bd=2, bg='#D980FA')
                frame2.pack(side="bottom", fill="both", expand=True)

                def mail(event):
                    mail = Toplevel()
                    mail.title('Mail Contents')
                    mail.geometry("350x500+100+100")
                    mail.resizable(False, False)
                    mail.configure(bg='#D980FA')


                    msg = '읹 쓵렍긵얁& 폎샢 귽렌겑 삹앉랁3 헩얹젽'

                    def decode():
                        result=""
                        for i in msg:
                            if i not in (' '):
                                i=chr(ord(i)-5)
                                result+=i
                            else:
                                result+=' '
                        contents.insert(INSERT, result)


                    def reply():
                        reply = Toplevel()
                        reply.title("Reply")
                        reply.geometry("315x550")
                        reply.configure(bg='#D980FA')

                        frame3=Frame(reply,  bd=1, height=50, bg="#AC58FA")
                        frame3.pack(side="top", fill="both", expand=False)

                        frame4=Frame(reply, relief="flat", bd=2, bg='#D980FA')
                        frame4.pack(side="bottom", fill="both", expand=True)

                        conn = sqlite3.connect('reply.db')

                        c = conn.cursor()

                        # c.execute("""CREATE TABLE letter (
                        #         fromName text,
                        #         toName text,
                        #         address text,
                        #         contents text
                        #         )""")
                        def submit():

                            conn = sqlite3.connect('reply.db')

                            c = conn.cursor()

                            c. execute("INSERT INTO letter VALUES(:fromName, :toName, :address, :contents)",
                                    {
                                        'fromName':fromName.get(),
                                        'toName':toName.get(),
                                        'address':address.get(),
                                        'contents':contents.get()
                                    })

                            conn.commit()
                            conn.close()

                            fromName.delete(0, END)
                            toName.delete(0, END)
                            address.delete(0, END)
                            contents.delete(0, END)

                            response2 = messagebox.showinfo("Completion", "It is completely sent")

                        
                        def query():
                            conn = sqlite3.connect('reply.db')
                            c = conn.cursor()
                            
                            c.execute("SELECT *, oid FROM letter")
                            records = c.fetchall()

                            # text=Text(frame4, width=30, height = 8, bg='#D6A2E8', font = ('Helvetica', 9, 'bold'))
                            # text.grid(row=5, column=1)
                            text.delete(1.0, END)
                            text.insert('1.0','From : '+ str(records[-1][0])+"\n")
                            text.insert('2.0','To : '+ str(records[-1][1]) + "\n")
                            text.insert('3.0','Address : '+ str(records[-1][2]) + "\n")
                            text.insert('4.0','Contents : '+ str(records[-1][3]) + "\n")



                            # print_records = ''
                            # for record in records:
                            #     print_records += str(record) + " " "\n"

                            # query_label = Label(frame4, text = print_records)
                            # # query_label.grid(row = 6, columnspan = 2)
                            # query_label.grid(row = 5, columnspan = 2)

                            conn.commit()
                            conn.close()
                            return

                        def delete():
                                #database 또는 연결할 것 생성
                            conn = sqlite3.connect('reply.db')

                            #커서 생성
                            c = conn.cursor()

                            c.execute("DELETE from letter WHERE oid = " + delete_box.get())

                            #커밋 변경
                            conn.commit()

                            #연결 해제
                            conn.close()

                        def last():
                            response = messagebox.askyesno("Final Question", "종료하시겠습니까?")
                            if response == 1:
                                reply.destroy()
                                mail.destroy()

                                listPage.destroy()
                                login.destroy()
                                root.destroy()
                            else:
                                pass

                        reply_title_icon=ImageTk.PhotoImage(Image.open('writing1.gif'))
                        Label(frame3, image = reply_title_icon).grid(row=0,column=0)
                        reply_title_label=Label(frame3, text='   Writing Emails', font=('Helvetica',15,'bold'), fg='white', bg='#AC58FA')
                        reply_title_label.grid(row=0,column=1)
                        
                        fromName = Entry(frame4, width = 30)
                        fromName.grid(row = 0, column = 1)

                        toName = Entry(frame4, width = 30)
                        toName.grid(row = 1, column = 1)

                        address = Entry(frame4, width = 30)
                        address.grid(row = 2, column = 1)

                        contents = Entry(frame4, width = 30)
                        contents.grid(row = 3, column = 1, ipady=20)

                        delete_box = Entry(frame4, width = 30)
                        delete_box.grid(row = 9, column = 1, pady = 5)                        

                        fromName_label = Label(frame4, text = "From", font=('Helvetica',11,'bold'), fg='white', bg='#D980FA', pady=5)
                        fromName_label.grid(row = 0, column = 0)

                        toName_label = Label(frame4, text = "To", font=('Helvetica',11,'bold'), fg='white', bg='#D980FA', pady=5)
                        toName_label.grid(row = 1, column = 0)

                        address_label = Label(frame4, text = "Address", font=('Helvetica',11,'bold'), fg='white', bg='#D980FA', pady=5)
                        address_label.grid(row = 2, column = 0)

                        contents_label = Label(frame4, text = "Contents", font=('Helvetica',11,'bold'), fg='white', bg='#D980FA', pady=5)
                        contents_label.grid(row = 3, column = 0)

                        submit_btn = Button(frame4, text = "Send", command = submit, font=('Helvetica',9,'bold'))
                        submit_btn.grid(row = 4, column = 0, columnspan = 2, pady = 10, padx = 10)

                        query_btn = Button(frame4, text = "Confirmation", command = query, font=('Helvetica',9,'bold'))
                        query_btn.grid(row = 5, column = 0)

                        text=Text(frame4, width=30, height = 8, bg='#D6A2E8', font = ('Helvetica', 9, 'bold'))
                        text.grid(row=5, column=1)
                        
                        delte_box_label = Label(frame4, text = "input id")
                        delte_box_label.grid(row = 9, column = 0, pady = 5)

                        delete_btn = Button(frame4, text = "Delete", command = delete, font=('Helvetica',9,'bold'))
                        delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10)

                        last_btn = Button(frame4, text = "Close", command = last, font=('Helvetica',9,'bold'))
                        last_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10)

                        conn.commit()
                        conn.close()

                        reply.mainloop()

                    text = Text(mail)
                    text.insert(INSERT, msg)
                    text.place(x=10, y=30, width=320, height=150)

                    scroll_y = Scrollbar(text, orient="vertical", command=text.yview)
                    scroll_y.pack(side="right", expand=False, fill="y")
                    text.configure(yscrollcommand=scroll_y.set)


                    btn_dec = Button(mail, text = 'DECODE', command=decode, overrelief="solid", width=40, height=2, bg="#AC58FA")
                    btn_dec.place(x=10, y=200, width=320, height=40)

                    contents = tkst.ScrolledText(mail, width=33, height=3, wrap=WORD)
                    contents.place(x=10, y=260, width=320, height=150)

                    btn_list = Button(mail, text = 'MAILBOX', command=clkLogin, overrelief="solid", width=10, height=2, bg="#AC58FA")
                    btn_list.place(x=10, y=430, width=100, height=40)

                    btn_write = Button(mail, text = 'REPLY', command=reply, overrelief="solid", width=10, height=2, bg="#AC58FA")
                    btn_write.place(x=230, y=430, width=100, height=40)


                    mail.mainloop()


                mailbox_icon=ImageTk.PhotoImage(Image.open("mailbox.gif"))
                mailbox_icon_label=Label(frame1, image = mailbox_icon)
                mailbox_icon_label.grid(row = 0, column=0, pady=10, padx=18)

                mailbox_title=Label(frame1, text="000's MAILBOX", font=('Helvetica',20,'bold'), fg='white', bg='#AC58FA')
                mailbox_title.grid(row=0, column=1, pady=10, padx=5)

                values=["메일 리스트", "작성 중인 메일", "보낸 메일", "수신 완료 메일"] 
                combobox= ttk.Combobox(frame2, values=values)
                combobox.pack(pady=20)
                combobox.set("메일 리스트")

                listbox = Listbox(frame2, selectmode='extended', width=30, height=15, activestyle="dotbox")
                listbox.insert(0, "김희애님의 메일")
                listbox.insert(1, "오정연님의 메일")
                listbox.insert(2, "이규형님의 메일")
                listbox.insert(3, "박서준님의 메일")
                listbox.insert(4, "박해준님의 메일")
                listbox.pack()
                listbox.bind('<Double-1>', mail)

                listPage.mainloop()
            
        login_icon=ImageTk.PhotoImage(Image.open("user_icon.gif"))
        login_icon_label=Label(login, image = login_icon)
        login_icon_label.grid(row = 0, column=1, pady=10)

        id_label = Label(login, text = "I D", bg='#D980FA', font=('Helvetica',12,'bold'), fg='white', padx=5)
        id_label.grid(row=1, column=0)
        id = Entry(login, width=30)
        id.grid(row=1, column=1)

        pw_label = Label(login, text = "PW", bg='#D980FA', font=('Helvetica',12,'bold'), fg='white', padx=5)
        pw_label.grid(row=2, column=0)
        pw = Entry(login, width=30, show='*')
        pw.grid(row=2, column=1)

        btn1 = Button(login, text = "Login", command = clkLogin)
        btn1.grid(row=3, column=1, pady=10)

        login.mainloop()

    else:
        root.destroy()

startBtn = Button(root, text = "Open", command = popup).pack()
root.mainloop()