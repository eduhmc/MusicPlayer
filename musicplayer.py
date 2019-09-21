""" import modules """
import pygame
import tkinter as tkr
import os

""" create window """
player = tkr.Tk() 

""" Edit window """
player.title("Audio Player 1")
player.geometry("205x340")

""" playlist directory """
os.chdir("/Users/eduardohuertamercado/Documents/mp3")

""" get song """

songlist = os.listdir()

""" playlist input"""
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
	pos = 0
	playlist.insert(pos, item)
	pos = pos + 1
""" pygame inits """
pygame.init()
pygame.mixer.init()

""" action event """
def Play():
	
	pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
	var.set(playlist.get(tkr.ACTIVE))
	pygame.mixer.music.play()

def ExitPlayer():
	pygame.mixer.music.stop()

""" register buttons """
button1 = tkr.Button(player,width=5 ,height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)


""" song name """
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)


""" Place widgets """
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
playlist.pack(fill="both", expand="yes")


""" activate """
player.mainloop()



