import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk
from tkinter import PhotoImage
from PIL import Image, ImageTk



import colors


class Main_Page():

    def __init__(self) -> None:
        self.mainpage  = ctk.CTk()
        
        # Title for the main app : 
        self.mainpage.title("Time Forge")

        # Setting up the geometry for the main app and setting the loca(tion to the center of the app  : 
        self.x_location  = (self.mainpage.winfo_screenwidth() //2) - (450)
        self.y_location  = (self.mainpage.winfo_screenheight() //2) - (300)
        print("x Location " + str(self.x_location) + "y Location" + str(self.y_location))
        self.mainpage.geometry(f"900x600+{self.x_location}+{self.y_location}")
        
        # Setting up the theme for the main app  : will make this change later in settings page : 
        self.mainpage._set_appearance_mode("dark")

        # Defining Icon and make the main icon for the app  : 
        # self.icon_image   = ImageTk.PhotoImage(Image.open(r"app_assets\main_icon.png"))
        # self.icon_image = PhotoImage( file="app_assets\main_icon.png")

        self.mainpage.after(201, lambda :self.mainpage.iconbitmap('app_assets\main_icon.ico'))

        # self.mainpage.iconphoto(False , self.icon_image)

        # Calling the main app : 
        self.mainpage.mainloop()




if __name__ == '__main__':
    Main_Page()