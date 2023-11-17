import tkinter as tk 
from tkinter import ttk 
import customtkinter as ctk



# Importing Program made files  : 
from Model import database
from Model import functions

# For Views 
from View import main_page

# For Message Passing  : 
from pubsub import pub


def main():
    main_page.Main_Page() 
    


if __name__ == '__main__':
    main()