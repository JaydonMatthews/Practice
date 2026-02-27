from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import sqlite3

root = Tk()

root.title("Ski")

root.geometry('1920x1080')


def Home():
    pagetitle = "Home"
    page_title = Label(root, text = pagetitle, borderwidth=2, font = Sub_header, relief = "groove", background = "grey66")
    page_title.grid(row = 1, column = 0, columnspan = 5, sticky = "nsew")
    home_button = Button(root, text = "Home Button", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Home)
    home_button.grid(row = 0, column = 1, sticky = "nsew")

    pagecontent = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""" 
    page_context = Label(root, text = pagecontent, borderwidth=2,font = Text_header, relief = "groove", background = "grey80")
    page_context.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "nsew")

    imagepath = "Other/ski2.jpg"
    imagelarge = Image.open(imagepath)

    resize_image = imagelarge.resize ((400, 350), Image.LANCZOS)
    global imagesmall
    imagesmall = ImageTk.PhotoImage(resize_image)

    box10 = Label(root, image = imagesmall)
    box10.grid(row = 2, column = 3, rowspan = 2, columnspan = 2, sticky = "nsew")


def Bar():
    pagetitle = "Bar"
    page_title = Label(root, text = pagetitle, borderwidth=2, font = Sub_header, relief = "groove", background = "grey66")
    page_title.grid(row = 1, column = 0, columnspan = 5, sticky = "nsew")
    bar_button = Button(root, text = "Bar Button", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Bar)
    bar_button.grid(row = 0, column = 2, sticky = "nsew")

    pagecontent = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""" 
    page_context = Label(root, text = pagecontent, borderwidth=2,font = Text_header, relief = "groove", background = "grey80")
    page_context.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "nsew")
    

    imagepath = "skibar.jpg"
    imagelarge = Image.open(imagepath)

    resize_image = imagelarge.resize ((400, 350), Image.LANCZOS)
    global imagesmall
    imagesmall = ImageTk.PhotoImage(resize_image)

    box10 = Label(root, image = imagesmall)
    box10.grid(row = 2, column = 3, rowspan = 2, columnspan = 2, sticky = "nsew")
    

def Kitchen():
    pagetitle = "Kitchen"
    page_title = Label(root, text = pagetitle, borderwidth=2, font = Sub_header, relief = "groove", background = "grey66")
    page_title.grid(row = 1, column = 0, columnspan = 5, sticky = "nsew")
    kitchen_button = Button(root, text = "Kitchen Button", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Kitchen)
    kitchen_button.grid(row = 0, column  = 3, sticky = "nsew")

    pagecontent = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""" 
    page_context = Label(root, text = pagecontent, borderwidth=2,font = Text_header, relief = "groove", background = "grey80")
    page_context.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "nsew")

    imagepath = "skikit.jpg"
    imagelarge = Image.open(imagepath)

    resize_image = imagelarge.resize ((400, 350), Image.LANCZOS)
    global imagesmall
    imagesmall = ImageTk.PhotoImage(resize_image)

    box10 = Label(root, image = imagesmall)
    box10.grid(row = 2, column = 3, rowspan = 2, columnspan = 2, sticky = "nsew")

def Lessons():
    pagetitle = "Lessons"
    page_title = Label(root, text = pagetitle, borderwidth=2, font = Sub_header, relief = "groove", background = "grey66")
    page_title.grid(row = 1, column = 0, columnspan = 5, sticky = "nsew")
    lessons = Button(root, text = "Lessons", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Lessons)
    lessons.grid(row = 0, column = 4, sticky = "nsew")

    pagecontent = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""" 
    page_context = Label(root, text = pagecontent, borderwidth=2,font = Text_header, relief = "groove", background = "grey80")
    page_context.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "nsew")

    imagepath = "skilessson.jpg"
    imagelarge = Image.open(imagepath)

    resize_image = imagelarge.resize ((400, 350), Image.LANCZOS)
    global imagesmall
    imagesmall = ImageTk.PhotoImage(resize_image)

    box10 = Label(root, image = imagesmall)
    box10.grid(row = 2, column = 3, rowspan = 2, columnspan = 2, sticky = "nsew")


def Policy():
    policy = Toplevel()
    policy.geometry('300x300+400+0')
    policy.title = "Policy"
    policycontent = """These are lots of super interesting bits of policy information that no-one will read"""
    policylabel = Label(policy, text = policycontent)
    policylabel.pack()

def Terms_Conditions():
    t_and_c = Toplevel()
    t_and_c.geometry('300x300+400+0')
    t_and_c.title = "Terms and Conditions"
    t_and_ccontent = """These are lots of super interesting bits of terms and conditions information that no-one will read"""
    t_and_clabel = Label(t_and_c, text = t_and_ccontent)
    t_and_clabel.pack()

def Accessibility():
    accessibility2 = Toplevel()
    accessibility2.geometry('300x300+400+0')
    accessibility2.title = "Accessibility2"
    accessibility2content = """These are lots of super interesting bits of accessibility information that no-one will read"""
    accessibility2label = Label(accessibility2, text = accessibility2content)
    accessibility2label.pack()

