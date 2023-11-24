import tkinter as tk 

import colors
import fonts
import styles


root = tk.Tk()

class Current_task():
    
    
    def __init__(self, master , width ,  height) -> None:
        self.ct_tab  = tk.Frame(master=master , background=colors.red_color ,width=width , height = height)
        
        self.ct_tab.pack(side='top' , expand=True , fill='both')
        
        
        


if __name__ == '__main__':
    ct  = Current_task(root , 100 ,100)
    root.mainloop()
        
        