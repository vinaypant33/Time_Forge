import tkinter as tk 
from math import sin , cos , radians
import colors
import time

from pubsub import pub

class Clock():
    
    def __init__(self , master_frame , width  , height ) -> None:
        self.main_clock  = master_frame
        self.width  = width
        self.height  = height
        self.main_clock.configure(background = colors.app_base)
        self.start_angle = 90
        self.arc_length  = 0
        self.radius  = 65
        self.clock_canvas  = tk.Canvas(self.main_clock , width  = self.width , height = self.height , bg=colors.app_base)
        self.clock_canvas.pack()
        
        self.center_x  = self.clock_canvas.winfo_reqwidth() /2
        self.center_y = self.clock_canvas.winfo_reqheight() /2
        

        # Make the Arc for tkinter canvas : 
        self.clock_arc  = self.clock_canvas.create_arc(10,10,150,150 , start = self.start_angle , extent  = self.arc_length ,fill='blue', outline=colors.text, width=5, style='arc')
        
        center_angle = self.start_angle + self.arc_length / 2
        center_x_arc = self.center_x + self.radius * cos(radians(center_angle))
        center_y_arc = self.center_y + self.radius * sin(radians(center_angle))
        # self.clock_canvas.create_text(center_x_arc, center_y_arc, text="Center Text", font=('Arial', 10))
    
    def change_with_time(self):
        self.arc_length+=6
        self.clock_canvas.delete(self.clock_arc)  
        
        end_angle = self.start_angle + self.arc_length
        end_x = 150 + 100 * cos(radians(end_angle))
        end_y = 150 + 100 * sin(radians(end_angle))
        
        self.clock_arc = self.clock_canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,self.center_x + self.radius,self.center_y + self.radius, start=self.start_angle,
                                          extent=self.arc_length, fill='blue', outline=colors.text, width=5, style='arc')
        
        self.clock_canvas.update()
        self.main_clock.after(1000 , self.change_with_time)
        

if __name__ == '__main__':
    root = tk.Tk()
    main = Clock(root, 200 , 150)
    
    root.after(1000 , main.change_with_time)
    root.mainloop()
    
        
        