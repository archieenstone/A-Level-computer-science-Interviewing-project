import customtkinter
import sys
import subprocess
import os, signal

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

testapp = customtkinter.CTk()
testapp.title('Agent start stop app') 
testapp.geometry('400x200') 

proc = None

def start():
    global proc
    if proc is None:
        proc = subprocess.Popen(["python", "agent.py", "start"], start_new_session=True)

def stop():
    global proc
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

    print('test gone through')
    proc.terminate()  
    try:
        proc.wait(timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()   

startbtn = customtkinter.CTkButton(testapp, text="start", command=start)
startbtn.pack(pady=10,padx=10)

stopbtn = customtkinter.CTkButton(testapp, text="stop", command=stop)
stopbtn.pack(pady=10,padx=10)

testapp.mainloop()
