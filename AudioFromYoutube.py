from pytube import YouTube
from tkinter import *
from tkinter import ttk


def download_link(link):
    """download func"""
    yt = YouTube(link, use_oauth=True)
    # ищем аудио по тегу itag
    # print(yt.streams)
    stream = yt.streams.get_by_itag(251)  # 251 tag direct to audio content
    return stream.download(output_path='D:\Downloads')


def window_api():
    """window_api func"""

    def get_link():
        link = entry.get()
        entry.delete(0, END)
        return download_link(link)

    root = Tk()
    root.title("Youtube Downloader")
    root.geometry("400x150")

    label = Label(text="Input link: ")
    label.pack()

    entry = ttk.Entry()
    entry.pack(padx=20, fill=X)

    btn = ttk.Button(text="Download", command=get_link)
    btn.pack(pady=30)
    root.mainloop()


window_api()
