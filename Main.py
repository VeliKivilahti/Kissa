import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

def loginToGreeting():
    frm_login.pack_forget()
    frm_greeting.pack()

def greetingToLogin():
    frm_greeting.pack_forget()
    frm_login.pack()

def geetingToMain():
    frm_greeting.pack_forget()
    frm_main.pack()

#Init Tkinter
root = tk.Tk()
root.title("Koulu appi")
root.wm_geometry("360x640")

#Login frame
frm_login = ttk.Frame(root)
lbl_cat = ttk.Label(frm_login, text="😺", font=("Courier",200))
lbl_email = ttk.Label(frm_login, text="Sähköposti")
ent_email = ttk.Entry(frm_login, width=30)
frm_empty = ttk.Frame(frm_login, height=20)
lbl_pw = ttk.Label(frm_login, text="Salasana")
ent_pw = ttk.Entry(frm_login, show="*", width=30)
btn_ok = ttk.Button(frm_login, width=10, text="Ok", command=loginToGreeting)

lbl_cat.grid(row=0, column=0)
lbl_email.grid(row=1, column=0)
ent_email.grid(row=2, column=0)
frm_empty.grid(row=3, column=0)
lbl_pw.grid(row=4, column=0)
ent_pw.grid(row=5, column=0)
btn_ok.grid(row=6, column=0, pady=20)

#Greeting frame
frm_greeting = ttk.Frame(root)
image = Image.open('speachBubble.png')
img_speachBubble = ImageTk.PhotoImage(image)
lbl_speachBubble = ttk.Label(frm_greeting, text="Hei käyttäjä!", font=25, image=img_speachBubble, compound='center')
lbl_cat = ttk.Label(frm_greeting, text="😺", font=("Courier",200))
lbl_geeting = ttk.Label(frm_greeting, text="Sinulla on 0 uutta läksyä")

frm_buttons = ttk.Frame(frm_greeting)
btn_back = ttk.Button(frm_buttons, width=10, text="Takaisin", command=greetingToLogin)
btn_ok = ttk.Button(frm_buttons, width=10, text="Ok", command=geetingToMain)

lbl_speachBubble.grid(row=0, column=0)
lbl_cat.grid(row=1, column=0)
lbl_geeting.grid(row=2, column=0)

frm_buttons.grid(row=3, column=0, pady=20)
btn_back.grid(row=0, column=0, padx=5)
btn_ok.grid(row=0, column=1, padx=5)

#Start page
frm_main = ttk.Frame(root)
lbl_name = ttk.Label(frm_main, text="Nimi\nKoulu", font=30)
btn_profile = ttk.Button(frm_main, width=10, text="Profile")
lbl_laksyt = ttk.Label(frm_main, text="LÄKSYT", font=30)
lst_laksyt = tk.Listbox(frm_main)
list_items = ["matematiikka","englanti","historia","äidinkieli",1,2,3,4,5,6,7,8]
for item in list_items:
    lst_laksyt.insert("end",item)


btn_scrollup =ttk.Button(frm_main,text="^",command=lambda:lst_laksyt.yview_scroll(-1,"units"))
btn_scrolldown =ttk.Button(frm_main,text="ˇ",command=lambda:lst_laksyt.yview_scroll(1,"units"))


lbl_name.grid(row=0,column=0,padx=10)
btn_profile.grid(row=0, column=3,sticky="NE")
lbl_laksyt.grid(row=1,column=1,sticky="SW")
lst_laksyt.grid(row=2,column=1)
btn_scrollup.grid(row=2,column=2,sticky="N")
btn_scrolldown.grid(row=2,column=2,sticky="S")

frm_login.pack()

root.mainloop()
