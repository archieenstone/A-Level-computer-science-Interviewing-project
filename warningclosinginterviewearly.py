import customtkinter
import win32api
import win32gui
import subprocess
import sys
import os
import signal

agent_action = str(sys.argv[1])

userloggedin_ID = 0
with open("useridloggedin.txt") as f:
    userloggedin_ID = (f.read().strip())
    f.close()

with open("guipid.pid", "r") as f:
    mainwindowpid = (f.read().strip()) # .strip() function removes the blank space at the end of the collection of numbers
os.remove("guipid.pid")

with open("agentpid.pid", "r") as f:
    agentrunpid = (f.read().strip()) # .strip() function removes the blank space at the end of the collection of numbers
os.remove("agentpid.pid")

customtkinter.set_appearance_mode('light') 
customtkinter.set_default_color_theme('blue') 

u_error_page = customtkinter.CTk() 
u_error_page.title('Ending interview early') 
u_error_page.geometry('600x400')

def closeinterviewearly():
    global agent_action
    global agentrunpid
    global mainwindowpid
    print('Closing interview early...')
    print('Opening feedback page...')
    subprocess.Popen([sys.executable, "feedbacktest.py", str(userloggedin_ID)])
    print('Feedback page opened')
    subprocess.run(["taskkill", "/F", "/T", "/PID", str(agentrunpid)])

    os.kill(int(mainwindowpid), signal.SIGTERM) # https://zetcode.com/python/os-kill/
    sys.exit()

def returntointerview():
    sys.exit()

title_font = customtkinter.CTkFont(size=40,weight="bold",family='Roboto', underline=True)

title = customtkinter.CTkLabel(u_error_page,
                               text="End interview early?",
                               text_color="blue", 
                               font=title_font)
title.place(x=50,y=30)


displaymessage = customtkinter.CTkLabel(u_error_page,
                                        wraplength=500,
                                        text="You haven't completed the full duration of your interview yet. Are you sure you want to exit early? If you choose to end now, your progress will be saved and you will still receive feedback. However, we highly recommend completing the session length you originally selected.")
displaymessage.place(x=50,y=100)

yesend = customtkinter.CTkButton(u_error_page,
                               width=300,
                               height=40,
                               border_width=0,
                               corner_radius=8,
                               command = closeinterviewearly,
                               text="End early",
                               fg_color="skyblue1",
                               text_color="grey")
yesend.place(x=150,y=250)

noend = customtkinter.CTkButton(u_error_page,
                               width=300,
                               height=40,
                               border_width=0,
                               corner_radius=8,
                               command = returntointerview,
                               text="Continue interview")
noend.place(x=150,y=300)

u_error_page.mainloop()