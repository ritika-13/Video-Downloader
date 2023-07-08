from tkinter import*
from mttkinter import mtTkinter
from pytube import YouTube

root=Tk() #Used to initialize tkinter to create display window
root.geometry=("500x300") #used to set window's width and height
root.resizable(0,0) #Set the fix size of window(in resizeable +ve integer or True can be passed to make window resizeable or 0 or False for non-resizeable) 
root.title("YouTube video downloader")#used to give title to window

Label(root,text="Download your YouTube video",font="arial 20 bold").pack()#Label() widget is used to display text that can't be modified by user
#root is the name of window, text displays title of the label, pack organizes widget in block
#pack geometry manager packs widgets relative to previous widget
link=StringVar()#String type variable that stores video link entered
Label(root,text="Paste Link Here:",font="arial 15 bold").pack()#place(x=160, y=60)
link_enter=Entry(root,width=70,textvariable=link).pack()#place(x=32, y=90)
#Entry() widget is input field is created, width sets width of entry widget, textvariable retrieves value of current text variable
#to entry widget, place() is used for position of the widget

#Function to start downloading
def Downloader():
    url=YouTube(str(link.get()), use_oauth=True, allow_oauth_cache=True)#gets video link from link variable by get()
    video=url.streams.get_highest_resolution()
    video.download("C:")
    Label(root,text="Downloaded",font="arial 15").pack()#place(x=180,y=210)

Button(root,text="Download",font="arial 15 bold",bg="red",padx=2,command=Downloader).pack()#place(x=180,y=150)
#Button used to display button, text displays label, bg sets background color, command used to call function

root.mainloop()
#Executes when we want to run the program
