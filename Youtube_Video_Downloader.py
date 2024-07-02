from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
Folder_Name = ""
#Choose Location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name, fg='green')
    else:
        locationError.config(text="Please Choose Folder!", fg='red')
#Download Video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)
        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Select Download Quality!", fg='red')
    else:
        ytdError.config(text="Check Url!", fg='red')
    #Download Function
    select.download(Folder_Name)
    ytdError.config(text="Download Complete!", fg='green')
def videoName():
    url = ytdEntry.get()
    if(len(url)>1):
        video = YouTube(url)
        name = video.title
        ytdError.config(text=name, fg='green')
    else:
        ytdError.config(text="Check Url!", fg='red')
def channelName():
    url = ytdEntry.get()
    if(len(url)>1):
        chvideo = YouTube(url)
        chname = chvideo.author
        ytdError.config(text=chname, fg='green')
    else:
        ytdError.config(text="Check Url!", fg='red')
def ytdViews():
    url = ytdEntry.get()
    if(len(url)>1):
        cvideo = YouTube(url)
        view = cvideo.views
        ytdError.config(text=view, fg='green')
    else:
        ytdError.config(text="Check Url!", fg='red')
def ytdLength():
    url = ytdEntry.get()
    if(len(url)>1):
        hvideo = YouTube(url)
        lenth = hvideo.length
        ytdError.config(text=lenth, fg='green')
    else:
        ytdError.config(text="Check Url!", fg='red')
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("760x500")
root.attributes('-alpha',0.9)
root.iconbitmap('Brand-Logo-Icon.ico')
root.resizable(False, False)
root.configure(bg='lemon chiffon')
ytdL = Label(root, text="", font=("Times", "24", "bold italic"), bg='lemon chiffon')
ytdL.grid(column=0)
ytdL = Label(root, text="", font=("Times", "24", "bold italic"), bg='lemon chiffon')
ytdL.grid(column=4)
#Get URL Label
ytdLabel = Label(root, text="Enter URL of the Video", font=("Times", "24", "bold italic"), bg='lemon chiffon')
ytdLabel.grid(row=0, column=2)
#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50,textvariable=ytdEntryVar, bd='3', bg='peach puff', font=("Times", "14"))
ytdEntry.grid(row=1, column=2)
#Error Message
ytdError = Label(root, text="", fg="red", font=("Helvetica", "12"), bg='lemon chiffon')
ytdError.grid(row=2, column=2)
#Space
space3 = Label(root, text="", bg='lemon chiffon')
space3.grid(row=3, column=1)
#Save Video Level
saveLabel = Label(root, text="Select Location to Save the Video", font=("Times", "16", "italic"), bg='lemon chiffon')
saveLabel.grid(row=4, column=2)
#Choose Path Button
saveEntry = Button(root, bg="red", fg="white", text="Choose Path", font=("Helvetica", "12", "italic"), bd='3', command=openLocation)
saveEntry.grid(row=5, column=2)
#Location Error Message
locationError = Label(root, text="", fg='red', font=("Helvetica", "12"), bg='lemon chiffon')
locationError.grid(row=6, column=2)
#Video Quality
ytdQuality = Label(root, text="Select Quality", font=("Times", "13", "italic"), bg='lemon chiffon')
ytdQuality.grid(row=7, column=2)
#Qualities ComboBox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices, font=("Helvetica", "12", "italic"))
ytdchoices.grid(row=8, column=2)
#Space
space2 = Label(root, text="", bg='lemon chiffon')
space2.grid(row=9, column=1)
#Download Button
downloadBtn = Button(root, text = "Get Video Title", fg='white', bg='red', font=("Helvetica", "12", "italic"), bd='3', command=videoName)
downloadBtn.grid(row=10, column=1)
downloadBtn1 = Button(root, text = "Get Channel Name", fg='white', bg='red', font=("Helvetica", "12", "italic"), bd='3', command=channelName)
downloadBtn1.grid(row=10, column=3)
downloadBtn2 = Button(root, width=50, text = "Download Video", fg='white', bg='maroon', font=("Helvetica", "12", "italic"), bd='3', command=DownloadVideo)
downloadBtn2.grid(row=11, column=2)
downloadBtn3 = Button(root, text = "See Views", fg='white', bg='red', font=("Helvetica", "12", "italic"), bd='3', command=ytdViews)
downloadBtn3.grid(row=12, column=1)
downloadBtn4 = Button(root, text = "Check Video Length", fg='white', bg='red', font=("Helvetica", "12", "italic"), bd='3', command=ytdLength)
downloadBtn4.grid(row=12, column=3)
#Space
space1 = Label(root, text="", bg='lemon chiffon')
space1.grid(row=13, column=1)
#Space
space4 = Label(root, text="", bg='lemon chiffon')
space4.grid(row=14, column=1)
#Developer Label
developerlabel = Label(root, text="Developed by Raunak Kumar", font=("Helvetica", "18", "italic",), bg='green', fg='white')
developerlabel.grid(row=15, column=2)
root.mainloop()
