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


        """ Main Code from here : Basic Repeated Controls : Sidebar : Bottombar : Username Icon and Image in Sidebar"""
        self.sidebar  = tk.Frame(self.mainpage , width =330 , background=colors.white_color)
        self.sidebar.pack_propagate(0)
        # Setting upnthe controls in sidebar : Sequence : userIcon : Image : Username : line : in the form of frame : then scrollbar type frame: 

        # Usericon Avater : Will change this later to the main user Image : 
        self.user_avater  = ImageTk.PhotoImage(Image.open(r"app_assets\avatar.png"))
        self.user_avater_label  = tk.Label(self.sidebar , image=self.user_avater)
        self.username_label  = tk.Label(self.sidebar , text="Username Vinay Pant")

        # Adding scrollable sidebar : It will have all the buttons for home and  other projects based data  : 
        self.sidebar_content_scrollbar  = ctk.CTkScrollableFrame(self.sidebar , bg_color=colors.black_color)

        '''Packing the  controls : Each control is to be packed sequentially : '''
        self.sidebar.pack(side="left" , fill='y')
        self.user_avater_label.pack(side="top" , pady=10)
        self.username_label.pack(side="top")
        self.sidebar_content_scrollbar.pack(pady=10)
        # Calling the main app : 
        self.mainpage.mainloop()




if __name__ == '__main__':
    Main_Page()