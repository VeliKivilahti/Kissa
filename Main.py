import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
email = "sahkoposti"
password = "salasana"
palautetut = []

def loginToGreeting(): 
    email = ent_email.get()
    password = ent_pw.get()
    if email == "a" and password == "a":
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

def mainToHomework(event):
    currentHomework = str(lst_laksyt.get(lst_laksyt.curselection()))
    lbl_ainelaksyt.configure(text=currentHomework)
    frm_main.pack_forget()
    frm_homework.pack()
    if (currentHomework in palautetut):## Inserts "Palautettu" if homework already is returned 
        btn_palautus.grid_forget()
        lbl_palautettu.grid(row=5,sticky="NSWE")
    
        

def mainToProfile():
    frm_main.pack_forget()
    frm_profile.pack()

def homeworkToProfile():
    lbl_palautettu.grid_forget() #Resets the view back to original
    frm_palautusPopUp.grid_forget()
    btn_palautus.grid(row=5)
    frm_homework.pack_forget()
    frm_profile.pack()

def homeworkToMain():
    lbl_palautettu.grid_forget() #Resets the view back to original
    frm_palautusPopUp.grid_forget()
    btn_palautus.grid(row=5)
    frm_homework.pack_forget()
    frm_main.pack()

def profileToMain():
    frm_profile.pack_forget()
    frm_main.pack()

def profileToLogin():
    frm_profile.pack_forget()
    frm_login.pack()

def labelChange(studentName): # Changes labels to have student's name in the different pages
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
frm_empty = ttk.Frame(frm_greeting, height=40)
img_speachBubble = tk.PhotoImage(file="pictures/speachBubble.png")
lbl_speachBubble = ttk.Label(frm_greeting, text=email, font=('Lato', 15), image=img_speachBubble, compound='center')
lbl_cat = ttk.Label(frm_greeting, text="😺", font=("Courier",200))
lbl_greeting = ttk.Label(frm_greeting, text="Sinulla on 27 uutta läksyä", font=('Lato', 15))
frm_buttons = ttk.Frame(frm_greeting)
btn_back = ttk.Button(frm_buttons, width=8, text="Takaisin", style=ttk.Style().configure('TButton', font=('Lato', 15)), command=greetingToLogin)
btn_ok = ttk.Button(frm_buttons, width=8, text="Ok", style=ttk.Style().configure('TButton', font=('Lato', 15)), command=greetingToMain)

frm_empty.grid(row=0)
lbl_speachBubble.grid(row=1, column=0)
lbl_cat.grid(row=2, column=0)
lbl_greeting.grid(row=3, column=0)
frm_buttons.grid(row=4, column=0, pady=20)
btn_back.grid(row=0, column=0, padx=5)
btn_ok.grid(row=0, column=1, padx=5)


#Start page
frm_main = ttk.Frame(root)
lbl_name = ttk.Label(frm_main,text="Nimi\nKoulu", font=('Lato', 25))
img_profile = tk.PhotoImage(file="pictures/profile.png")
btn_profile = tk.Button(frm_main, image=img_profile, highlightthickness=0, bd=0, command=mainToProfile)
lbl_laksyt = ttk.Label(frm_main, text="Läksyt", font=('Lato', 25))
lst_laksyt = tk.Listbox(frm_main, height=9, width=15, font=('Lato', 20), relief=tk.SOLID, bd=1.5)
list_items = ["Matematiikka 1","Matematiikka 2","Matematiikka 3","Englanti 1","Englanti 2","Historia 1","Historia 2","Äidinkieli 1","Äidinkieli 2","Äidinkieli 3","Äidinkieli 4","Kuvataide 1","Kuvataide 2","Uskonto 1","Uskonto 2","Maantieto 1","Maantieto 2","Biologia 1","Biologia 2","Fysiikka 1","Fysiikka 2","Kemia 1","Kemia 2","Ruotsi 1","Ruotsi 2","Ruotsi 3","Liikunta 1"]
for item in list_items:
    lst_laksyt.insert("end", item) # Initialize an list of homeworks
