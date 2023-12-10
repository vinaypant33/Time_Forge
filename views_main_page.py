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
        self.dashboard_image = ImageTk.PhotoImage(Image.open(r"app_assets\home_white.png"))
        self.avatar_image = ImageTk.PhotoImage(Image.open(r"app_assets\avatar.png"))


        self.sidebar = tk.Frame(self.main_page , width=160 , background=colors.sidebar)
        self.sidebar.pack_propagate(0)

        # Image and the username : Frame , Image, username Label : 
        self.user_frame = tk.Frame(self.sidebar , width=150 , height=100  , background=colors.sidebar)
        self.user_image  = tk.Label(self.user_frame , image=self.avatar_image , background=colors.sidebar)
        self.user_name   = tk.Label(self.user_frame , text="Vinay Pant" , background=colors.sidebar , foreground=colors.white_color)

        # golden seperator in the form of frame  : 
        self.first_seperator  = tk.Frame(self.sidebar ,height=1 , background=colors.golden_color)

        # frames for teh images and the text for the names  : 
        self.dashboard_frame  =tk.Frame(self.sidebar , background=colors.sidebar)
        self.dashboard_image_label = tk.Label(self.dashboard_frame , image=self.dashboard_image , background=colors.sidebar)
        self.dashboard_image_text = tk.Label(self.dashboard_frame , text="Dashboard" , background=colors.sidebar , foreground=colors.white_color)




        self.bottom_frame = tk.Frame(self.sidebar , background=colors.golden_color , height=30)


        # packing the controls : 
        self.sidebar.pack(side="left" , fill="y")
        self.user_frame.pack(side="top" , pady=15)

        self.user_image.grid(row=0 , column=0 , padx=10)
        self.user_name.grid(row = 0 , column=1 , padx=10)

        self.first_seperator.pack(side="top" , fill="x" , pady=10)

        self.dashboard_frame.pack()
        self.dashboard_image_label.grid(row = 0 , column=0)
        self.dashboard_image_text.grid(row=0 , column=1)


        self.bottom_frame.pack(side="bottom" , fill="x")
        self.main_page.mainloop()




if __name__ == '__main__':
    main = Main_Page("master" , 100,100)
