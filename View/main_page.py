import tkinter as tk 
import colors
import fonts

# Importing Library for Message Passing :  Pubsub
from pubsub import pub


class Main_Page():

    # Functions for running the app : 
    def mouse_click(self):
        pass

    def mouse_move(self):
        pass

    def closing_app(self):
        self.main_app.destroy()

    def __init__(self , width  , height) -> None:
        self.main_app = tk.Tk()
        self.width  = width 
        self.height  = height


        self.main_app.overrideredirect(True)


        # setting up the geometry and setting up the app in the center of the screen : 
        self.x_position  = (self.main_app.winfo_screenwidth() //2 )   - ( self.width  // 2 )
        self.y_postition  = (self.main_app.winfo_screenheight() //2  )  - (self.height //2 )        

        # setting up the geomery and making the main app  : 
        self.main_app.geometry(f'{self.width}x{self.height}+{self.x_position}+{self.y_postition}')

        # Making the title bar and setting up the app with the custom title bar : 
        self.titlebar = tk.Frame(self.main_app ,height=30  ,background=colors.upper_tab_color)
        self.titlebar.pack_propagate(0)
        self.app_titlebar_label  = tk.Label(self.titlebar , text="Time Forge" , background=colors.upper_tab_color , foreground=colors.text)
        
        # Buttons for the titlebar and messgae for the max button : 
        self.close_button  = tk.Button(self.titlebar , text="close" , command=self.closing_app)
        self.max_button   = tk.Button(self.titlebar , text = "maximize")
        self.min_button   = tk.Button(self.titlebar  , text="minimize")
        # Packing the controls : 
        # Packing titlebar and title text :  label not requied for now  :
        self.titlebar.pack(side= 'top' , fill='x')
        self.app_titlebar_label.pack(side='left' , padx=2)


        #  Making frames : Clock and canvs and the textbar : 
        
        # Packing the buttons for the titlebar : 
        self.close_button.pack(side='right' , padx=0)
        self.max_button.pack(side='right' , padx=0)
        self.min_button.pack(side='right' , padx = 0)
        self.main_app.mainloop()


if __name__ == '__main__':

    hehe = Main_Page(400 , 600)