from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import youtube_dl

import sys

root = Tk()
# root.resizable(0, 0)
root.geometry("500x600")


def handle_focus_in(_):
    e1.delete("1.0", "end")
    e1.config(fg='black')


def download_mp3(dir, url):
    # messagebox.showinfo('Folder Selection', 'Select download folder')
    # directory = filedialog.askdirectory()
    # ydl_opts = {
    #     'outtmpl': dir + '%(title)s-%(id)s',  # ~/Downloads/%(title)s-%(id)s.%(ext)s
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     }],
    # }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([url])
    pass



def download_video(url, file_type):
    messagebox.showinfo('Folder Selection', 'Select download folder')
    directory = filedialog.askdirectory()
    # youtube_dl -f bestvideo+bestaudio
    # if file_type == "mp3":
    ydl_opts = {
        # 'outtmpl': directory + '%(title)s.%(ext)s',  # ~/Downloads/%(title)s-%(id)s.%(ext)s
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'postprocessors': [{
        }],
    }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     info_dict = ydl.extract_info(url, download=False)
    #     video_title = info_dict.get('title', None)

    # if file_type == "mp3":
    #     path = f'{directory}/{video_title}.mp3'
    # if file_type == "mp4":
    #     path = f'{directory}/{video_title}.mp4'

    ydl_opts.update({'outtmpl': directory + '%(title)s.%(ext)s'})

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    messagebox.showinfo('Success', 'Download completed')


def save():
    url = e1.get("1.0", 'end-1c')
    print(url)
    file_type = var.get()
    if url != "":
        if format != "":
            if format == "mp4":
                download_video(url, file_type)
            else:
                download_mp3(url, file_type)
        else:
            messagebox.showerror("Error", "Please select format")
    else:
        messagebox.showerror("Error", "Please enter url")


def exit():
    sys.exit()


data = {'mp3', 'mp4'}

if __name__ == '__main__':
    root.title('Youtube downloader')
    l1 = Label(root, text='Download MP3 from Youtube video', font=20, justify=CENTER)
    l1.place(x=70, y=100)

    var = StringVar()
    fileType = OptionMenu(root, var, *data)
    fileType.place(x=445, y=155)

    e1 = Text(root, height=2, width=50)
    # e1.insert(END, 'Enter youtube url here')
    e1.place(x=20, y=150)

    b1 = Button(root, text='Download', width=7, height=2, command=save)
    b1.place(x=80, y=250)

    b2 = Button(root, text='Exit', command=exit, width=7, height=2)
    b2.place(x=280, y=250)

    # e1.bind("<FocusIn>", handle_focus_in)
    root.mainloop()
