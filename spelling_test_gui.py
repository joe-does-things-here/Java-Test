from tkinter import*
import tkinter as tk #allows you to just type 'tk' instead of 'tkinter' when using it
from tkinter import ttk #imports ttk for imporved styling

#TODO create all the needed frames,have ways of calling them all, make sure they don't overlap
#splash screen --> signin/signup --> dificulty select --> game screen --> leaderboard

def splash_screen():
    splash_screen_frame = ttk.Frame(root)
    button = ttk.Button(splash_screen_frame, text="sign up", command=signup)
    button.grid(row=0,column=0,sticky="W")
    button1 = ttk.Button(splash_screen_frame, text="sign in", command=signin)
    button1.grid(row=0,column=1,sticky="W")
    splash_screen_frame.pack()
    
def signup():
    signup_frame = ttk.Frame(root)
    text1 = ttk.Label(signup_frame,text="Enter your username: ")
    text1.grid(row=0,column=0,sticky="W")
    splash_screen_frame.destroy() #this doesn't work?
    signupframe.pack()
def signin():
    print()
def dificulty_select():
    print()
def game_frame():
    print()
def leaderboard():
    print()

root = tk.Tk() #gives the container the identifier "root"
root.title("Spelling test") #gives the root  title
splash_screen() #displays the splash screen
root.mainloop()
