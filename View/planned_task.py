import tkinter as tk 
import customtkinter
from tkinter import ttk 
import fonts 
import colors 


class Planned_Task():

    def adding_text(self):
        pass

    def __init__(self , master , width , height   , current_text , current_index) -> None:
        self.master = master
        self.width  = width 
        self.height  = height
        self.current_index  = current_index
        self.current_text = current_text

        # Make the main text box for the main frame 
        self.text  = tk.Text(self.master , height=2, font=fonts.super_small_bold)
        self.text.insert(tk.END , self.current_text)
        self.text.configure(state="disabled")
        self.text.pack(padx=5 , pady=5)
        
        # setting up a temporary button for deleting the currnet task : 
        

        # self.master.configure(background = colors.app_base )
        self.text.configure(background=colors.app_base , foreground=colors.text)


        self.master.mainloop()
    
    def delete_current_instance(self):
        self.text.destroy()
        





if __name__ == '__main__':
    main = Planned_Task(tk.Tk() , 300 ,300 , "I am the one" , 1 )