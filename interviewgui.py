import sys
import customtkinter
import subprocess
from tkinter_webcam import webcam
from PIL import Image
import os
import sqlite3

userloggedin_ID = str(sys.argv[1])
agent_action = None

if os.path.exists("useridloggedin.txt"):
    os.remove("useridloggedin.txt")
    with open("useridloggedin.txt", "w") as f:
        f.write(userloggedin_ID)
else:
    with open("useridloggedin.txt", "w") as f:
        f.write(userloggedin_ID)

interviewgui = customtkinter.CTk()
interviewgui.title('Interview lab')
interviewgui.geometry('1200x700')

db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

cur.execute(f"SELECT lengthofinterview FROM USERS where id = {userloggedin_ID}")
result = cur.fetchone()
timeofinterview = result[0]

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

def stopagentaftertime():
    global agent_action
    print('time finished... stopping agent then redirecting you to feedback page')
    subprocess.Popen([sys.executable, "feedbacktest.py", str(agent_action)])
    print('feedback page opened')
    subprocess.run(["taskkill", "/F", "/T", "/PID", str(agent_action.pid)])
    print('agent terminated')
    sys.exit()
    
def updatetimer():
    global hours, minutes, seconds
    global timeofinterview
    global agent_action

    if timeofinterview == "10mins":
        timetostop = 10
    elif timeofinterview == "15mins":
        timetostop = 15
    elif timeofinterview == "20mins":
        timetostop = 20
    elif timeofinterview == "30mins":
        timetostop = 30
    elif timeofinterview == "45mins":
        timetostop = 45
    elif timeofinterview == "60mins":
        timetostop = 60

    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == timetostop:
        stopagentaftertime()
    if minutes == 60:
        hours =+ 1
        minutes = 0

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    timerdisplay.configure(text = hours_string + ':' + minutes_string + ':' + seconds_string)
    
    timerdisplay.after(10, updatetimer)

def connecttoagent():        
    global btntext1
    global agent_action
    global userloggedin_ID
    global running

    if btntext1 == "Start interview":
        btntext1 = "End interview"
        starttimerbtn.configure(text = "End interview")
        if os.path.exists("conversation_log.txt"):
            os.remove("conversation_log.txt")
        agent_action = subprocess.Popen(["uv", "run", "agent.py", "console"])
        starttimer()

        x = agent_action.pid
        with open("agentpid.pid", "w") as f:
            f.write(str(x))
        print('interview assistant lauching...')
    elif btntext1 == "End interview":
        print('ending interview warning message appearing')
        subprocess.Popen([sys.executable, "warningclosinginterviewearly.py", str(userloggedin_ID)])

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
