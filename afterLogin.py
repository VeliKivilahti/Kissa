from page import Page
import tkinter as tk

class AfterLogin(Page):
     def __init__(self, *args, **kwargs):
        
        Page.__init__(self, *args, **kwargs)
        lbl_name=tk.Label(self,text="😺",font=("Courier",128))
        lbl_name.grid(row=0,column=0)
