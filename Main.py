import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
email = "sahkoposti"
password = "salasana"

def loginToGreeting():
    email = ent_email.get()
    password = ent_pw.get()
    if email == "Oppilas@email.com" and password == "asd":
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

def mainToProfile():
    frm_main.pack_forget()
    frm_profile.pack()

def homeworkToProfile():
    frm_homework.pack_forget()
    frm_profile.pack()

def homeworkToMain():
    frm_homework.pack_forget()
    frm_main.pack()

def profileToMain():
    frm_profile.pack_forget()
    frm_main.pack()

def profileToLogin():
    frm_profile.pack_forget()
    frm_login.pack()

def labelChange(studentName):
    lbl_speachBubble.configure(text="Hei " + studentName.split('@')[0] + "!")
    lbl_name.configure(text=studentName.split('@')[0] + "\nKoulu")
    lbl_nameHomework.configure(text=studentName.split('@')[0] + "\nKoulu")
    lbl_nameProfile.configure(text=studentName.split('@')[0] + "\nKoulu")


#Init Tkinter
root = tk.Tk()
root.title("Koulu appi")
root.wm_geometry("360x640")

#Login frame
frm_login = ttk.Frame(root)
frm_login.columnconfigure(0, weight=1)
lbl_cat = tk.Label(frm_login, text="😺", font=("Courier", 200))
lbl_email = ttk.Label(frm_login, text="Sähköposti", font=('Lato', 15))
ent_email = ttk.Entry(frm_login, font=('Lato', 15), textvariable=email, width=50)
frm_empty = ttk.Frame(frm_login, height=25)
lbl_pw = ttk.Label(frm_login, text="Salasana", font=('Lato', 15))
ent_pw = ttk.Entry(frm_login, font=('Lato', 15), textvariable=password, show="*", width=50)
btn_ok = ttk.Button(frm_login, width=8, text="Ok", style=ttk.Style().configure('TButton', font=('Lato', 15)), command=loginToGreeting)
lbl_error = ttk.Label(frm_login, text="Sähköposti tai salasana on väärin.", font=('Lato', 10), foreground="red")

lbl_cat.grid(row=0, column=0, sticky="ew")
lbl_email.grid(row=1, column=0, sticky="w", padx=40)
ent_email.grid(row=2, column=0, padx=40)
frm_empty.grid(row=3, column=0)
lbl_pw.grid(row=4, column=0, sticky="w", padx=40)
ent_pw.grid(row=5, column=0, padx=40)
btn_ok.grid(row=6, column=0, pady=30)

#Greeting frame
frm_greeting = ttk.Frame(root)
img_speachBubble = tk.PhotoImage(file="pictures/speachBubble.png")
lbl_speachBubble = ttk.Label(frm_greeting, text=email, font=('Lato', 15), image=img_speachBubble, compound='center')
lbl_cat = ttk.Label(frm_greeting, text="😺", font=("Courier",200))
lbl_greeting = ttk.Label(frm_greeting, text="Sinulla on 27 uutta läksyä", font=('Lato', 15))

frm_buttons = ttk.Frame(frm_greeting)
btn_back = ttk.Button(frm_buttons, width=8, text="Takaisin", style=ttk.Style().configure('TButton', font=('Lato', 15)), command=greetingToLogin)
btn_ok = ttk.Button(frm_buttons, width=8, text="Ok", style=ttk.Style().configure('TButton', font=('Lato', 15)), command=greetingToMain)

lbl_speachBubble.grid(row=0, column=0)
lbl_cat.grid(row=1, column=0)
lbl_greeting.grid(row=2, column=0)

frm_buttons.grid(row=3, column=0, pady=20)
btn_back.grid(row=0, column=0, padx=5)
btn_ok.grid(row=0, column=1, padx=5)

#Start page
frm_main = ttk.Frame(root)
lbl_name = ttk.Label(frm_main,text="Nimi\nKoulu", font=('Lato', 25))
img_profile = tk.PhotoImage(file="pictures/profile.png")
btn_profile = tk.Button(frm_main, image=img_profile, highlightthickness=0, bd=0, command=mainToProfile)
lbl_laksyt = ttk.Label(frm_main, text="Läksyt", font=('Lato', 25))
lst_laksyt = tk.Listbox(frm_main, height=9, width=15, font=('Lato', 20), relief=tk.SOLID, bd=2)
list_items = ["Matematiikka 1","Matematiikka 2","Matematiikka 3","Englanti 1","Englanti 2","Historia 1","Historia 2","Äidinkieli 1","Äidinkieli 2","Äidinkieli 3","Äidinkieli 4","Kuvataide 1","Kuvataide 2","Uskonto 1","Uskonto 2","Maantieto 1","Maantieto 2","Biologia 1","Biologia 2","Fysiikka 1","Fysiikka 2","Kemia 1","Kemia 2","Ruotsi 1","Ruotsi 2","Ruotsi 3","Liikunta 1"]
for item in list_items:
    lst_laksyt.insert("end", item)
img_arrowUp = tk.PhotoImage(file="pictures/arrowUp.png")
btn_scrollup = tk.Button(frm_main, image=img_arrowUp, highlightthickness=0, bd=0, command=lambda:lst_laksyt.yview_scroll(-1,"units"))
img_arrowDown = tk.PhotoImage(file="pictures/arrowDown.png")
btn_scrolldown =tk.Button(frm_main, image=img_arrowDown, highlightthickness=0, bd=0, command=lambda:lst_laksyt.yview_scroll(1,"units"))
lst_laksyt.bind("<Button-1>", mainToHomework)

