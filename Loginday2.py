import os
import ast
import re
import mmap
from tkinter import *
file=open("logins.txt","r")
data=file.read().replace('\n', '')
def check():
    found = False 
    for line in file:
        if username in line:
            print(line)
            return True
    return False
username=password=""
num_lines = sum(1 for line in open('logins.txt'))
print(num_lines)
p=open("passwords.txt","r")
start=Tk()
def begin():
    global password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton
    login_text=Label(start,text="Username:")
    login_text.pack()
    login_box=Entry(start,width=50)
    login_box.pack()
    password_text=Label(start,text="Password:")
    password_text.pack()
    password_box=Entry(start,width=50,show="•")
    password_box.pack()
    login_button=Button(start,text="Login",command=login)
    login_button.pack()
    newaccountbutton=Button(start,text="Create a new account",command=newaccount)
    newaccountbutton.pack()

def login():
    global password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton
    username=login_box.get()
    password=password_box.get()
    print("login")
    print(data)
    data=ast.literal_eval(data)
    password_list=ast.literal_eval(open("passwords.txt","r").read())
    print(username)
    if username in data:
        print("found username")
        position=data.index(username)
        print(position)
    if password==password_list[position]:
        print("password correct")
        success()
    else:
        print("password incorrect")
def newaccount():
    global password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton
    print("newa")

def success():
    global password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,success_text
    login_text.pack_forget()
    login_box.pack_forget()
    password_text.pack_forget()
    password_box.pack_forget()
    login_button.pack_forget()
    newaccountbutton.pack_forget()
    success_text=Label(start,text="Login success")
    success_text.pack()
    ex=Button(start,text="quit",command=end)
    ex.pack()

def end():
    quit()
    


begin()
