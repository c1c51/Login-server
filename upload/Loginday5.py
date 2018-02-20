import ast
from tkinter import *
capital=lower=symbol=number=debugq=restart=0
file=open("logins.txt","r")
data=file.read().replace('\n', '')  #opens files
filep=open("passwords.txt","r")
datap=filep.read().replace("\n","")
username=password=""
start=Tk()
start.title("Login into the secure server")
start.configure(background="#0099ff")

#generates boxes and text and buttons etc
def begin():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    login_text=Label(start,text="Username:",bg="#0099FF")
    login_text.pack()
    login_box=Entry(start,width=50,background="#FF6600") 
    login_box.pack()
    password_text=Label(start,text="Password:",bg="#0099FF")
    password_text.pack()
    password_box=Entry(start,width=50,show="•",background="#FF6600")
    password_box.pack()
    login_button=Button(start,text="Login",command=login,bg="#0099FF")
    login_button.pack()
    newaccountbutton=Button(start,text="Create a new account",command=newaccount,bg="#0099FF")
    newaccountbutton.pack()

        
def debug():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    debug.pack_forget()
    print("debug")          #toggles debug mode on
    debugq=1

#checks the values of the boxes against the file
def login():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    debug.pack_forget()
    username=login_box.get()
    file=open("logins.txt","r")
    data=file.read().replace('\n', '')
    password=password_box.get()
    filep=open("passwords.txt","r")
    datap=filep.read().replace("\n","")
    username_list=ast.literal_eval(data)
    password_list=ast.literal_eval(datap)       #converts content of files to list form
    if debugq==1:
        print("login")
        print(data)                 
        print(datap)
        print(username)
    if username in username_list:
        position=username_list.index(username)          #checks if username is in the list
        if debugq==1:
            print("found username")
            print(position)
            print(password_list[position])
    else:
        if debugq==1:
            print("user incorrect")
        login_text.config(text="Username: Incorrect")
        return
    if password==password_list[position]:           #checks if the password is correct
        if debugq==1:
            print("password correct")
        success()
    else:
        if debugq==1:
            print("password incorrect")
        password_box.delete(0, 'end')
        password_text.config(text="Password:incorrect")
        position=-1

#changes the standard screen for creating a new account
def newaccount():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    debug.pack_forget()
    if debugq==1:
        print("newa")
    newaccountset=Button(start,text="create account",command=checkaccount,bg="#0099FF")
    login_button.pack_forget()
    newaccountbutton.pack_forget()
    newaccountset.pack()
    newerror=Label(start,text="",bg="#0099FF")
    newerror.pack()
    username_list=ast.literal_eval(data)
    password_list=ast.literal_eval(datap)   #converts file contents to list

def checkaccount():
    #checks if the username is taken and if password is the correct strength 
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    
    username=login_box.get()
    password=password_box.get()
    if username in username_list:
        newerror.config(text="Username taken")
        return
    else:
        for char in password:
            if "A" <= char <= "Z":              #checks if password is secure enough
                capital=1
            elif "a"<= char<="z":
                 lower=1
            elif 32<=ord(char)<=47 or 58<=ord(char)<=64 or 91<=ord(char)<=96 or 123<=ord(char)<=126 or ord(char)>=128:
                symbol=1
            elif 48<=ord(char)<=57:
                number=1
    if capital+lower+symbol+number==4:
        setaccount()
    else:
        newerror.config(text="Strong password required")
        return
        
            
#creates the new account
def setaccount():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    if debugq==1:
        print("setaccount")

    newerror.pack_forget()
        
    login_text.pack_forget()
    login_box.pack_forget()
    password_text.pack_forget()
    password_box.pack_forget()
    
    
    username_list.append(username)
    password_list.append(password)  # converts contents of file to list form
    if debugq==1:
        print(username_list)
        print(password_list)
    username_write=open("logins.txt","w")
    password_write=open("passwords.txt","w")
    username_list=str(username_list)
    password_list=str(password_list)            #adds items to the lists
    username_write.write(username_list)
    password_write.write(password_list)
    username_write.close()
    password_write.close()                      #closes file
    newaccountset.pack_forget()
    newaccountsuccesstext=Label(start,text="New account created",bg="#0099FF")
    newaccountsuccesslogin=Button(start,text="Login",command=restart,bg="#0099FF")
    newaccountsuccesstext.pack()
    newaccountsuccesslogin.pack()

#prepares for a restart
def restart():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    newaccountsuccesstext.pack_forget()
    newaccountsuccesslogin.pack_forget()
    begin()

#operates after a successful login 
def success():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    login_text.pack_forget()
    login_box.pack_forget()
    password_text.pack_forget()
    password_box.pack_forget()
    login_button.pack_forget()
    newaccountbutton.pack_forget()
    success_text=Label(start,text="Login success",bg="#0099FF")
    success_text.pack()
    ex=Button(start,text="quit",command=end,bg="#0099FF")
    ex.pack()


def end():
    global username_list,newaccountset,password_list,position,username,password,f,mf,m,login_box,password_box,data,login_text,login_box,password_text,password_box,login_button,newaccountbutton,newaccountsuccesslogin,newaccountsuccesstext,filep,datap,newerror,symbol,capital,number,lower,newaccountsuccesstext,newaccountsuccesslogin,debugq,debug,restart
    quit() #quits
debug=Button(start,text="debug",command=debug,bg="#0099FF")
#debug.pack()


begin()



