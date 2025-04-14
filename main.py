import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Creating window
window = tk.Tk()
window.title('Automatic Power-Off')
window.geometry('400x250')
window.configure(background='black')
window.iconbitmap('shutdown-icon.ico')

# Send shutdown commands method
def shutdownCommand(time):
    seconds = secondsConverter(time)
    os.system(f"shutdown -s -t {seconds}")

# Convert minutes -> seconds
def secondsConverter(minutes):
    return minutes * 60

# Creating title label
labelTitle = Label(window,
                text='Automatic shutdown',
                background='black',
                fg='red',
                font=('Times New Roman', 15)).place(relx=0.3, rely=0.02)

# Creating buttons
shutdownOneMinute = Button(window,
                                width=10,
                                height=4,
                                text='1 minute',
                                bg='#959595',
                                command=lambda: shutdownCommand(1)).place(x=50, y=40)
shutdownFiveMinutes = Button(window,
                                width=10,
                                height=4,
                                text='5 minutes',
                                bg='#b4b4b4',
                                command=lambda: shutdownCommand(5)).place(x=150, y=40)
shutdownFifteenMinutes = Button(window,
                                width=10,
                                height=4,
                                text='15 minutes',
                                bg='#c5c5c5',
                                command=lambda: shutdownCommand(15)).place(x=250, y=40)
shutdownHalfHour = Button(window,
                                width=10,
                                height=4,
                                text='30 minutes',
                                bg='#d5d5d5',
                                command=lambda: shutdownCommand(30)).place(x=50, y=140)
shutdownOneHour = Button(window,
                                width=10,
                                height=4,
                                text='1 hour',
                                bg='#e5e5e5',
                                command=lambda: shutdownCommand(60)).place(x=150, y=140)
shutdownTwoHours = Button(window,
                                width=10,
                                height=4,
                                text='2 hours',
                                bg='#f2efef',
                                command=lambda: shutdownCommand(120)).place(x=250, y=140)

window.mainloop()