img_arrowUp = tk.PhotoImage(file="pictures/arrowUp.png")
btn_scrollup = tk.Button(frm_main, image=img_arrowUp, highlightthickness=0, bd=0, command=lambda:lst_laksyt.yview_scroll(-1,"units"))
img_arrowDown = tk.PhotoImage(file="pictures/arrowDown.png")
btn_scrolldown =tk.Button(frm_main, image=img_arrowDown, highlightthickness=0, bd=0, command=lambda:lst_laksyt.yview_scroll(1,"units"))
lst_laksyt.bind("<ButtonRelease-1>", mainToHomework) # Clicking the list of homework goes to invidiual homework page

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
 
def changeButton(): # Changes return button to have buttons for file return, camera and return
    btn_palautus.grid_forget()
    frm_palautusPopUp.grid(row=5, sticky="WE", )
    btn_file.grid(row=0,column=0, sticky="SNW", padx=2, pady=2)
    btn_camera.grid(row=0,column=1, sticky="SNEW", padx=2, pady=2)
    btn_cancel.grid(row=0, column=2, sticky="SNE", padx=2, pady=2)

def openFile(): ## Opens a file and marks the homework as done if file has been selected
    filename = filedialog.askopenfilename()
    if filename: # when cancel, it will be ""
        frm_palautusPopUp.grid_forget()
        btn_file.grid_forget()
        btn_camera.grid_forget()
        btn_cancel.grid_forget()
        lbl_palautettu.grid(row=5,sticky="NSWE")
        palautetut.append(lbl_ainelaksyt.cget("text")) ## Marks the homework as done

def cancel(): ## Cancels the homework
    frm_palautusPopUp.grid_forget()
    btn_palautus.grid(row=5)

frm_homework = ttk.Frame(root)
lbl_nameHomework = ttk.Label(frm_homework, text="Nimi\nKoulu", font=('Lato', 25))
btn_profile = tk.Button(frm_homework,image=img_profile, highlightthickness=0, bd=0,command=homeworkToProfile)
lbl_ainelaksyt = ttk.Label(frm_homework, text="Läksyt", font=('Lato', 25))
txt_ainelaksyt = tk.Text(frm_homework,height=9, width=15, font=('Lato', 15), bd=1.5, relief=tk.SOLID)
txt_ainelaksyt.insert("end","Tämä on tehtävänanto oppilaalle.")
txt_ainelaksyt.configure(state="disabled")
btn_scrollup = tk.Button(frm_homework, image=img_arrowUp, highlightthickness=0, bd=0,command=lambda:txt_ainelaksyt.yview_scroll(-1,"units"))
btn_scrolldown =tk.Button(frm_homework, image=img_arrowDown, highlightthickness=0, bd=0,command=lambda:txt_ainelaksyt.yview_scroll(1,"units"))
lbl_palautus = ttk.Label(frm_homework,text="Palauta viim. 1.4", font=('Lato', 18))
img_palautus= tk.PhotoImage(file="pictures/download.png")
btn_palautus = tk.Button(frm_homework, image=img_palautus, highlightthickness = 0, bd = 0, command=changeButton)
frm_palautusPopUp = tk.Frame(frm_homework, background="white", relief=tk.SOLID, bd=1.5)
frm_palautusPopUp.columnconfigure([0, 1, 2], weight=1)
img_file=tk.PhotoImage(file="pictures/file.png")
btn_file = tk.Button (frm_palautusPopUp, image=img_file, background="white", highlightthickness = 0, bd = 0, command=openFile)
img_camera=tk.PhotoImage(file="pictures/camera.png")
btn_camera = tk.Button(frm_palautusPopUp, background="white", highlightthickness = 0, bd = 0, image=img_camera)
img_cancel = tk.PhotoImage(file="pictures/cancel.png")
btn_cancel = tk.Button(frm_palautusPopUp, image=img_cancel, background="white", highlightthickness = 0, bd = 0, command=cancel)
lbl_palautettu = tk.Label(frm_homework,text = "✓ Palautettu", background="green", font=('Lato', 20), relief=tk.SOLID, bd=1.5)
img_back=tk.PhotoImage(file="pictures/back.png")
btn_returnToMain = tk.Button(frm_homework, image=img_back, highlightthickness = 0, bd = 0, command=homeworkToMain)
lbl_nameHomework.grid(row=0,column=0,sticky="NW", pady=20)
btn_profile.grid(row=0, column=1,sticky="NSEW", pady=20)
lbl_ainelaksyt.grid(row=1,column=0,sticky="SW")
txt_ainelaksyt.grid(row=2,column=0,ipadx=20)
btn_scrollup.grid(row=2, column=1, sticky="NW", padx=5)
btn_scrolldown.grid(row=2, column=1, sticky="SW", padx=5)
lbl_palautus.grid(row=4, sticky="W") 
btn_palautus.grid(row=5)
btn_returnToMain.grid(row=6,sticky="SW",pady=30)



