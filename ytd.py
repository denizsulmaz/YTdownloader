
# Importing necessary packages
from tkinter import *
import pathlib
from pytube import YouTube
# pip install pytube3
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    link_label = Label(root, text="YouTube link :", bg="#E8D579", width=20)
    link_label.grid(row=1, column=0, pady=5, padx=5)

    linkText = Entry(root, width=55, textvariable=video_Link)
    linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Destination :", bg="#E8D579", width=20)
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    destinationText = Entry(root, width=40, textvariable=download_Path)
    destinationText.grid(row=2, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Browse", command=Browse, width=10, bg="#05E8E0")
    browse_B.grid(row=2, column=2, pady=1, padx=1)

    Download_B = Button(root, text="Download", command=Download, width=20, bg="#05E8E0")
    Download_B.grid(row=3, column=1, pady=3, padx=3)


# Defining Browse() to select a
# destination folder to save the video
def Browse():
    download_Directory = filedialog.askdirectory(initialdir=pathlib.Path.cwd())
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)


# Defining Download() to download the video
def Download():
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()
    # select the optimal location for
    # saving file's
    download_Folder = download_Path.get()
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
    # Getting all the available streams of the
    # youtube video and selecting the first
    # from the
    videoStream = getVideo.streams.first()
    # Downloading the video to destination
    # directory
    videoStream.download(download_Folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


# Creating object of tk class
root = Tk()
root.geometry("500x110")
root.resizable(0, 0)
root.title("YouTube Video Downloader")
root.config(background="#000000")
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
# Calling the Widgets() function
Widgets()
root.mainloop()
