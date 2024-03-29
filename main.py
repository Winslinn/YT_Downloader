from tkinter import filedialog
import customtkinter as ctk
import os

def open_directory(label: ctk.CTkLabel):
    os.startfile(label.cget('text'))
    
def label_in(label: ctk.CTkLabel):
    if label.cget('text') != '':
        label.configure(font=('Roboto', 12, 'underline'))

def label_out(label: ctk.CTkLabel):
    if label.cget('text') != '':
        label.configure(font=('Roboto', 12))

def browse_button(button: ctk.CTkButton, label: ctk.CTkEntry):
    directory = filedialog.askdirectory()
    
    label.configure(text=directory, font=('Roboto', 12), width=label.winfo_width, cursor='hand2')
    button.configure(text='Change')