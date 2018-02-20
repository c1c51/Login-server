import os
import ast
import re
from tkinter import *
file=open("logins.txt","r")
data=file.read().replace('\n', '')
filep=open("passwords.txt","r")
datap=filep.read().replace("\n","")
username=password=""
start=Tk()
def begin():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newaccountsuccesstext,newaccountsuccesslogin
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
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
    username=login_box.get()
    file=open("logins.txt","r")
    data=file.read().replace('\n', '')
    password=password_box.get()
    filep=open("passwords.txt","r")
    datap=filep.read().replace("\n","")
    print("login")
    print(data)
    print(datap)
    username_list=ast.literal_eval(data)
    password_list=ast.literal_eval(datap)
    print(username)
    if username in username_list:
        print("found username")
        position=username_list.index(username)
        print(position)
        print(password_list[position])
        
    try:
        if password==password_list[position]:
            print("password correct")
            success()
        else:
            print("password incorrect")
            password_box.delete(0, 'end')
            password_text.config(text="Password:incorrect")
    except:
        print("user incorrect")
        login_text.config(text="Username: Incorrect")
def newaccount():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
    print("newa")
    newaccountset=Button(start,text="create account",command=setaccount)
    login_button.pack_forget()
    newaccountbutton.pack_forget()
    newaccountset.pack()
def setaccount():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
    print("hi")
    login_text.pack_forget()
    login_box.pack_forget()
    password_text.pack_forget()
    password_box.pack_forget()
    username_list=ast.literal_eval(data)
    password_list=ast.literal_eval(datap)
    username=login_box.get()
    password=password_box.get()
    username_list.append(username)
    password_list.append(password)
    print(username_list)
    print(password_list)
    username_write=open("logins.txt","w")
    password_write=open("passwords.txt","w")
    username_list=str(username_list)
    password_list=str(password_list)
    username_write.write(username_list)
    password_write.write(password_list)
    username_write.close()
    password_write.close()
    newaccountcreated()
def newaccountcreated():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
    newaccountset.pack_forget()
    newaccountsuccesstext=Label(start,text="New account created")
    newaccountsuccesslogin=Button(start,text="Login",command=restart)
    newaccountsuccesstext.pack()
    newaccountsuccesslogin.pack()
def restart():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
    newaccountsuccesstext.pack_forget()
    newaccountsuccesslogin.pack_forget()
    begin()
def success():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
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
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap
    quit()
    


begin()
