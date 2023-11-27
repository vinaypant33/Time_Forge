import tkinter as tk 
import customtkinter
from tkinter import ttk 
import fonts 
import colors 
import styles
from pubsub import pub

import tooltip

class Planned_Task():

    def adding_text(self):
        pub.sendMessage("adding_current_text" , current_text = self.text.get("1.0", "end-1c"))
        
        # pub.subscribe(self.delete_current_task , "deleting_task")
        # self.delete_current_task()
        
    
    def delete_current_task(self):
        self.text.destroy()
        self.delete_button.destroy()
        self.inner_frame.destroy()
            

    def __init__(self , master , width , height   , current_text , current_index) -> None:
        self.master = master
        self.width  = width 
        self.height  = height
        self.current_index  = current_index
        self.current_text = current_text

        # Make the main text box for the main frame 
        self.inner_frame  = tk.Frame(self.master , background=colors.app_base)
        self.inner_frame.pack_propagate(0)
        self.text  = tk.Text(self.inner_frame , height=self.height, width=self.width , font=fonts.super_small_bold)
        self.text.insert(tk.END , self.current_text)
        self.text.configure(state="disabled")
        self.inner_frame.pack()
        self.text.grid(row=0  , column=0 , rowspan=2)
        
        
        
        
        # setting up a temporary button for deleting the currnet task : 
        self.delete_button  = tk.Button(self.inner_frame , text='\u2716' , command=self.delete_current_task , height=2  ,width=2)
        # Button for setting up the button to transfer the current task to the completed tab 
        self.play_button   = tk.Button(self.inner_frame , text = "\u25B6" , height=2 ,  width=2 , font=fonts.super_small_bold , command=self.adding_text)
        
        
        
        styles.Styles.button_styles(self.delete_button , colors.app_base , colors.text , colors.red_color , colors.text)
        styles.Styles.button_styles(self.play_button , colors.app_base , colors.text , colors.red_color , colors.text)
        
        tooltip.ToolTip(self.delete_button , "Delete Task" , colors.upper_tab_color , colors.app_base)
        tooltip.ToolTip(self.play_button , "Start Task" , colors.upper_tab_color , colors.app_base)
        
        
        self.delete_button.grid(row=1 , column=1)
     
        self.play_button.grid(row= 0 , column=1)
        
        # self.master.configure(background = colors.app_base )
        self.text.configure(background=colors.app_base , foreground=colors.text)


        self.master.mainloop()
    



if __name__ == '__main__':
    main = Planned_Task(tk.Tk() , 100 ,2 , "I am the one" , 1 )