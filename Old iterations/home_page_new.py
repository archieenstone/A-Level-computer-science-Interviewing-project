import customtkinter
import subprocess
import sys

customtkinter.set_appearance_mode('light') 
customtkinter.set_default_color_theme('blue') 

home_page = customtkinter.CTk()
home_page.title('Interview lab')
home_page.geometry('1200x800')

def interview_setup():
    subprocess.Popen([sys.executable, "interview_setup_set.py"]) 

def open_settings():
    subprocess.Popen([sys.executable, "usersettings.py"]) 

def open_account():
    subprocess.Popen([sys.executable, "user_account.py"]) 

def open_history():
    subprocess.Popen([sys.executable, "user_history.py"]) 

# Creating a frame for the whole page. This will allow scrolling
scrollingframe = customtkinter.CTkFrame(home_page)
scrollingframe.pack(fill="both", expand=1)

# Creating a canvas
canvas = customtkinter.CTkCanvas(scrollingframe)
canvas.pack(side="left", fill="both", expand=1)

# Adding a scrollbar to the canvas 
scrollbar = customtkinter.CTkScrollbar(scrollingframe, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create another frame inside the canvas 
editingframe = customtkinter.CTkFrame(canvas, fg_color="transparent")

# Add that new frame to a window in the canvas 
canvas.create_window((0,0), window=editingframe, anchor="nw")

optionsframe = customtkinter.CTkFrame(editingframe)
optionsframe.pack(side="left",
                  fill="y",
                  anchor="nw")

titleframe = customtkinter.CTkFrame(editingframe,
                                      width=300,
                                      height=100)
titleframe.pack(padx=250,
                pady=0,
                anchor="n")

instructionframe1 = customtkinter.CTkFrame(editingframe)
instructionframe1.pack(pady=30)

textinput1frame = customtkinter.CTkFrame(editingframe,
                                         width=800,
                                         height=700)
textinput1frame.pack(pady=30)
textinput1frame.pack_propagate(False)

textinput2frame = customtkinter.CTkFrame(editingframe,
                                         width=800,
                                         height=700)
textinput2frame.pack(pady=30)
textinput2frame.pack_propagate(False)

welcome_text = customtkinter.CTkLabel(master=instructionframe1,
                                      text="Welcome to Interview Lab, where interview preparation becomes interview success. Are you ready to walk into the room with confidence and leave with the job?")
welcome_text.pack()

accountbuttton = customtkinter.CTkButton(master=optionsframe,
                                                  width=40,
                                                  height=30,
                                                  corner_radius=5,
                                                  text="My account",
                                                  command=open_account)
accountbuttton.pack(padx=20,
                    pady=10)

settingsbuttton = customtkinter.CTkButton(master=optionsframe,
                                                  width=40,
                                                  height=30,
                                                  corner_radius=5,
                                                  text="Settings",
                                                  command=open_settings)
settingsbuttton.pack(padx=20,
                    pady=10)

historybutton = customtkinter.CTkButton(master=optionsframe,
                                                  width=40,
                                                  height=30,
                                                  corner_radius=5,
                                                  text="History",
                                                  command=open_history)
historybutton.pack(padx=20,
                    pady=10)

title_font = customtkinter.CTkFont(size=50,weight="bold",family='Roboto')
title = customtkinter.CTkLabel(master=titleframe,
                               text='Interview lab home',
                               text_color='blue',
                               font=title_font,
                               padx=20,
                               pady=20)                              
title.pack()

instructiontext1 = customtkinter.CTkLabel(master=textinput1frame,
                                          text="Paste your job info, requirements, or links below (Word docs work too—just Ctrl+C and Ctrl+V!). Press Continue to start your interview simulation when you feel you have put enough information in. .",
                                          wraplength=800)
instructiontext1.pack(pady=10,padx=10)

instructiontext11 = customtkinter.CTkLabel(master=textinput1frame,
                                           text="Skip the hassle of re-typing if you want to reuse your text from last session. Scroll down to review or edit it.")
instructiontext11.pack(pady=10,padx=10)

inputnewbox = customtkinter.CTkTextbox(master=textinput1frame,
                                       width=600,
                                       height=500)
inputnewbox.pack(pady=10)

instructiontext2 = customtkinter.CTkLabel(master=textinput2frame,
                                          text="Welcome back! Here's the input from your last practice session. Feel free to update it or add more details, then hit continue when you're ready.",
                                          wraplength=600)
instructiontext2.pack(pady=10,padx=10)

inputreusebox = customtkinter.CTkTextbox(master=textinput2frame,
                                       width=600,
                                       height=500)
inputreusebox.pack(pady=10)

inputreusebutton1 = customtkinter.CTkButton(master=textinput1frame,
                                           width=40,
                                           height=30,
                                           text="Continue",
                                           command=interview_setup)
inputreusebutton1.pack(pady=10)

inputbutton2 = customtkinter.CTkButton(master=textinput2frame,
                                           width=40,
                                           height=30,
                                           text="Continue",
                                           command=interview_setup)
inputbutton2.pack(pady=10)

home_page.mainloop()