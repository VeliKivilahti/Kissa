import tkinter as tk
import tkinter.ttk as ttk
email = "sahkoposti"
password = "salasana"

def loginToGreeting():
    email = ent_email.get()
    password = ent_pw.get()
    if email == "asd@email.com" and password == "asd":
        lbl_error.grid_forget()
        frm_login.pack_forget()
        labelChange(email)
        frm_greeting.pack()
    else:
        lbl_error.grid(row=7, column=0)

def greetingToLogin():
    frm_greeting.pack_forget()
    frm_login.pack()

def greetingToMain():
    frm_greeting.pack_forget()
    frm_main.pack()

def mainToHomework(*args):
    frm_main.pack_forget()
    frm_homework.pack()

def labelChange(studentName):
    lbl_speachBubble.configure(text="Hei " + studentName.split('@')[0] + "!")
    lbl_name.configure(text=studentName.split('@')[0] + "\nKoulu")


#Init Tkinter
root = tk.Tk()
root.title("Koulu appi")
root.wm_geometry("360x640")

#Login frame
frm_login = ttk.Frame(root)
lbl_cat = ttk.Label(frm_login, text="😺", font=("Courier",200))
lbl_email = ttk.Label(frm_login, text="Sähköposti")
ent_email = ttk.Entry(frm_login, textvariable=email, width=30)
frm_empty = ttk.Frame(frm_login, height=20)
lbl_pw = ttk.Label(frm_login, text="Salasana")
ent_pw = ttk.Entry(frm_login, textvariable=password, show="*", width=30)
btn_ok = ttk.Button(frm_login, width=10, text="Ok", command=loginToGreeting)
lbl_error = ttk.Label(frm_login, text="Sähköposti tai salasana on väärin.", foreground="red")

lbl_cat.grid(row=0, column=0)
lbl_email.grid(row=1, column=0, padx=50, sticky="w")
ent_email.grid(row=2, column=0)
frm_empty.grid(row=3, column=0)
lbl_pw.grid(row=4, column=0, padx=50, sticky="w")
ent_pw.grid(row=5, column=0)
btn_ok.grid(row=6, column=0, pady=20)

#Greeting frame
frm_greeting = ttk.Frame(root)
img_speachBubble = tk.PhotoImage(file="pictures/speachBubble.png")
lbl_speachBubble = ttk.Label(frm_greeting, text=email, font=25, image=img_speachBubble, compound='center')
lbl_cat = ttk.Label(frm_greeting, text="😺", font=("Courier",200))
lbl_greeting = ttk.Label(frm_greeting, text="Sinulla on 0 uutta läksyä")

frm_buttons = ttk.Frame(frm_greeting)
btn_back = ttk.Button(frm_buttons, width=10, text="Takaisin", command=greetingToLogin)
btn_ok = ttk.Button(frm_buttons, width=10, text="Ok", command=greetingToMain)

lbl_speachBubble.grid(row=0, column=0)
lbl_cat.grid(row=1, column=0)
lbl_greeting.grid(row=2, column=0)

frm_buttons.grid(row=3, column=0, pady=20)
btn_back.grid(row=0, column=0, padx=5)
btn_ok.grid(row=0, column=1, padx=5)

#Start page
frm_main = ttk.Frame(root)
lbl_name = ttk.Label(frm_main, text="Nimi\nKoulu", font=30)
btn_profile = ttk.Button(frm_main, text="Profile")
lbl_laksyt = ttk.Label(frm_main, text="LÄKSYT", font=30)
lst_laksyt = tk.Listbox(frm_main, font=30)
list_items = ["Matematiikka","Englanti","Historia","Äidinkieli","Kuvataide","Uskonto","Maantieto","Biologia","Fysiikka","Kemia","Ruotsi","Liikunta"]
for item in list_items:
    lst_laksyt.insert("end", item)
btn_scrollup =ttk.Button(frm_main, text="^",command=lambda:lst_laksyt.yview_scroll(-1,"units"))
btn_scrolldown =ttk.Button(frm_main, text="ˇ",command=lambda:lst_laksyt.yview_scroll(1,"units"))
lst_laksyt.bind("<Double-Button-1>", mainToHomework)