## Profile Page
frm_profile = ttk.Frame(root)
lbl_nameProfile = ttk.Label(frm_profile, text="Nimi\nKoulu", font=('Lato', 25))
btn_profile = tk.Button(frm_profile, image=img_profile, highlightthickness=0, bd=0, command=homeworkToProfile)
lbl_omatTiedot= ttk.Label(frm_profile, text="OMAT TIEDOT", font=('Lato', 25))
lbl_tiedot = ttk.Label(frm_profile, text="Opettaja\nPuhelinnumero\nHuoltaja", font=('Lato', 18))
img_profileBigger = tk.PhotoImage(file="pictures/profileBigger.png")
frm_picEmailPassword = ttk.Frame(frm_profile)
frm_picEmailPassword.columnconfigure(0, weight=1)
frm_picEmailPassword.columnconfigure(1, weight=2)
btn_kuva = tk.Button(frm_picEmailPassword, image=img_profileBigger, highlightthickness = 0, bd = 0)
btn_sposti = ttk.Button(frm_picEmailPassword, text="Sähköposti", width=13, style=ttk.Style().configure('TButton', font=('Lato', 18)), state=tk.DISABLED)
btn_salasana = ttk.Button(frm_picEmailPassword, text="Vaihda salasana", width=13, style=ttk.Style().configure('TButton', font=('Lato', 18)), state=tk.DISABLED)
btn_uloskirjautuminen = ttk.Button(frm_profile, text="Kirjaudu ulos", style=ttk.Style().configure('TButton', font=('Lato', 18)), command=profileToLogin)
img_settings = tk.PhotoImage(file="pictures/setting.png")
btn_asetukset = tk.Button(frm_profile, image=img_settings, highlightthickness = 0, bd = 0)
btn_returnToMain = tk.Button(frm_profile, image=img_back, highlightthickness = 0, bd = 0, command=profileToMain)

lbl_nameProfile.grid(row=0, column=0, sticky="NW", pady=20)
btn_profile.grid(row=0, column=1, sticky="E", pady=20)
lbl_omatTiedot.grid(row=1, column=0, columnspan=2, sticky="W")
frm_picEmailPassword.grid(row=2, column=0, columnspan=2, ipadx=2)
btn_kuva.grid(row=0, column=0, rowspan=2)
btn_sposti.grid(row=0, column=1, sticky="NE")
btn_salasana.grid(row=1, column=1, sticky="SE")
btn_uloskirjautuminen.grid(row=3, column=0, sticky="WE", columnspan=2, pady=2)
lbl_tiedot.grid(row=4, column=0, sticky="W", columnspan=2)
btn_asetukset.grid(row=5, column=0, sticky="SNEW", columnspan=2, pady=40)
btn_returnToMain.grid(row=6, sticky="W")

# Pack the Login page and start
frm_login.pack()

root.mainloop()