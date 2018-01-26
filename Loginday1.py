import os
import re
import mmap
from tkinter import *
username=password=""
p=open("passwords.txt","r")
start=Tk()
def begin():
    global username,password
    login_text=Label(start,text="Username:")
    login_text.pack()
    login_box=Entry(start,textvariable=username,width=50)
    login_box.pack()
    password_text=Label(start,text="Password:")
    password_text.pack()
    password_box=Entry(start,textvariable=password,width=50,show="•")
    password_box.pack()
    login_button=Button(start,text="Login",command=login)
    login_button.pack()
    newaccountbutton=Button(start,text="Create a new account",command=newaccount)
    newaccountbutton.pack()



def login():
    global username,password,f,mf,m
    print("login")
   

    with open("logins.txt", 'rb') as file:
        logins=file.read()
    print(logins)

    
def newaccount():
    print("newa")



begin()