frm_buttons = ttk.Frame(frm_main)
frm_buttons.columnconfigure(0, weight=1)
frm_buttons.columnconfigure(1, weight=1)
frm_buttons.columnconfigure(2, weight=1)
img_mail= tk.PhotoImage(file="pictures/mail.png")
btn_mail= tk.Button(frm_buttons,image=img_mail,highlightthickness = 0, bd = 0)
img_schedule =tk.PhotoImage(file="pictures/schedule.png")
btn_schedule= tk.Button(frm_buttons,image=img_schedule,highlightthickness = 0, bd = 0)
img_note =tk.PhotoImage(file="pictures/note.png")
btn_note= tk.Button(frm_buttons,image=img_note,highlightthickness = 0, bd = 0)

lbl_name.grid(row=0,column=0,sticky="NW", pady=20)
btn_profile.grid(row=0, column=1,sticky="NE", pady=20)
lbl_laksyt.grid(row=2,column=0,sticky="SW")
lst_laksyt.grid(row=3,column=0,ipadx=20)
btn_scrollup.grid(row=3,column=1,sticky="N")
btn_scrolldown.grid(row=3,column=1,sticky="S")

frm_buttons.grid(row=4, column=0, columnspan=2, pady=25, sticky="EW")
btn_mail.grid(row=0,column=0, sticky="W")
btn_schedule.grid(row=0,column=1)
btn_note.grid(row=0,column=2, sticky="E")

## Homework Page

frm_homework = ttk.Frame(root)
lbl_name = ttk.Label(frm_homework, text="Nimi\nKoulu", font=30)
btn_profile = ttk.Button(frm_homework, text="Profile")
lbl_ainelaksyt = ttk.Label(frm_homework, text="LÄKSYT\nAINE", font=30)
lst_ainelaksyt = tk.Listbox(frm_homework, font=30)
list_homework = ["Laksy1","Laksy2","Laksy3","Laksy4","Laksy5","Laksy6","Laksy7"]
for item in list_homework:
    lst_ainelaksyt.insert("end", item)
btn_scrollup =ttk.Button(frm_homework, text="^",command=lambda:lst_ainelaksyt.yview_scroll(-1,"units"))
btn_scrolldown =ttk.Button(frm_homework, text="ˇ",command=lambda:lst_ainelaksyt.yview_scroll(1,"units"))

#frm_buttons = ttk.Frame(frm_homework)
#frm_buttons.columnconfigure(0, weight=1)
#frm_buttons.columnconfigure(1, weight=1)
#frm_buttons.columnconfigure(2, weight=1)
#img_mail= tk.PhotoImage(file="pictures/mail.png")
#btn_mail= tk.Button(frm_buttons,image=img_mail,highlightthickness = 0, bd = 0)
#img_schedule =tk.PhotoImage(file="pictures/schedule.png")
#btn_schedule= tk.Button(frm_buttons,image=img_schedule,highlightthickness = 0, bd = 0)
#img_note =tk.PhotoImage(file="pictures/note.png")
#btn_note= tk.Button(frm_buttons,image=img_note,highlightthickness = 0, bd = 0)

lbl_name.grid(row=0,column=0,sticky="NW", pady=20)
btn_profile.grid(row=0, column=1,sticky="NE", pady=20)
lbl_laksyt.grid(row=2,column=0,sticky="SW")
lst_ainelaksyt.grid(row=3,column=0,ipadx=20)
btn_scrollup.grid(row=3,column=1,sticky="N")
btn_scrolldown.grid(row=3,column=1,sticky="S")

#frm_buttons.grid(row=4, column=0, columnspan=2, pady=25, sticky="EW")
#btn_mail.grid(row=0,column=0, sticky="W")
#btn_schedule.grid(row=0,column=1)
#btn_note.grid(row=0,column=2, sticky="E")


# Pack the Login page and start
frm_login.pack()

root.mainloop()
