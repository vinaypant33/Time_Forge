import tkinter as tk 
import customtkinter
from tkinter import ttk 
import fonts 
import colors 
import styles

class Completed_Task():

    def adding_text(self):
        pass
    
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
        self.inner_frame  = tk.Frame(self.master)
        self.inner_frame.pack_propagate(0)
        self.text  = tk.Text(self.inner_frame , height=2, font=fonts.super_small_bold)
        self.text.insert(tk.END , self.current_text)
        self.text.configure(state="disabled")
        self.inner_frame.pack()
        self.text.grid(row=0  , column=0)
        
        
        
        
        # setting up a temporary button for deleting the currnet task : 
        self.delete_button  = tk.Button(self.inner_frame , text='\u2716' , command=self.delete_current_task , height=2 )
        
        
        
        
        styles.Styles.button_styles(self.delete_button , colors.app_base , colors.text , colors.red_color , colors.text)
        self.delete_button.pack(side='right')
        # self.master.configure(background = colors.app_base )
        self.text.configure(background=colors.app_base , foreground=colors.text)


        self.master.mainloop()
    



if __name__ == '__main__':
    main = Completed_Task(tk.Tk() , 100 ,100 , "I am the one" , 1 )