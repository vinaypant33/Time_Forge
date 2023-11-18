import tkinter as tk 

# root = tk.Tk()


# mainbtn = tk.Button(root)

class Styles():

    def button_styles( control  ,  btn_bg ,  btn_fg  ,btn_active_bg ,  btn_active_fg):
        control.configure(background=btn_bg , foreground=btn_fg , activebackground=btn_active_bg , activeforeground=btn_active_fg  , bd= 0 , relief='raised' ) 