from tkinter import filedialog
from tkinter import ttk, Label, StringVar

import customtkinter as ctk
import os
import bs4
import requests

correct_path = False
correct_URL = False

url_str = ''

def open_directory(label: ctk.CTkLabel):
    os.startfile(label.cget('text'))
    
def label_in(label: ctk.CTkLabel):
    if label.cget('text') != '':
        label.configure(font=('Roboto', 12, 'underline'))
        
def label_out(label: ctk.CTkLabel):
    if label.cget('text') != '':
        label.configure(font=('Roboto', 12))
        
def path_changed(label: ctk.CTkLabel, button: ctk.CTkButton):
    if label.cget('text') != '':
        global correct_path
        correct_path = True
    else: correct_path = False
    
    args_changed(button)

def url_changed(var, button: ctk.CTkButton):
    global url_str
    global correct_URL
    
    if url_str != var.get():
        url_str = var.get()
    
    if url_str.find('https://www.youtube.com/watch?v') != -1:
        correct_URL = True
    else: correct_URL = False
    
    args_changed(button)

def args_changed(button: ctk.CTkButton):
    if correct_URL and correct_path:
        button.grid(pady=65)
    else: button.grid_forget()

def browse_button(button: ctk.CTkButton, label: ctk.CTkEntry):
    directory = filedialog.askdirectory()
    
    if directory != '':
        button.configure(text='Change')
        label.configure(text=directory, font=('Roboto', 12), cursor='hand2')
        
def download_button(button: ctk.CTkButton, prgBar: ttk.Progressbar, prgLabel: Label, url_label: ctk.CTkEntry):
    prgLabel.grid(ipady=22, sticky='w')
    prgLabel.configure(anchor='s')
    
    url_label.configure(state='disabled', text_color='#718093')
    
    button.grid_forget()
    prgBar.grid(sticky='w')
    button.grid_forget()
    
    page = requests.get(url_str)
    
    if page.status_code == 200:
        