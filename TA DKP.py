from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import pygame
from pygame import mixer
root=Tk()
root.title("Music Player")
root.geometry("720x560")
pygame.init()
pygame.mixer.init()
pause=False
stop=False

class musicbutton:
    def __init__(self):
        self.music = StringVar()
        self.status = StringVar()
        self.filename=""
    def open(self):
        self.filename=fd.askopenfilename(title="Select File",initialdir="/",filetypes=[("Mp3 Files","*.mp3")])
        filesong=self.filename.split('/')[-1].split('.')[0]
        listnama.append(filesong)
        for i in listnama:
            if i not in listnama_temp:
                listnama_temp.append(filesong)
                playlist.insert(END,i)  
    def play(self):
        if not listnama_temp:
            messagebox.showwarning(title="Warning",message="Tidak ada lagu didalam playlist")
            self.status.set()
        playsong=playlist.get(ACTIVE)
        playsong=f'D:/tes lagu/{playsong}.mp3'
        pygame.mixer.music.load(playsong)
        self.music.set(playlist.get(ACTIVE))
        self.status.set("Playing")
        pygame.mixer.music.play()
    def pause(self):
        global pause
        if not listnama_temp:
            messagebox.showwarning(title="Warning",message="Tidak ada lagu didalam playlist")
            self.status.set()
        if pause == False:
            pygame.mixer.music.pause()
            pause = True
            self.status.set("Pause")
        else:
            pygame.mixer.music.unpause()
            self.status.set("Playing")
            pause = False
    def stop(self):
        if not listnama_temp:
            messagebox.showwarning(title="Warning",message="Tidak ada lagu didalam playlist")
            self.status.set()
        pygame.mixer.music.stop()
        stop=True
        self.status.set("Stopped")
    def prev(self):
        if not listnama_temp:
            messagebox.showwarning(title="Warning",message="Tidak ada lagu didalam playlist")
            self.status.set()
        prevsong=playlist.curselection()
        prevsong=(prevsong[0]+1)%len(listnama_temp)
        prevdirsong=playlist.get(prevsong)
        prevdirsong=f'D:/tes lagu/{prevdirsong}.mp3'
        pygame.mixer.music.load(prevdirsong)
        self.music.set(playlist.get(prevsong))
        self.status.set("Playing")
        pygame.mixer.music.play(loops=0)
        playlist.selection_clear(0,END)
        playlist.activate(prevsong)
        playlist.selection_set(prevsong,last=None)
    def next(self):
        if not listnama_temp:
            messagebox.showwarning(title="Warning",message="Tidak ada lagu didalam playlist")
            self.status.set()
        nextsong=playlist.curselection()
        nextsong=(nextsong[0]+1)%len(listnama_temp)
        nextdirsong=playlist.get(nextsong)
        nextdirsong=f'D:/tes lagu/{nextdirsong}.mp3'
        pygame.mixer.music.load(nextdirsong)
        self.music.set(playlist.get(nextsong))
        self.status.set("Playing")
        pygame.mixer.music.play(loops=0)
        playlist.selection_clear(0,END)
        playlist.activate(nextsong)
        playlist.selection_set(nextsong,last=None)
        
mb=musicbutton()
#Label judul, nama lagu dan status
JudulLabel=Label(text="Judul: ",font=("calibri",14)).place(x=100,y=270)
JudulMusic=Label(textvariable=(mb.music),font=("calibri",14)).place(x=160,y=270)
StatusLabel=Label(text="Status: ",font=("calibri",14)).place(x=100,y=300)
MusicStatus=Label(textvariable=(mb.status),font=("calibri",14)).place(x=160,y=300)
#Button
playbtn=Button(root,text="Play",command=mb.play,font=("calibri",14)).place(x=100,y=380)
pausebtn=Button(text="Pause",command=mb.pause,font=("calibri",14)).place(x=160,y=380)
stopbtn=Button(text="Stop",command=mb.stop,font=("calibri",14)).place(x=230,y=380)
nextbtn=Button(text="Next",command=mb.next,font=("calibri",14)).place(x=290,y=380)
prevbtn=Button(text="Previous",command=mb.prev,font=("calibri",14)).place(x=350,y=380)
#Menu
top_menu=Menu(root)
root.config(menu=top_menu)
add_menu=Menu(top_menu)
top_menu.add_cascade(label="Add",menu=add_menu)
add_menu.add_command(label="Add song",command=mb.open)
#Playlist
scroll=Scrollbar(orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)
playlist=Listbox(root,selectmode=SINGLE,bg="lightslategray",fg="white",font=("calibri",14),width=100)
playlist.config(yscrollcommand=scroll.set)
playlist.pack(pady=20)
listnama=[]
listnama_temp=[]
scroll.config(command=playlist.yview)


mainloop()