frm_buttons = ttk.Frame(frm_main)
frm_buttons.columnconfigure(0, weight=1)
frm_buttons.columnconfigure(1, weight=1)
frm_buttons.columnconfigure(2, weight=1)
img_mail= tk.PhotoImage(file="pictures/mail.png")
btn_mail= tk.Button(frm_buttons, image=img_mail, highlightthickness = 0, bd = 0)
img_schedule =tk.PhotoImage(file="pictures/schedule.png")
btn_schedule= tk.Button(frm_buttons, image=img_schedule, highlightthickness = 0, bd = 0)
img_note =tk.PhotoImage(file="pictures/note.png")
btn_note= tk.Button(frm_buttons, image=img_note, highlightthickness = 0, bd = 0)

lbl_name.grid(row=0, column=0, sticky="NW", pady=20)
btn_profile.grid(row=0, column=1, sticky="NSEW", pady=20)
lbl_laksyt.grid(row=2, column=0, sticky="SW")
lst_laksyt.grid(row=3, column=0)
btn_scrollup.grid(row=3, column=1, sticky="NW", padx=5)
btn_scrolldown.grid(row=3, column=1, sticky="SW", padx=5)

frm_buttons.grid(row=4, column=0, columnspan=2, pady=35, sticky="EW")
btn_mail.grid(row=0, column=0, sticky="W")
btn_schedule.grid(row=0, column=1)
btn_note.grid(row=0,column=2, sticky="E")

## Homework Page

def changeButton():
    btn_palautus.grid_forget()
    btn_file.grid(row=5,column=0, sticky="W")
    btn_camera.grid(row=5,column=0, sticky="E")

def openFile():
    filename = filedialog.askopenfilename()
    btn_file.grid_forget()
    btn_camera.grid_forget()
    lbl_palautettu.grid(row=5)

    
frm_homework = ttk.Frame(root)
lbl_nameHomework = ttk.Label(frm_homework, text="Nimi\nKoulu", font=30)
btn_profile = ttk.Button(frm_homework, text="Profile",command=homeworkToProfile)
lbl_ainelaksyt = ttk.Label(frm_homework, text="LÄKSYT\nAINE", font=30)
txt_ainelaksyt = tk.Text(frm_homework,width=25)
btn_scrollup =ttk.Button(frm_homework, text="^",command=lambda:txt_ainelaksyt.yview_scroll(-1,"units"))
btn_scrolldown =ttk.Button(frm_homework, text="ˇ",command=lambda:txt_ainelaksyt.yview_scroll(1,"units"))
lbl_palautus = ttk.Label(frm_homework,text="Palauta viim. 1.4", font=30)
btn_palautus = ttk.Button(frm_homework, text="palautus", command=changeButton)
btn_file = ttk.Button (frm_homework, text="file",command=openFile)
btn_camera = ttk.Button (frm_homework, text="camera")
lbl_palautettu = ttk.Label(frm_homework,text = "✓ palautettu",background="green",font=30)
btn_returnToMain = ttk.Button(frm_homework,text= "back", command=homeworkToMain)

lbl_nameHomework.grid(row=0,column=0,sticky="NW", pady=20)
btn_profile.grid(row=0, column=1,sticky="NE", pady=20)
lbl_laksyt.grid(row=2,column=0,sticky="SW")
txt_ainelaksyt.grid(row=3,column=0,ipadx=20)
btn_scrollup.grid(row=3,column=1,sticky="N")
btn_scrolldown.grid(row=3,column=1,sticky="S")
lbl_palautus.grid(row=4) 
btn_palautus.grid(row=5)
btn_returnToMain.grid(row=6,sticky="SW")


## Profile Page
frm_profile = ttk.Frame(root)
lbl_nameProfile = ttk.Label(frm_profile, text="Nimi\nKoulu", font=30)
btn_profile = ttk.Button(frm_profile, text="Profile")
lbl_omatTiedot= ttk.Label(frm_profile, text="OMAT TIEDOT", font =40)
lbl_tiedot = ttk.Label(frm_profile,text="Opettaja\nPuhelinnumero\nHuoltaja", font=30)
btn_kuva = ttk.Button(frm_profile,image=img_schedule)
btn_sposti = ttk.Button(frm_profile,text="Sposti")
btn_salasana = ttk.Button(frm_profile,text="Vaihda salasana")
btn_uloskirjautuminen = ttk.Button(frm_profile, text="Kirjaudu ulos", command=profileToLogin)
img_settings = tk.PhotoImage(file="pictures/setting.png")
btn_asetukset = ttk.Button(frm_profile,image=img_settings)
btn_returnToMain = ttk.Button(frm_profile,text="Back", command=profileToMain)

lbl_nameProfile.grid(row=0,column=0,sticky="NW", pady=20)
btn_profile.grid(row=0, column=1,sticky="NE", pady=20)
lbl_omatTiedot.grid(row=1)
btn_kuva.grid(row=2,column=0,sticky="W")
btn_sposti.grid(row=2, column=1,sticky="N")
btn_salasana.grid(row=2,column=1,sticky="S")
btn_uloskirjautuminen.grid(row=3,sticky="W")
lbl_tiedot.grid(row=4,sticky="W")
btn_asetukset.grid(row=5,sticky="W")
btn_returnToMain.grid(row=6,sticky="W")

# Pack the Login page and start
frm_login.pack()

root.mainloop()