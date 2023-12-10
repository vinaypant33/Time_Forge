import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as tbs
from PIL import Image ,  ImageTk

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


        # Importing the images for the main controls  : 
        self.dashboard_iamge  = ImageTk.PhotoImage(Image.open(r"app_assets\home_white.png"))
        self.avatar_image = ImageTk.PhotoImage(Image.open(r"app_assets\avatar.png"))


        self.sidebar = tk.Frame(self.main_page , width=150 , background=colors.sidebar)

        # Image and the username : Frame , Image, username Label : 
        self.user_frame = tk.Frame(self.sidebar , width=150 , height=100  , background=colors.sidebar)
        self.user_image  = tk.Label(self.user_frame , image=self.avatar_image , background=colors.sidebar)
        self.user_name   = tk.Label(self.user_frame , text="Vinay Pant" , background=colors.sidebar)





        # packing the controls : 
        self.sidebar.pack(side="left" , fill="y")
        self.user_frame.pack(side="top")

        self.user_image.grid(row=0 , column=0)
        self.user_name.grid(row = 0 , column=1)
        self.main_page.mainloop()




if __name__ == '__main__':
    main = Main_Page("master" , 100,100)
