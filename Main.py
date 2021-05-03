import tkinter as tk 

def loginToSecond():
    login.pack_forget()
    nextFrame.pack()

def secondToLogin():
    nextFrame.pack_forget()
    login.pack()
#Init Tkinter
root = tk.Tk()

#Login frame
login = tk.Frame(root)
lbl_name=tk.Label(login,text="name")
lbl_pw=tk.Label(login,text="password")
namebar=tk.Text(login,width=25,height=1)
pwbar=tk.Text(login,width=25,height=1)
btn_ok=tk.Button(login,text="OK",
                command= loginToSecond)
cat=tk.Label(login,text="😺",font=("Courier",64))

cat.grid(row=0,column=0)
lbl_name.grid(row=1, column=0)
namebar.grid(row=2, column=0)
lbl_pw.grid(row=3, column=0)
pwbar.grid(row=4, column=0)
btn_ok.grid(row=5, column=0)

#Second frame
nextFrame =tk.Frame(root)
kissa2=tk.Label(nextFrame,text="😺",font=("Courier",200))
btn_back=tk.Button(nextFrame,text="back",command=secondToLogin)

kissa2.grid(row=0,column=0)
btn_back.grid(row=1,column=0)

login.pack()





root.mainloop()
