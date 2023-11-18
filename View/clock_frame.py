import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk 



# only for testing  : 

root = ctk.CTk()
root.geometry("500x500")

button = ctk.CTkButton(master=root, text="CTkButton").pack()

root.mainloop()