import sys
import customtkinter
import subprocess
from tkinter_webcam import webcam
from PIL import Image
import os

userloggedin_ID = str(sys.argv[1])


if os.path.exists("useridloggedin.txt"):
    os.remove("useridloggedin.txt")
    with open("useridloggedin.txt", "a") as f:
        f.write(userloggedin_ID)
else:
    with open("useridloggedin.txt", "a") as f:
        f.write(userloggedin_ID)

interviewgui = customtkinter.CTk()
interviewgui.title('Interview lab')
interviewgui.geometry('1200x700')

running = False
hours, minutes, seconds = 0,0,0
btntext1 = "Start interview"

def helpinstructionsopen():
    subprocess.Popen([sys.executable, "helpinstructions.py"]) 

def starttimer():
    global running
    if not running:
        updatetimer()
        running = True
    
def updatetimer():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours =+ 1
        minutes = 0

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    timerdisplay.configure(text = hours_string + ':' + minutes_string + ':' + seconds_string)
    
    timerdisplay.after(1000, updatetimer)

def connecttoagent():
    global btntext1

    if btntext1 == "Start interview":
        starttimerbtn.configure(text = "End interview")
        if os.path.exists("conversation_log.txt"):
            os.remove("conversation_log.txt")
        subprocess.Popen(["uv", "run", "agent.py", "console"])
        starttimer()
        print('interview assistant lauching...')
    else:
        None
        # Here I need to insert some code to shut down the AI agent from running in the command line powershell. 

cmdframe = customtkinter.CTkFrame(interviewgui,
                                  width=1200,
                                  height=60)
cmdframe.place(x=0,y=0)

cameraframe = customtkinter.CTkFrame(interviewgui,
                                     width=1000,
                                     height=640)
cameraframe.place(x=100,y=60)

timerfont = customtkinter.CTkFont(size=30)

timerdisplay = customtkinter.CTkLabel(cmdframe, width=50,height=40, text='00:00:00', font=timerfont)
timerdisplay.place(x=10,y=10)    

starttimerbtn = customtkinter.CTkButton(cmdframe, width=100, height=50, text="Start interview", command=connecttoagent)
starttimerbtn.place(x=1095,y=5)

logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),size=(50,50))

photolabel = customtkinter.CTkLabel(cmdframe, image=logoimage, text="")
photolabel.place(x=280,y=5)

titlefont = customtkinter.CTkFont(size=45,weight="bold")

titletext = customtkinter.CTkLabel(cmdframe,text="Interview lab connect", text_color="blue", font=titlefont)
titletext.place(x=350,y=5)

questionmark = customtkinter.CTkImage(light_image=Image.open("helpimage.png"),size=(70,50))

helpbtn = customtkinter.CTkButton(interviewgui, image=questionmark, text="", command=helpinstructionsopen, width=70, height=50)
helpbtn.place(x=1100,y=630)

interviewgui.mainloop()
