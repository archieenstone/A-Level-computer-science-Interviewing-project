import customtkinter
import smtplib
import sqlite3
import subprocess
import sys
from email.message import EmailMessage
import random

emailcode = 0 

connection = sqlite3.connect('Interview_lab_database.db') #creating database file
cursor = connection.cursor() #create cursor function to use the information in the table

customtkinter.set_appearance_mode('light') 
customtkinter.set_default_color_theme('blue') 

page = customtkinter.CTk() 
page.title('Reset password') 
page.geometry('500x400')  

def checkcode():
    global emailcode
    codeentered = codesubmit.get()
    emailinput = emailenter.get()
    if codeentered == emailcode:
        subprocess.Popen([sys.executable, "reset_password_popout from login.py", str(emailinput)]) 
        sys.exit()
    else:
        subprocess.Popen([sys.executable, "error_reset_password_code from forgot email.py"]) 

def emailcodeandresetopen():
    global emailcode
    def generate_email_code():
        global currentsecuritycode
        digits = "0123456789"
        otp = ""
        for i in range(6):
            otp += random.choice(digits)
            i=i+1
        return otp
    
    emailinput = emailenter.get()
    cursor.execute(f"SELECT email FROM USERS where email = '{emailinput}'")
    checkifexists = cursor.fetchone()
    if checkifexists == None:
        subprocess.Popen([sys.executable, "error message for email not recognised.py"]) 
    else:
        codegenerated = generate_email_code()
        emailcode = codegenerated

        msg = EmailMessage()
        msg.set_content(f'Your code from Interview lab to reset your password is {codegenerated}')

        msg['Subject'] = 'Password reset code from interview lab'
        msg['From'] = 'interviewlabcommunications@gmail.com'
        msg['To'] = f'{emailinput}'

        sender_password = 'ejkm dimq vdoi ktmd'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('interviewlabcommunications@gmail.com', sender_password)
        server.send_message(msg)
        print('email sucessfully sent')

topframe = customtkinter.CTkFrame(page,
                                  width=500,
                                  height=50)
topframe.place(x=0,y=0)

secondframe = customtkinter.CTkFrame(page,
                                     width=300,
                                     height=100)
secondframe.place(x=100,y=60)

thirdframe = customtkinter.CTkFrame(page,
                                    width=300,
                                    height=100)
thirdframe.place(x=100,y=220)
                                     
displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=500,
                                        text='To reset your password please enter your email address below. A security key will be sent to it which you can then enter on the next page to reset your password')
displaymessage.place(x=10,y=10)

emailenter = customtkinter.CTkEntry(secondframe,
                                placeholder_text="Please enter your email here.",
                                placeholder_text_color="Light blue",
                                width=300,
                                height=50,
                                border_width=2,
                                corner_radius=30)
emailenter.pack(padx=10,pady=10)

sendcodebtn = customtkinter.CTkButton(secondframe,
                                        width=150,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8,
                                        text="Send a password reset code to email",
                                        command=emailcodeandresetopen)
sendcodebtn.pack(pady=20)

codesubmit = customtkinter.CTkEntry(thirdframe,
                                placeholder_text="Please the code here once you have recieved it in your email.",
                                placeholder_text_color="Light blue",
                                width=300,
                                height=50,
                                border_width=2,
                                corner_radius=30)
codesubmit.pack(padx=10,pady=10)

submitcodebtn = customtkinter.CTkButton(thirdframe,
                                        width=150,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8,
                                        text="Submit code",
                                        command=checkcode)
submitcodebtn.pack(pady=20)


page.mainloop()