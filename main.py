from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


def select_path():
    path =  filedialog.askdirectory()
    path_label.config(text=path)
    
def download_file():
    get_link = link_entry.get()
    
    user_path = path_label.cget("text")
    
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    VideoFileClip(mp4_video)

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo_image = PhotoImage(file='youtube_logo_icon_154503.png')
logo_image = logo_image.subsample(4,4)
canvas.create_image(250,80,image=logo_image)

link_label = Label(screen, text="Enter Download Link: ", font=('Arial',15))
link_entry = Entry(screen, width=50)

canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_entry)

path_label = Label(screen, text="Select a folder: ", font=('Arial', 15))
select_path_button = Button(screen, text="Select", command= select_path)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_path_button)

download_button = Button(screen, text="Download")
canvas.create_window(250, 390, window=download_button)
screen.mainloop()