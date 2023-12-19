import tkinter as tk 
from tkinter import ttk 
import customtkinter
import ttkbootstrap




class Sidebar():

    def __init__(self , master , height  ,  width) -> None:
        self.Sidebar  = master
        self.main_frame  = tk.Frame()