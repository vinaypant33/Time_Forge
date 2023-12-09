import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as tbs


import colors



class Main_Page():

    def __init__(self , master , height  , width ) -> None:
        self.main_page   = ctk.CTk()
        
        # setting app height and width  : 
        self.main_page.geometry("900x600")
        self.main_page.title("Time Forge")

        # Setting the theme for the aplication  : 
        ctk.set_appearance_mode("light")
        self.main_page.configure(background  = colors.app_base)

        ##### Setting up controls for the main dashboard : Fixed controls  : 
        # sidebar
        self.sidebar = tk.Frame(self.main_page , height=900 , width=150 , background=colors.sidebar)
        self.sidebar.pack_propagate(0)
        




        ##### Packing the controls : 
        self.sidebar.pack(side="left" , fill="y")


        # Caling the main app : 
        self.main_page.mainloop()




if __name__ == '__main__':
    main = Main_Page("master" , 100,100)
