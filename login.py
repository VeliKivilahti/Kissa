from page import Page
import tkinter as tk

class Login(Page):
     def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)
        lbl_name=tk.Label(self,text="name")
        lbl_pw=tk.Label(self,text="password")
        namebar=tk.Text(self,width=25,height=1)
        pwbar=tk.Text(self,width=25,height=1)
        btn_ok=tk.Button(self,text="OK",
                            command = self.hide)
        cat=tk.Label(self,text="😺",font=("Courier",64))

        cat.grid(row=0,column=0)
        lbl_name.grid(row=1, column=0)
        namebar.grid(row=2, column=0)
        lbl_pw.grid(row=3, column=0)
        pwbar.grid(row=4, column=0)
        btn_ok.grid(row=5, column=0)
        
        