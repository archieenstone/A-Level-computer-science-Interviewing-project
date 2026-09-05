import customtkinter
import sqlite3
import tkinter
import os
import sys
import subprocess
from PIL import Image

connection = sqlite3.connect('Interview_lab_database.db') #creating database file
cursor = connection.cursor() #create cursor function to use the information in the table

customtkinter.set_appearance_mode('light') #set light mode 
customtkinter.set_default_color_theme('blue') #set colour scheme to blue

home_page = customtkinter.CTk() #create the output app
home_page.title('Interview lab') #set a title for the program window 
home_page.geometry('1200x800')

optionsframe = customtkinter.CTkFrame(home_page)
optionsframe.pack(side="left",
                  fill="y",
                  anchor="nw")

titleframe = customtkinter.CTkFrame(home_page,
                                      width=300,
                                      height=100)
titleframe.pack(padx=300,
                pady=0)

instructionframe1 = customtkinter.CTkFrame(home_page)
instructionframe1.pack(pady=30)

textinput1frame = customtkinter.CTkFrame(home_page)
textinput1frame.pack(pady=30)

textinput2frame = customtkinter.CTkFrame(home_page)
textinput2frame.pack()

title_font = customtkinter.CTkFont(size=50,weight="bold",family='Roboto')

title = customtkinter.CTkLabel(master=titleframe,
                               text='Interview lab home',
                               text_color='blue',
                               font=title_font,
                               padx=20,
                               pady=20)                              
title.pack()

welcome_text = customtkinter.CTkLabel(master=instructionframe1,
                                      text="Welcome to Interview Lab, where interview preparation becomes interview success. Are you ready to walk into the room with confidence and leave with the job?")
welcome_text.pack()

instructiontext1 = customtkinter.CTkLabel(master=textinput1frame,
                                          text="Paste your job info, requirements, or links below (Word docs work too—just Ctrl+C and Ctrl+V!). Skip the hassle of re-typing if you want to reuse your text from last session. Scroll down to review or edit it. Press Continue to start your interview simulation when you feel you have put enough information in. .",
                                          wraplength=800)
instructiontext1.pack()

inputnewbox = customtkinter.CTkTextbox(master=textinput1frame,
                                       width=600,
                                       height=100)
inputnewbox.pack(pady=50)

instructiontext2 = customtkinter.CTkLabel(master=textinput2frame,
                                          text="Welcome back! Here's the input from your last practice session. Feel free to update it or add more details, then hit continue when you're ready.")
instructiontext2.pack()

inputreusebox = customtkinter.CTkTextbox(master=textinput2frame,
                                       width=600,
                                       height=100)
inputreusebox.pack(pady=50)

accountbuttton = customtkinter.CTkButton(master=optionsframe,
                                                  width=40,
                                                  height=30,
                                                  corner_radius=5,
                                                  text="My account")
accountbuttton.pack(padx=20,
                    pady=10)

settingsbuttton = customtkinter.CTkButton(master=optionsframe,
                                                  width=40,
                                                  height=30,
                                                  corner_radius=5,
                                                  text="Settings")
settingsbuttton.pack(padx=20,
                    pady=10)

historybutton = customtkinter.CTkButton(master=optionsframe,
                                                  width=40,
                                                  height=30,
                                                  corner_radius=5,
                                                  text="History")
historybutton.pack(padx=20,
                    pady=10)

home_page.mainloop()