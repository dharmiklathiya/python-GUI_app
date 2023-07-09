# Starter Code

import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title('GUI')







# creat Lable...
name_lable = ttk.Label(win, text= 'Enter You Name :')
name_lable.grid(row = 0, column=0, sticky=tk.W)

email_lable = ttk.Label(win, text='Enter Your Email :')
email_lable.grid(row=1,column=0,sticky=tk.W )

age_lable = ttk.Label(win, text='Enter Your Age :')
age_lable.grid(row=2,column=0,sticky=tk.W)

gender_lable = ttk.Label(win,text='Select Your Gender ')
gender_lable.grid(row=3,column=0)

# creat entry tex.....
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=16, textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = tk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var = tk.StringVar()
age_entrybox = tk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

# creat Commbobox..
gender_var = tk.StringVar()
gender_Commbobox = ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_Commbobox['values'] = ('Male','Female','other')
gender_Commbobox.current('0')
gender_Commbobox.grid(row=3,column=1)

# creat Radio Button...
usertype_var = tk.StringVar()
raddiobtn1 = ttk.Radiobutton(win,text='Student',value='Student', variable= usertype_var)
raddiobtn1.grid(row=4 , column=0)

raddiobtn2 = ttk.Radiobutton(win,text='Teacher',value='teacher',variable=usertype_var)
raddiobtn2.grid(row=4,column=1)

# creat Check Box...
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text='Check if you want subscribe our newslatter',variable= checkbtn_var)
checkbtn.grid(row=5,columnspan=3)

# Creat Submit Button...

# def action():
#     username = name_var.get()
#     user_email = email_var.get()
#     userage = age_var.get()
#     print(f'{username} is {userage} years old and email is {user_email}')
#     user_gender = gender_var.get()
#     usertype = usertype_var.get()
#     if checkbtn_var.get() == 0:
#         subscribed = 'NO'
#     else:
#         subscribed = 'YES'
#     print(f'{user_gender} is {usertype} and {subscribed}')

#     with open('file.txt','a') as f:
#         f.write(f'{username},{userage},{user_email},{user_gender},{usertype},{subscribed}')
    
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0, tk.END)

# # creat lable color...  
#     name_lable.configure(foreground='Blue')


# Write to CSV...

def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype_var.get()
    if checkbtn_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'
    
    #write csv file
    with open('file.csv','a',newline='') as f:
        dict_writer = DictWriter(f, fieldnames= ['UserName','User Age','User Email Address','User Gender','User Types','Subscribed' ])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'UserName':username,
            'User Age':userage,
            'User Email Address':user_email,
            'User Gender':user_gender,
            'User Types' : user_type,
            'Subscribed' : subscribed
        })

    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0, tk.END)
   
submit_button = tk.Button(win,text='Submit',command= action)
submit_button.grid(row=6,column=0)

win.mainloop()