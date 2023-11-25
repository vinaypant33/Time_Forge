import tkinter as tk 
from tkinter import ttk
import colors
import fonts
import styles
import customtkinter as ctk
from tkinter import Menu

import messagebox # for making messageboxes available on temnporary basis 
from ctypes import windll

# Importing Library for Message Passing :  Pubsub
from pubsub import pub

# importing pre made libraries : 
import planned_task
import current_task
import tooltip

class Main_Page():

    # Pre Made function to make the app logo visible in the minimized position
    def set_appwindow(self ,root):
        GWL_EXSTYLE=-20
        WS_EX_APPWINDOW=0x00040000
        WS_EX_TOOLWINDOW=0x00000080
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.wm_withdraw()
        root.after(1000, lambda: root.wm_deiconify())

    # Functions for running the app : 
    def mouse_click(self , event):
        self.x  = event.x 
        self.y = event.y


    def mouse_move(self , event):
        self.delta_x  = event.x - self.x
        self.delta_y = event.y - self.y
        self.new_x = self.main_app.winfo_x() + self.delta_x
        self.new_y  = self.main_app.winfo_y() + self.delta_y
        self.main_app.geometry(f'{self.width}x{self.height}+{self.new_x}+{self.new_y}')

    def closing_app(self):
        self.main_app.destroy()
    
    def max_button_clicked(self):
        messagebox.showerror("Task Forge" , "Unable to maxmize the app : Maximize function disabled")
    
    def min_button_clicked(self):
        self.main_app.overrideredirect(False)
        self.main_app.wm_iconify()
        self.main_app.bind('<FocusIn>' , self.on_deiconify)
    
    def on_deiconify(self , event):
        if self.main_app.wm_state() == 'normal' and self.main_app.overrideredirect() != True : 
                self.main_app.overrideredirect(True)
                self.set_appwindow(self.main_app)
                self.main_app.deiconify()
        

    def adding_text(self ):
        self.char_length = len(self.enter_text.get())
        if self.char_length < 1 : 
            messagebox.showerror("Task Forge" , "Please Enter Task : Empty Task Name")
        else:
            if self.planned_task_frame.winfo_ismapped() == True:
                self.getting_text  = self.enter_text.get()
                self.enter_text.delete(0  ,tk.END)
                self.current_index+=1
                planned_task.Planned_Task(self.planned_task_scrollable_frame , 40  , 40 ,self.getting_text , self.current_index)
            else:
                self.enter_text.delete(0  , tk.END)
        
    
    def adding_text_1(self , event):
        self.char_length = len(self.enter_text.get())
        if self.char_length < 1 : 
            messagebox.showerror("Task Forge" , "Please Enter Task : Empty Task Name")
        else:
            if self.planned_task_frame.winfo_ismapped() == True:
                self.getting_text  = self.enter_text.get()
                self.enter_text.delete(0  ,tk.END)
                self.current_index+=1
                planned_task.Planned_Task(self.planned_task_scrollable_frame , 40  , 40 ,self.getting_text , self.current_index)
            else:
                self.enter_text.delete(0  , tk.END)
                
        
    def frame_change(self , passed_text): # check the function and change the frame with the click of the button  :
        if passed_text == "currenttask":
            self.planned_task_frame.pack_forget()
            self.planned_task_scrollable_frame.pack_forget()
            self.completed_task_frame.pack_forget()
            self.completed_task_scrollable_frame.pack_forget()
            self.current_task_frame.pack(fill='both' , padx=10 , pady=10 , expand=True)
            self.current_task_scrollable_frame.pack()
        elif passed_text == "plannedtask" : 
            self.current_task_frame.pack_forget()
            self.current_task_scrollable_frame.pack_forget()
            self.completed_task_frame.pack_forget()
            self.completed_task_scrollable_frame.pack_forget()
            self.planned_task_frame.pack(fill='both' , padx=10 , pady=10 , expand=True)
            self.planned_task_scrollable_frame.pack()
        elif passed_text == "completedtask":
            self.planned_task_frame.pack_forget()
            self.planned_task_scrollable_frame.pack_forget()
            self.current_task_frame.pack_forget()
            self.current_task_scrollable_frame.pack_forget()
            self.completed_task_frame.pack(fill='both' , padx=10 , pady=10 , expand=True)
            self.completed_task_scrollable_frame.pack()
            
            

    def __init__(self , width  , height) -> None:
        self.main_app = tk.Tk()
        self.width  = width 
        self.height  = height
        
        # calling the after functiion to call the min button for showing the bottom icon  : 
        self.main_app.after(10 , lambda  : self.set_appwindow(self.main_app))

        self.current_index = 0
        self.char_length  = 0

        self.main_app.overrideredirect(True)

        # setting up the geometry and setting up the app in the center of the screen : 
        self.x_position  = (self.main_app.winfo_screenwidth() //2 )   - ( self.width  // 2 )
        self.y_postition  = (self.main_app.winfo_screenheight() //2  )  - (self.height //2 )        

        # setting up the geomery and making the main app  : 
        self.main_app.geometry(f'{self.width}x{self.height}+{self.x_position}+{self.y_postition}')

        # Making the title bar and setting up the app with the custom title bar : 
        self.titlebar = tk.Frame(self.main_app ,height=24  ,background=colors.upper_tab_color)
        # self.titlebar.pack_propagate(0)
        self.app_titlebar_label  = tk.Label(self.titlebar , text="Time Forge" , background=colors.upper_tab_color , foreground=colors.text)
        
        # Buttons for the titlebar and messgae for the max button : 
        self.close_button  = tk.Button(self.titlebar , text='\u2716' , command=self.closing_app)
        self.max_button   = tk.Button(self.titlebar , text = u"\U0001F5D6" , command=self.max_button_clicked)
        self.min_button   = tk.Button(self.titlebar  , text="\u23AF" , command = self.min_button_clicked)
        
        # Bottom base titlebar and its controls : 
        self.basetitlebar = tk.Frame(self.main_app , height= 35  , background=colors.upper_tab_color) 
        self.basetitlebar.pack_propagate(0)
        # making settings , add button for bottom title bar : 
        self.settings_button  = tk.Button(self.basetitlebar , text="\u2699" )
        self.add_task_button   = tk.Button(self.basetitlebar , text="\u002B" , font=fonts.super_small_bold , command=self.adding_text)

        # Text box for the bottom basetitlebar and  make text box for entering in the work app  :z
        self.enter_text = tk.Entry(self.basetitlebar  , background=colors.app_base , bd= 2 ,  width=53 , foreground=colors.text , relief='flat' ,  highlightthickness=2, highlightcolor=colors.app_base) # Will change this code later make seperate frame for adding the task data

        # Frame for the canvas ,  clock and current text with time : 
        self.add_task_button.configure(width=3)
        self.clock_main_frame  = tk.Frame(self.main_app , background=colors.app_base , height=150 )
        self.clock_main_frame.pack_propagate(0)
        
        self.seperator   = tk.Frame(self.main_app , height=2 , background=colors.upper_tab_color) # To change the seperator later for more robust look and feel : make the whole app more material design

        self.button_frame = tk.Frame(self.main_app  , height=60 , background=colors.app_base ) # will give this color later when testing the
        self.button_frame.pack_propagate(0)
        self.button_under_frame = tk.Frame(self.button_frame, background=colors.clock_base , width=325  ,height=40)
        self.button_under_frame.pack_propagate(0)
        
        ''' Frame for showing planned completed and current task data 
        Frames to be packed and unpacked for different frames '''

        # Making the Main frame in which the three frames will be placed : 
        self.planned_task_frame = tk.Frame(self.main_app  , background=colors.app_base) # setting another frame from custom tkitner inside this frame : it was red and will change this to app color later
        self.current_task_frame  = tk.Frame(self.main_app , background=colors.app_base) # second frame for the planned task frame
        self.completed_task_frame  = tk.Frame(self.main_app ,background=colors.app_base) # third frame for the completed tasks. 
        # Making two more frames on Temporary basis for changing the frames when the buttons are clicked : 
        
       # loading the scrollable frame for all three task frames 
        self.planned_task_scrollable_frame  = ctk.CTkScrollableFrame(self.planned_task_frame , fg_color='transparent',  width=400 , height=300)
        self.current_task_scrollable_frame = ctk.CTkScrollableFrame(self.current_task_frame , fg_color='transparent' , width=400 , height=300)
        self.completed_task_scrollable_frame  = ctk.CTkScrollableFrame(self.completed_task_frame , fg_color="transparent" , width=400 , height=300)
        
        

        # Three buttons are to be added as : planned task , current doing  , completed tasks
        self.planned_task_button  = tk.Button(self.button_under_frame , text="Planned Task" ,  command=lambda : self.frame_change("plannedtask") )
        self.current_seperator_1  = ttk.Separator(self.button_under_frame , orient='vertical')
        self.current_task_button  = tk.Button(self.button_under_frame , text="Current Task" , command=lambda : self.frame_change("currenttask"))
        self.current_seperator_2  = ttk.Separator(self.button_under_frame , orient='vertical')
        self.completed_task_button  = tk.Button(self.button_under_frame , text="Completed Task")
        
        
        
        # Making the right click button 
        # 3 Menu bar to be made all 3 to be done : All three would point to a common function : 
        self.planned_task_menu = Menu(self.planned_task_scrollable_frame , tearoff= 0 )
        

        # configuring the controls: 
        self.app_titlebar_label.configure(font=fonts.super_small_bold)
        self.main_app.configure(background=colors.app_base)
        self.close_button.configure(height=1 , width=4)
        self.max_button.configure(height=1, width=4)
        self.min_button.configure(height=1 , width=4)
        


        styles.Styles.button_styles(self.close_button , colors.upper_tab_color , colors.text , colors.tab_color_unused  , colors.red_color)
        styles.Styles.button_styles(self.max_button , colors.upper_tab_color , colors.text , colors.tab_color_unused  , colors.text)
        styles.Styles.button_styles(self.min_button , colors.upper_tab_color, colors.text , colors.tab_color_unused  , colors.text)
        styles.Styles.button_styles(self.settings_button , colors.upper_tab_color , colors.text  , colors.tab_color_unused , colors.text)
        styles.Styles.button_styles(self.add_task_button , colors.upper_tab_color  , colors.text , colors.tab_color_unused , colors.text)

        styles.Styles.button_styles(self.planned_task_button , colors.upper_tab_color , colors.text , colors.tab_color_unused  , colors.red_color)
        styles.Styles.button_styles(self.completed_task_button , colors.upper_tab_color , colors.text , colors.tab_color_unused  , colors.red_color)
        styles.Styles.button_styles(self.current_task_button , colors.upper_tab_color , colors.text , colors.tab_color_unused  , colors.red_color)
        
    
        

        # configuring the tool tip for the controls : 
        tooltip.ToolTip(self.settings_button , "Settings" , colors.app_base , colors.upper_tab_color)
        tooltip.ToolTip(self.add_task_button , "Add Task" , colors.app_base , colors.upper_tab_color)
        tooltip.ToolTip(self.planned_task_button, "Switch to planned task tab" , colors.app_base , colors.upper_tab_color)
        tooltip.ToolTip(self.completed_task_button, "Switch to completed task tab" , colors.app_base , colors.upper_tab_color)
        tooltip.ToolTip(self.current_task_button, "Switch to current task tab" , colors.app_base , colors.upper_tab_color)
        


        # Binding the Frames : 

        self.titlebar.bind("<Button-1>" , self.mouse_click)
        self.titlebar.bind("<B1-Motion>" , self.mouse_move)
        self.enter_text.bind("<Return>" , self.adding_text_1)

       
        
  
        # Packing Controls : 

        self.titlebar.pack(side= 'top' , fill='x')
        self.app_titlebar_label.pack(side='left' , padx=2)
        self.close_button.pack(side='right' , padx=0 ,pady=0)
        self.max_button.pack(side='right' , padx=0)
        self.min_button.pack(side='right' , padx = 0)

        self.basetitlebar.pack(side='bottom' ,padx=0  ,fill='x')
        # self.settings_button.pack(side='left' , padx = 5 , pady = 5)
        self.settings_button.grid(row=0 , column= 0 ,padx=4 , pady=5)

        # self.enter_text.pack()
        self.enter_text.grid(row=0 , column=1 , padx=4 , pady=5)

        # self.add_task_button.pack(side='right'  , padx = 2 , pady=4)
        self.add_task_button.grid(row=0 , column=2 , padx=4  , pady=5)

        self.clock_main_frame.pack(fill='x')
        self.seperator.pack(fill='x')

        self.button_frame.pack(fill='x')
        self.button_under_frame.pack(padx=20 , pady=10)

        self.planned_task_button.pack(side='left', padx=10 )
        self.current_seperator_1.pack(side='left' , padx=2 , pady=5 , fill='y')
        self.current_task_button.pack(side='left' , padx=10)
        self.current_seperator_2.pack(side='left' , pady=5 , padx=2 , fill='y')
        self.completed_task_button.pack(side='left', padx=10)

        self.planned_task_frame.pack(fill='both' , padx=10 , pady=10 , expand=True)
        self.planned_task_scrollable_frame.pack()


        self.main_app.mainloop()


if __name__ == '__main__':
    hehe = Main_Page(400 , 600)