def Contact():
    global contact
    contact = Toplevel()
    contact.geometry('600x400+400+0')
    contact.title = "Contact Us"


    titlebox = Label(contact, text = "Contact Us")
    namelabel = Label(contact, text = "Name")
    global nameentry
    nameentry = Entry(contact, width = 50, bg = "white", fg = "black")
    emaillabel = Label(contact, text = "Email")
    global emailentry
    emailentry = Entry(contact, width = 50, bg = "white", fg = "black")
    messagelabel = Label(contact, text = "Message")
    global messageentry
    messageentry = Entry(contact, width = 50, bg = "white", fg = "black")
    submitbutton = Button(contact, text = "Submit", bd = 5, command = ContactSubmit)
    
    

    contact.columnconfigure(0, weight = 1)
    contact.columnconfigure(1, weight = 10)
    contact.rowconfigure((0,1,2,3,4), weight = 1)

    titlebox.grid(row = 0, column = 0)
    namelabel.grid(row = 1, column = 0)
    nameentry.grid(row = 1, column = 1)
    emaillabel.grid(row = 2, column = 0)
    emailentry.grid(row = 2, column = 1)
    messagelabel.grid(row = 3, column = 0)
    messageentry.grid(row = 3, column = 1)
    submitbutton.grid(row = 4, column = 0)

def ContactSubmit():
    global nameentry
    global emailentry
    global messageentry

    global name
    name = nameentry.get()
    global email
    email = emailentry.get()
    global message
    message = messageentry.get()

    print(name)
    print(email)
    print(message)

    data = (name, email, message)
    con = sqlite3.connect('Database.db')
    cur = con.cursor()
    cur.execute('INSERT INTO contactInfo VALUES (?, ?, ?)', data)
    con.commit()

    contact.destroy() 


    


def home():
    pass



Main_header = tkFont.Font(family="Arial", size = 20, weight = tkFont.NORMAL)
Sub_header = tkFont.Font(family="Arial", size = 15, weight = tkFont.NORMAL)
Text_header = tkFont.Font(family="Arial", size = 12, weight = tkFont.NORMAL)

logo = Label(root, text = "Logo", borderwidth=2, font = Main_header, relief = "groove", background = "grey")
home_button = Button(root, text = "Home Button", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Home)
bar_button = Button(root, text = "Bar Button", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Bar)
kitchen_button = Button(root, text = "Kitchen Button", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Kitchen)
lessons = Button(root, text = "Lessons", borderwidth=2, font = Main_header, relief = "groove", background = "grey", command = Lessons)
page_title = Label(root, text = "Page Title", borderwidth=2, font = Sub_header, relief = "groove", background = "grey66")
page_context = Label(root, text = "Page Context", borderwidth=2,font = Text_header, relief = "groove", background = "grey80")
policy = Button(root, text = "Policy", borderwidth=2, font = Text_header, relief = "groove", background = "grey", command = Policy)
terms_conditions = Button(root, text = "Terms and Conditions", borderwidth=2, font = Text_header, relief = "groove", background = "grey", command = Terms_Conditions)
box10 = Label(root, text = "box10", borderwidth=2, font = Text_header, relief = "groove", background = "grey")
accessibility = Button(root, text = "Accessibility", borderwidth=2, font = Text_header, relief = "groove", background = "grey", command = Accessibility)
contact_us = Button(root, text = "Contact us", borderwidth=2, font = Text_header, relief = "groove", background = "grey", command = Contact)
home = Button(root, text = "Home", borderwidth=2, font = Text_header, relief = "groove", background = "grey", command = home)

imagepath = "Other/ski.jpg"
imagelarge = Image.open(imagepath)

resize_image = imagelarge.resize ((400, 350), Image.LANCZOS)
imagesmall = ImageTk.PhotoImage(resize_image)

box10 = Label(root, image = imagesmall)
box10.grid(row = 2, column = 3, rowspan = 2, columnspan = 2, sticky = "nsew")

#print(tkFont.families(root=None, displayof=None))

logo.grid()
home_button.grid()
bar_button.grid()
kitchen_button.grid()
lessons.grid()

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 1)
root.columnconfigure(4, weight = 1)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)
root.rowconfigure(4, weight = 1)

logo.grid(row = 0, column = 0, sticky = "nsew")
home_button.grid(row = 0, column = 1, sticky = "nsew")
bar_button.grid(row = 0, column = 2, sticky = "nsew")
kitchen_button.grid(row = 0, column  = 3, sticky = "nsew")
lessons.grid(row = 0, column = 4, sticky = "nsew")
page_title.grid(row = 1, column = 0, columnspan = 5, sticky = "nsew")
page_context.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "nsew")
policy.grid(row = 4, column = 0, sticky = "nsew")
terms_conditions.grid(row = 4, column = 1, sticky = "nsew")
box10.grid(row = 2, column = 3, rowspan = 2, columnspan = 2, sticky = "nsew")
contact_us.grid(row = 4, column = 3, sticky = "nsew")
home.grid(row = 4, column = 4, sticky = "nsew")
accessibility.grid(row = 4, column = 2, sticky = "nsew")



root.mainloop()

