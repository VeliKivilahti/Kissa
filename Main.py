from afterLogin import AfterLogin
import tkinter as tk 
from login import Login



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)       
        p1 = Login(self)
        p2 = AfterLogin(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)


        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.show()
        p1.show()
        



if __name__ == "__main__":
    window = tk.Tk()
    main =  MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.wm_geometry("300x600")
    
    window.mainloop()