from tkinter import filedialog
import customtkinter as ctk

def browse_button(button: ctk.CTkButton, entry: ctk.CTkEntry):
    directory = filedialog.askdirectory()
    print(directory)
    entry.configure(textvariable=directory)