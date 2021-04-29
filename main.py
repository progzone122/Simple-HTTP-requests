from tkinter import *
from textwrap import wrap
import requests

root = Tk()  
root.title("API")
root.geometry('570x400')
url1 = ""
url2 = ""
key = ""
value = ""
response = ""
response1 = ""
response2 = ""

header_font = ("Times", 18)
text_font = ("Times", 12)
txt_font = ("Times", 16)


def post():
    global url1
    global key
    global value
    global response1
    #
    url1 = txt_url1.get()
    
    if url1 != "":
        key=txt_key.get()
        value=txt_val.get()
        
        response1 = requests.post(url1, data = {key:value})
        response = response1
        listbox.delete(0, END)
        listbox.insert(0, response)
    else:
        print("Ошибка! Вы не ввели ссылку на источник POST запроса")
    exit
#
def get():
    global url2
    global response2
    #
    url2 = txt_url2.get()
    
    if url2 != "":
        response2 = requests.get(url2)
        response = response2.text.split(',')
        i = 0
        l = len(response)
        listbox.delete(0, END)
        while i < l:
            listbox.insert(i, response[i])
            i = i + 1
    else:
        print("Ошибка! Вы не ввели ссылку на источник GET запроса")
    exit







#
lbl1 = Label(root, text="Отправить POST запрос", font=header_font)
lbl_url = Label(text="URL:", font=text_font)
txt_url1 = Entry(root, width=46, font=txt_font)
lbl_key = Label(text="Ключ:", font=text_font)
lbl_val = Label(text="Значение:", font=text_font)
txt_key = Entry(root, width=14, font=txt_font)
txt_val = Entry(root, width=14, font=txt_font)
btn1 = Button(root, width=15, text="Отправить", command=post)

lbl2 = Label(root, font=header_font, text="Отправить GET запрос")
lbl_url2 = Label(text="URL:", font=text_font)
txt_url2 = Entry(root, width=35, font=txt_font)
btn2 = Button(root, width=15, text="Отправить", command=get)
lbl_resp = Label(root, font=text_font, text="Ответ от сервера:")
listbox = Listbox(root, height = 8, 
                  width = 70, 
                  activestyle = 'dotbox', 
                  font = text_font)
#
txt_url1.insert(0, "https://paphian-yield.000webhostapp.com/api/post.php")
txt_url2.insert(0, "https://paphian-yield.000webhostapp.com/api/get.php")
#
lbl1.place(x=1, y=0)
lbl_url.place(x=1, y=30)
txt_url1.place(x=50, y=30)
lbl_key.place(x=1, y=60)
txt_key.place(x=50, y=60)
lbl_val.place(x=210, y=60)
txt_val.place(x=283, y=60)
btn1.place(x=445, y=60)

lbl2.place(x=1, y=90)
lbl_url2.place(x=1, y=120)
txt_url2.place(x=50, y=120)
btn2.place(x=445, y=120)
lbl_resp.place(x=1, y=150)
listbox.place(x=1, y=180)
#
root.mainloop()
