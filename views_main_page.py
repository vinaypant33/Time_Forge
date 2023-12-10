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



    

        # setting up some universal variables  : 
        self.sidebar_image_size  = (20,20)
        ##### Setting up controls for the main dashboard : Fixed controls  : 
        # sidebar
        self.sidebar = tk.Frame(self.main_page , height=900 , width=160 , background='black')
        self.sidebar.pack_propagate(0)
        self.sidebar.pack(side="left" , fill="y" )


        # # sidebar controls : Logo , buittons with the image : bottom 3 sidebar with the images  :  round button to open and close the sidebar  : 

        # # setting up images for the controls
        self.profile_image  = Image.open(r"app_assets\avatar.png")
        self.profile_image  = ImageTk.PhotoImage(self.profile_image)
        self.black_home  = Image.open(r"app_assets\home_black.png")
        self.black_home  = ImageTk.PhotoImage(self.black_home)
        self.white_home  = Image.open(r"app_assets\home_white.png")
        # self.white_home = ImageTk.PhotoImage(self.white_home)
        self.white_home = ctk.CTkImage(Image.open(r"app_assets\home_white.png") , size=self.sidebar_image_size)
        self.home_light_blue  = Image.open(r"app_assets\home_light_blue.png")
        self.home_light_blue  = ImageTk.PhotoImage(self.home_light_blue)

        self.todo_image  = ctk.CTkImage(Image.open(r"app_assets\todo_white.png") ,size=self.sidebar_image_size)
        self.timesheet_image  = ctk.CTkImage(Image.open(r"app_assets\timesheet_white.png") , size=self.sidebar_image_size)



        self.image_label = tk.Label(self.sidebar , image=self.profile_image , background=colors.sidebar)
        self.profile_name  = tk.Label(self.sidebar , text="Vinay Pant" , background=colors.sidebar , foreground=colors.app_base)
        
        # seperator for the sidebar before the buttons and other controls  : 
        self.separator = ttk.Separator(self.sidebar , orient="horizontal")
       
        # self.separator  = tbs.Separator(self.seperator_frame)
        # self.separator  = ttk.Separator(self.seperator_frame, orient="horizontal")
        # self.upper_sidebar  = tk.Frame(self.main_page, height=50 , width=600  ,background=colors.upper_sidebar)
        self.dashboard_button  = ctk.CTkButton(self.sidebar , text="Dashboard" , image=self.white_home , corner_radius=0 , hover_color=colors.pinkish_color  , compound="left"   , fg_color=colors.grey_background)
        self.timesheet_button = ctk.CTkButton(self.sidebar , text="Timesheet" , image=self.timesheet_image , corner_radius=0 ,  hover_color=colors.pinkish_color ,compound="left" , fg_color=colors.grey_background)
        self.todo_button  = ctk.CTkButton(self.sidebar , text="Todo           " , image=self.todo_image , corner_radius=0 , hover_color=colors.pinkish_color , compound="left" , fg_color=colors.grey_background )

        # setting frame and the relevant buttons in the bottom frame and 
        self.bottom_frame = tk.Frame(self.sidebar  , background=colors.golden_color , height=30)
        self.bottom_frame.pack_propagate(0)
        self.notification_button = tk.Button(self.bottom_frame ,text="🔔" , relief="flat" , bd= 0 , height=1 , width=4)
        self.first_seperator   = ttk.Separator(self.bottom_frame , orient="vertical")
        self.settings_button  =tk.Button(self.bottom_frame , text="⚙️" , relief="flat" , bd = 0 , height=1 ,width=4)
        self.second_seperator  = ttk.Separator(self.bottom_frame , orient="vertical")
        # making the third button which will change the sidebar width  : 
        self.open_close_button  = tk.Button(self.bottom_frame , text="\u003C" , height=1 , bd=  0, relief="flat" , width=4)
        
       

        #### Packing the controls : 
        self.sidebar.pack(side="left" , fill="y" )
        # self.upper_sidebar.pack(side="top" , fill="x")
        self.image_label.pack(side="top" , pady=10)
        self.profile_name.pack(side="top" , padx=10)
       
        self.separator.pack(fill="x" , pady=10)
        self.dashboard_button.pack(fill="x")
        self.timesheet_button.pack(fill="x")
        self.todo_button.pack(fill="x")

        self.bottom_frame.pack(side="bottom" , fill ="x")
        # make the method to make the grid with the some padx and pady : 
        
        self.notification_button.grid(row = 0 , column=0 , padx=10)
        self.first_seperator.grid(row = 0  , column=1)
        self.settings_button.grid(row = 0 , column=2 , padx=10)
        self.second_seperator.grid(row=0 , column=3)
        self.open_close_button.grid(row= 0 , column=4 , padx=10)
        # Caling the main app : 
        self.main_page.mainloop()




if __name__ == '__main__':
    main = Main_Page("master" , 100,100)
