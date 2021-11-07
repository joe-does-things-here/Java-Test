from tkinter import* #imports tkinter
import tkinter as tk #allows you to just type 'tk' instead of 'tkinter' when using it
from tkinter import ttk #imports ttk for imporved widget styling

#splash screen --> signin/signup --> dificulty select --> game screen --> leaderboard

def splash_screen():
    global last_frame
    last_frame = "splash_screen"
    button = ttk.Button(splash_screen_frame, text="sign up", command=signup)
    button.grid(row=0,column=0,sticky="W")
    button1 = ttk.Button(splash_screen_frame, text="sign in", command=signin)
    button1.grid(row=0,column=1,sticky="W")
    splash_screen_frame.pack()
    
def signup():
    global current_frame,last_frame
    current_frame = "signup_frame"
    text1 = ttk.Label(signup_frame,text="Enter your username: ")
    text1.grid(row=0,column=0,sticky="W")
    text2 = ttk.Label(signup_frame,text="Enter your password: ")
    text2.grid(row=1,column=0,sticky="W")
    text3 = ttk.Label(signup_frame,text="Enter your email: ")
    text3.grid(row=2,column=0,sticky="W")
    
    textbox = ttk.Entry(signup_frame, textvariable=username)
    textbox.grid(row=0,column=1,sticky="W")
    textbox1 = ttk.Entry(signup_frame, textvariable=password)
    textbox1.grid(row=1,column=1,sticky="W")
    textbox2 = ttk.Entry(signup_frame, textvariable=email)
    textbox2.grid(row=2,column=1,sticky="W")

    button3 = ttk.Button(signup_frame,text="back",command=back)
    button3.grid(row=3,column=0,sticky="W")
    button4 = ttk.Button(signup_frame,text="submit",command=singup_button) #sends to the database
    button4.grid(row=3,column=1,sticky="W")

    splash_screen_frame.pack_forget()
    signup_frame.pack()
    
def signin():
    global current_frame
    current_frame = "signin_frame"
    text4 = ttk.Label(signin_frame,text="Enter your username: ")
    text4.grid(row=0,column=0,sticky="W")
    text5 = ttk.Label(signin_frame,text="Enter your password: ")
    text5.grid(row=1,column=0,sticky="W")
    text6 = ttk.Label(signin_frame,text="Enter your email: ")
    text6.grid(row=2,column=0,sticky="W")

    textbox3 = ttk.Entry(signin_frame, textvariable=username)
    textbox3.grid(row=0,column=1,sticky="W")
    textbox4 = ttk.Entry(signin_frame, textvariable=password)
    textbox4.grid(row=1,column=1,sticky="W")
    textbox5 = ttk.Entry(signin_frame,textvariable=email)
    textbox5.grid(row=2,column=1,sticky="W")
    
    button3 = ttk.Button(signin_frame,text="back",command=back)
    button3.grid(row=3,column=0,sticky="W")
    button4 = ttk.Button(signin_frame,text="submit",command=signin_button) #seperate function that checks against the database
    button4.grid(row=3,column=1,sticky="W")
    
    splash_screen_frame.pack_forget()
    signin_frame.pack()
def dificulty_select():
    print()
def game_frame():
    print()
def leaderboard():
    print()
def signup_button():
    print("submit")
    signin()
def signin_button():
    print()
def back(): #not efficient but it works for now,add a case statement to make it go back to the right screen (global current_frame,last_frame?)
    signup_frame.pack_forget()
    signin_frame.pack_forget()
    splash_screen()
    
root = tk.Tk() #gives the container the identifier "root"
root.title("Spelling test") #gives the root  title

splash_screen_frame = ttk.Frame(root) #creates a new frame that widgets can be added to independently of other frames
signup_frame = ttk.Frame(root)
signin_frame = ttk.Frame(root)
dificulty_select_frame = ttk.Frame(root)
game_frame = ttk.Frame(root)
leaderboard = ttk.Frame(root)

global current_frame, last_frame #creates global variables used to navigate between frames

username = tk.StringVar() #empty string variable that will hold the users username when submitted
password = tk.StringVar() #empty string that will hold the uers password when submitted
email = tk.StringVar() #empty string that will hold the uers email when entered
splash_screen() #displays the splash screen

root.mainloop()
