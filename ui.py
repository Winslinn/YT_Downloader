from tkinter import *
from tkinter import font
from tkinter import ttk

import customtkinter as ctk
import main as lg
import font_load

theme_bg = '#f5f6fa'

root = Tk()
font_load.load(['font/Roboto-Italic.ttf'])

root.title('YouTube URL video scrap')
root.resizable(False, False)
root.geometry("400x300")
root.configure(bg=theme_bg)

container = Frame(root, bg=theme_bg)
container.place(x=20)

label = Label(container, bg=theme_bg, text='YouTube video downloader', font='Roboto 16 bold')
label.grid(sticky='w', ipady=20)

entry_Frame = Frame(container, bg=theme_bg)
entry_Frame.grid()

url_label = Label(entry_Frame, text='Paste video url:', fg='#2f3640', bg=theme_bg, font='Roboto 12 bold')
url_label.grid(sticky='w')

url_var = StringVar()
url_entry = ctk.CTkEntry(entry_Frame, font=('Roboto', 12), fg_color='#dcdde1', border_color='#718093', text_color='#2f3640', textvariable=url_var,placeholder_text="URL", width=360, height=15)
url_entry.bind('<KeyRelease>', lambda e: lg.url_changed(url_var, download_button))
url_entry.grid()

path_label = Label(entry_Frame, text='Enter path for video:', fg='#2f3640', bg=theme_bg, font='Roboto 12 bold', anchor='sw')
path_label.grid(sticky='w', ipady=10)

path_label = ctk.CTkLabel(entry_Frame, text='',font=('Roboto', 1), bg_color=theme_bg, text_color='#718093', anchor='w', width=1, height=0)
path_label.bind('<Configure>',lambda e: lg.path_changed(path_label, download_button))
path_label.bind('<Button-1>',lambda e: lg.open_directory(path_label))
path_label.bind('<Enter>',lambda e: lg.label_in(path_label))
path_label.bind('<Leave>',lambda e: lg.label_out(path_label))
path_label.grid(sticky='w')

path_button = ctk.CTkButton(entry_Frame, text='Browse', fg_color='#718093', font=('Roboto', 12), width=30, height=15, command=lambda: lg.browse_button(path_button, path_label))
path_button.grid(sticky='w')

progress_label = Label(entry_Frame, text='Progress: 0%', bg=theme_bg)

download_prgBar = ttk.Progressbar(entry_Frame, length=360)

download_button = ctk.CTkButton(entry_Frame, text='Download a video', fg_color='#44bd32', font=('Roboto', 12, 'bold'), height=15, command=lambda: lg.download_button(download_button, download_prgBar, progress_label, url_entry))

root.mainloop()