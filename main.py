from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


def select_path():
    path =  filedialog.askdirectory()
    path_label.config(text=path)
    
def download_file(i):
    get_link = link_entry.get()
    
    user_path = path_label.cget("text")
    if i == 1 :
        vid = YouTube(get_link).streams.get_audio_only().download()
    elif i == 2 :
        vid = YouTube(get_link).streams.filter(res="144p").first().download()
    elif i == 3 :
        vid = YouTube(get_link).streams.filter(res="240p").first().download()
    elif i == 4 :
        vid = YouTube(get_link).streams.filter(res="360p").first().download()
    elif i == 5 :
        vid = YouTube(get_link).streams.filter(res="480p").first().download()
    elif i == 6 :
        vid = YouTube(get_link).streams.filter(res="720p").first().download()
    VideoFileClip(vid)

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=600)
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

canvas.create_window(250, 260, window=path_label)
canvas.create_window(250, 290, window=select_path_button)

download_audio = Button(screen, text="Audio" ,command= lambda:download_file(1))
canvas.create_window(250, 350, window=download_audio)

download_144p = Button(screen, text="144p", command=lambda: download_file(2))
canvas.create_window(250, 390, window=download_144p)

download_240p = Button(screen, text="240p", command=lambda: download_file(3))
canvas.create_window(250, 430, window=download_240p)

download_360p = Button(screen, text="360p", command=lambda: download_file(4))
canvas.create_window(250, 470, window=download_360p)

download_480p = Button(screen, text="480p", command=lambda: download_file(5))
canvas.create_window(250, 510, window=download_480p)

download_720p = Button(screen, text="720p", command=lambda: download_file(6))
canvas.create_window(250, 550, window=download_720p)
screen.mainloop()