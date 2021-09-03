from tkinter import *
from pytube import YouTube
win=Tk()
win.geometry('500x300')
win.resizable(0,0)
win.title('youtube downloader')

Label(win,text='1.copy the link', font='arial 20 bold').place(relx=0.05,y=10)
Label(win, text='2.paste the link here:',font='arial 20 bold').place(relx=0.05,y=60)
link=StringVar()
link_paste=Entry(win,textvariable=link, font='arial 15').place(relx=0.05,y=110,height=30, width=450)
def downloader():
	url=YouTube(str(link.get()))
	video=url.streams.first()
	video.download()
	Label(win,text='successfully downloaded',font='arial 15').place(x=180,y=220)

Button(win,text='DOWNLOAD',font='Verdana 15 bold',bg='orange',padx=2,command=downloader).place(x=180,y=180)
win.mainloop()
















'''useful links:
https://dev.to/larymak/beginner-python-project-4-youtube-video-downloader-4gpj
https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/
https://www.geeksforgeeks.org/create-gui-for-downloading-youtube-video-using-python/
https://data-flair.training/blogs/python-youtube-downloader-with-pytube/
https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
'''

