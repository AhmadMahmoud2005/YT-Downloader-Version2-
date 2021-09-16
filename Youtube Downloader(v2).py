from pytube import YouTube
from pytube import Playlist
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from pytube.contrib.playlist import Playlist

def video():
    label_of_entry["text"] = "Enter the video link"
    download_button["command"] = download_video

def playlist():
    label_of_entry["text"] = "Enter the playlist link"
    download_button["command"] = download_playlist

def download_video():
    download_button.config(state=DISABLED)
    label_of_download = Label(root, text=f"Wait for download...")
    label_of_download.grid(row=9, column=0)
    root.update_idletasks()
    link_path = entry2.get()
    link_video = entry1.get()
    clip = YouTube(link_video)
    if combo_path.get() == "video":
        clip.streams.filter(progressive=True, res=combo_quality.get()).first().download(output_path=link_path)
    else:
        clip.streams.filter(progressive=False, type=combo_path.get(), abr='160kbps').first().download(output_path=link_path)
    messagebox.showinfo("Success", f'The Download is finished Successfully, you will find your video at:\n{link_path}')
    label_of_download.destroy()
    download_button['state'] = NORMAL

def download_playlist():
    download_button.config(state=DISABLED)
    label_of_download = Label(root, text=f"Wait for download...")
    label_of_download.grid(row=9, column=0)
    root.update_idletasks()
    link_path = entry2.get()
    link_video = entry1.get()
    playlist = Playlist(link_video)
    for clip in playlist.videos:
        if combo_path.get() == "video":
            clip.streams.filter(progressive=True, res=combo_quality.get()).first().download(output_path=link_path)
        else:
            clip.streams.filter(progressive=False, type=combo_path.get(), abr='160kbps').first().download(output_path=link_path)
    messagebox.showinfo("Success", f'The Download is finished Successfully, you will find your video at:\n{link_path}')
    label_of_download.destroy()
    download_button['state'] = NORMAL
    

def selectedcombo(event):
    if combo_path.get() == "audio":
        combo_quality.config(state=DISABLED)
    else:
        combo_quality.config(state=NORMAL)

def browse():
    root.filename = filedialog.askdirectory(initialdir="This PC", title="Browse the path")
    entry2.insert(0, root.filename)


# set the window of app
root = Tk()
root.geometry('700x300')
root.title('Youtube Downloader')

r = StringVar()
r.set("video")

label_of_download = Label(root, text="Do you want to download a single video or a playlist:")
label_of_download.grid(row=0, column=0, pady=8) # label of download

video = Radiobutton(root, text="video", variable=r, value="video", command=video)
video.grid(row=0, column=1)

playlist = Radiobutton(root, text="playlist", variable=r, value="playlist", command=playlist)
playlist.grid(row=0, column=2)

label_of_entry = Label(root, text="Enter the video link: ")
label_of_entry.grid(row=1, column=0, pady=8) # label of entry

label_combo_path = Label(root, text="Choose the video type:")
label_combo_path.grid(row=3, column=0, pady=8) # label of combobox of the type of the video

label_combo_quality = Label(root, text="Choose the video quality:")
label_combo_quality.grid(row=5, column=0, pady=8) # label of combobox of the quality

label_entry2 = Label(root, text="Enter the video path:")
label_entry2.grid(row=7, column=0, pady=8)

entry1 = Entry(root, width=50)
entry1.grid(row=1, column=1, pady=8) # entry of the video link

entry2 = Entry(root, width=40)
entry2.grid(row=7, column=1, pady=8) # entry of the video Path in the device

combo_path = ttk.Combobox(root, values=("video", "audio"))
combo_path.set("video")
combo_path.bind("<<ComboboxSelected>>", selectedcombo)
combo_path.grid(row=3, column=1, pady=8) # combobox of the type of the video

combo_quality = ttk.Combobox(root, values=("144p", "360p", "720p"))
combo_quality.grid(row=5, column=1, pady=8) # combobox of the quality of the video
combo_quality.set("360p")

download_button = ttk.Button(root, text="Download", width=20, command=download_video)
download_button.grid(row=9, column=1, pady=8) # download button

browse_button = ttk.Button(root, text="Browse", command=browse)
browse_button.grid(row=7, column=2, pady=8) # browse button

root.mainloop()
