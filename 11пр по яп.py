import json

import requests
import tkinter as tk
from tkinter import *
from pprint import pprint

def pars():
    data = {}
    nickname = input_nick.get()
    nickname = f"https://api.github.com/users/{nickname}"
    user_data = requests.get(nickname).json()
    company, created_at, email = user_data['company'], user_data['created_at'], user_data['email']
    id, name, url = user_data['id'], user_data['name'], user_data['url']

    data['company'], data['created_at'], data['email'] = company, created_at, email
    data['id'], data['name'], data['url'] = id, name, url

    pprint(company)
    pprint(created_at)
    pprint(email)
    pprint(id)
    pprint(name)
    pprint(url)

    with open('data.json', 'w') as f:
        json.dump(data, f)


win = tk.Tk()
win.geometry(f"240x270+100+200")
win['bg'] = '#33ffe6'
win.title('Бобров Андрей Евгеньевич')

input_nick = StringVar()

text_pole = Entry(width=35, insertbackground='black', textvariable=input_nick)
text_pole.pack(ipady=1)
btn = Button(width=20, height=4, text='Get json', bg='#6B8E23', command=pars)
btn.pack(ipady=20)

win.mainloop()