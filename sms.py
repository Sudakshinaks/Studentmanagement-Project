from tkinter import *
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pymysql
#functionality part

def add_student():

    def add_data():
         
         if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_window)

         else:
            mydb=mysql.connector.connect(host='localhost', user='root', password='sudakshinaks@21',database='studentmanagementSystem')    
            mycursor=mydb.cursor()
            currentdate=time.strftime('%d/%m/%Y')
            currenttime=time.strftime('%H:%M:%S')
            Query='Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(Query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),currentdate,currenttime))
            
            
            result=messagebox.askyesno('confirm','Data added successfully.Do you want to clean the form?')
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
                


    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)
    idLable=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLable.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=10,pady=15)


    nameLable=Label(add_window,text='Name',font=('times new roman',20,'bold'))
    nameLable.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)


    phoneLable=Label(add_window,text='Mobile No',font=('times new roman',20,'bold'))
    phoneLable.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=10,pady=15)

    emailLable=Label(add_window,text='Email',font=('times new roman',20,'bold'))
    emailLable.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=10,pady=15)

    addressLable=Label(add_window,text='Address',font=('times new roman',20,'bold'))
    addressLable.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,padx=10,pady=15)

    genderLable=Label(add_window,text='Gender',font=('times new roman',20,'bold'))
    genderLable.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=10,pady=15)

    dobLable=Label(add_window,text='D.O.B',font=('times new roman',20,'bold'))
    dobLable.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,padx=10,pady=15)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)



def connect_database():

    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(hostEntry.get()=='' or  userEntry.get()=='' or passwordEntry.get()=='')
            mycursor=con.cursor()
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            
            
        except:
            hostEntry.get()=='localhost'and userEntry.get()=='root' and passwordEntry.get()=='1234'
            messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
            connectWindow.destroy()
            
            addstudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            deletstudentButton.config(state=NORMAL)
            updatestudentButton.config(state=NORMAL)
            showstudentButton.config(state=NORMAL)
            exportstudentButton.config(state=NORMAL)
            exitButton.config(state=NORMAL)
            return
        mydb=mysql.connector.connect(host='localhost', user='root', password='sudakshinaks@21')    
        mycursor=mydb.cursor()

        

        try:
           query='create database studentmanagementSystem'
           mycursor.execute(query)
           query='use studentmanagementSystem'
           mycursor.execute(query)
           query='create table student(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30),'\
            'address varchar(100), gender varchar(30), dob varchar(20), date varchar(50), time varchar(50))'
           mycursor.execute(query)

        except:
            query='use studentmanagementSystem'
            mycursor.execute(query)
        
          
    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'),)
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    
    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'),)
    usernameLabel.grid(row=1,column=0,padx=20)

    userEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'),)
    passwordLabel.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)


    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''

def slider():
    global text,count

    if count==len(s):
        count=0
        text=''

    text=text+s[count] #S
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)
 

    




def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)


#GUI part

root=ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')

root.title('Student Management System')

root.resizable(0,0)

datetimeLabel=Label(root,text='',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)

clock()
s='Student Management System'  #s[count]=S when count value is 0
sliderLabel=Label(root,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)

slider()

connectButton=ttk.Button(root,text='Connect to Database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root,bg='')
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED)
searchstudentButton.grid(row=2,column=0,pady=20)

deletstudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED)
deletstudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,state=DISABLED)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)


studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                                 xscrollcommand=scrollBarX.set,
                                 yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)


studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')


studentTable.config(show='headings')
root.mainloop()