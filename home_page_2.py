import customtkinter
import sys
import smtplib
import random
import sqlite3
from email.message import EmailMessage
import subprocess
from PIL import Image
import re

userloggedin_ID = int(sys.argv[1])

db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

customtkinter.set_appearance_mode('light') 
customtkinter.set_default_color_theme('blue') 

home_page = customtkinter.CTk()
home_page.title('Interview lab')
home_page.geometry('1150x800')

colourmode = "light"

def changelightdark(): 
    global colourmode
    if colourmode == "light":
        customtkinter.set_appearance_mode("dark")
        colourmode = "dark"
    else:
        customtkinter.set_appearance_mode("light")
        colourmode = "light"

# Function for displaying whats in the home page 
def home_page_frame():
    def startinterview():
        jobinfo = inputnewbox.get("1.0", "end-1c")
        sql = (f"UPDATE USERS SET recentjobinfo = '{jobinfo}' WHERE id = '{userloggedin_ID}'") # Basically a repeat of the code above for putting the password in now. Added to the SQL statement to ensure that the password and username are entered into the same record 
        cur.execute(sql)
        db.commit()

        subprocess.Popen([sys.executable, "interview_setup_set.py", str(userloggedin_ID)])
        sys.exit()

    global main_frame
    # Clearing everything in the main frame out of memory using the destroy() method then I can pack the new frames/ wdigets into the main frame for this page 
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Creating a frame for the whole page. This will allow scrolling
    scrollingframe = customtkinter.CTkFrame(main_frame)
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
    editingframe = customtkinter.CTkFrame(canvas)

    # Add that new frame to a window in the canvas 
    canvas.create_window((0,0), window=editingframe, anchor="nw", height=2000)

    titleframe = customtkinter.CTkFrame(master=editingframe,
                                        width=1100,
                                        height=125,
                                        fg_color="transparent")
    titleframe.pack(anchor="center")
    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)
    title = customtkinter.CTkLabel(titleframe, text="Interview lab home", font=title_font, text_color="blue")
    title.place(x=10,y=10)

    introphrase = customtkinter.CTkLabel(titleframe,
                                         text="Welcome to Interview Lab, where interview preparation becomes interview success. Are you ready to walk into the room with confidence and leave with a job?",
                                         wraplength=900)
    introphrase.place(x=10,y=100)

    textinput1frame = customtkinter.CTkFrame(master=editingframe,
                                            width=800,
                                            height=450)
    textinput1frame.place(x=50, y=175)
    textinput1frame.pack_propagate(False)

    instructiontext1 = customtkinter.CTkLabel(textinput1frame,
                                            text="Paste your job info, requirements, or links below (Word docs work too—just Ctrl+C and Ctrl+V!). Press Continue to start your interview simulation when you feel you have put enough information in. .",
                                            wraplength=800)
    instructiontext1.pack(pady=10,padx=10)

    inputnewbox = customtkinter.CTkTextbox(textinput1frame,
                                    width=600,
                                    height=300)
    inputnewbox.pack(pady=10)

    btn1 = customtkinter.CTkButton(textinput1frame,
                                   text="Continue",
                                   width=50,
                                   height=30,
                                   command=startinterview)
    btn1.pack(pady=15,padx=350)

    textinput2frame = customtkinter.CTkFrame(master=editingframe,
                                            width=800,
                                            height=450)
    textinput2frame.place(x=50, y=650)
    textinput2frame.pack_propagate(False)

    instructiontext2 = customtkinter.CTkLabel(master=textinput2frame,
                                            text="Welcome back! Here's the input from your last practice session. Feel free to update it or add more details, then hit continue when you're ready.",
                                            wraplength=700)
    instructiontext2.pack(pady=10,padx=10)

    inputreusebox = customtkinter.CTkTextbox(textinput2frame,
                                    width=600,
                                    height=300)
    inputreusebox.pack(pady=10)

    btn2 = customtkinter.CTkButton(textinput2frame,
                                   text="Continue",
                                   width=50,
                                   height=30)
    btn2.pack(padx=350, pady=15)

def account_frame():
    global main_frame
    global userloggedin_ID
    global enternewresetpassword

    # Clearing everything in the main frame out of memory using the destroy() method then I can pack the new frames/ wdigets into the main frame for this page 
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Creating a frame for the whole page. This will allow scrolling
    scrollingframe = customtkinter.CTkFrame(main_frame)
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
    editingframe = customtkinter.CTkFrame(canvas)

    # Add that new frame to a window in the canvas 
    canvas.create_window((0,0), window=editingframe, anchor="nw", height=2000)

    def email_key():
        global currentsecuritycode
        cur.execute(f"SELECT email FROM USERS where id = {userloggedin_ID}")
        result = cur.fetchone()
        useremail = result[0]

        codegenerated = generate_email_code()
        currentsecuritycode = codegenerated
        
        msg = EmailMessage()
        msg.set_content(f'Your code from Interview lab to reset your password is {codegenerated}')

        msg['Subject'] = 'Password reset code from interview lab'
        msg['From'] = 'interviewlabcommunications@gmail.com'
        msg['To'] = f'{useremail}'

        sender_password = 'ejkm dimq vdoi ktmd'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('interviewlabcommunications@gmail.com', sender_password)
        server.send_message(msg)
        print('email sucessfully sent')

    def generate_email_code():
        global currentsecuritycode
        digits = "0123456789"
        otp = ""
        for i in range(6):
            otp += random.choice(digits)
            i=i+1
        return otp

    def resetpassword():
        enternewresetpassword()

    def updateusername():
        newusername = updateusernameentry.get()
        print(newusername)
        print(userloggedin_ID)
        sqlite3_add = f"UPDATE USERS SET username = '{newusername}' WHERE id = {userloggedin_ID}"
        cur.execute(sqlite3_add) 
        db.commit()
        print('username changed')
        lengthofusername = len(newusername)
        updateusernameentry.delete(0, lengthofusername)
        subprocess.Popen([sys.executable, "username changed update.py"]) 
    
    def logoutcmd():
        subprocess.Popen([sys.executable, "login page better attempt.py"]) 
        sys.exit()

    titleframe = customtkinter.CTkFrame(master=editingframe,
                                        width=1100,
                                        height=125,
                                        fg_color="transparent")
    titleframe.pack(anchor="center")
    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)
    title = customtkinter.CTkLabel(titleframe, text="Account", font=title_font, text_color="blue")
    title.place(x=10,y=10)

    introphrase = customtkinter.CTkLabel(titleframe,
                                         text="In this page you can change/ update your account details such as your username, password or email address",
                                         wraplength=900)
    introphrase.place(x=10,y=100)

    accountmainframe = customtkinter.CTkFrame(master=editingframe,
                                        width=1100,
                                        height=500,
                                        fg_color="transparent")
    accountmainframe.place(x=0,y=130)

    updateusernameinstruct = customtkinter.CTkLabel(accountmainframe, text="Want to change your username? Enter a new user name below to update it.")
    updateusernameinstruct.place(x=10,y=20)

    updateusernameentry = customtkinter.CTkEntry(accountmainframe, width=200, height=50)
    updateusernameentry.place(x=10,y=50)

    updateusernamebtn = customtkinter.CTkButton(accountmainframe, text="Update user name", width=100, height=30, command=updateusername)
    updateusernamebtn.place(x=10, y=110)

    updatepasswordinstruct = customtkinter.CTkLabel(accountmainframe, text="Want to change your password? Click 'Email security key' and a 6 digit code will be sent to your email attached to this account. Enter the security key in the entry box below then you can update your password in the pop out window.",
                                                    wraplength=900,
                                                    justify="left")
    updatepasswordinstruct.place(x=10,y=180)

    updatepasswordbtn = customtkinter.CTkButton(accountmainframe, text="Email security key", width=100, height=30, command=email_key)
    updatepasswordbtn.place(x=10, y=220)

    entersecuritykey = customtkinter.CTkEntry(accountmainframe, width=200, height=50)
    entersecuritykey.place(x=10, y=270)

    emailentersecuritykeybtn = customtkinter.CTkButton(accountmainframe, width=100, height=30, text="Enter code", command=resetpassword)
    emailentersecuritykeybtn.place(x=220, y=280)

    logoutbtn_font = customtkinter.CTkFont(size=20)

    logout = customtkinter.CTkButton(accountmainframe,
                                     width=200,
                                     height=60,
                                     text="Log out",
                                     font=logoutbtn_font,
                                     command=logoutcmd)
    logout.place(x=10, y=340)

def settings_frame():
    global main_frame
    # Clearing everything in the main frame out of memory using the destroy() method then I can pack the new frames/ wdigets into the main frame for this page 
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Creating a frame for the whole page. This will allow scrolling
    scrollingframe = customtkinter.CTkFrame(main_frame)
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
    editingframe = customtkinter.CTkFrame(canvas)

    # Add that new frame to a window in the canvas 
    canvas.create_window((0,0), window=editingframe, anchor="nw", height=2000)

    titleframe = customtkinter.CTkFrame(master=editingframe,
                                        width=1100,
                                        height=125,
                                        fg_color="transparent")
    titleframe.pack(anchor="center")
    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)
    title = customtkinter.CTkLabel(titleframe, text="Settings", font=title_font, text_color="blue")
    title.place(x=10,y=10)

    introphrase = customtkinter.CTkLabel(titleframe,
                                         text="In this page you can adjust your settings for Interview Lab.",
                                         wraplength=900)
    introphrase.place(x=10,y=100)

    settingsmainframe = customtkinter.CTkFrame(master=editingframe,
                                        width=1100,
                                        height=125,
                                        fg_color="transparent")
    settingsmainframe.place(x=0,y=130)

    lightdarkintruction = customtkinter.CTkLabel(settingsmainframe, text="Fancy changing to light or dark mode? Just click the button below.")
    lightdarkintruction.place(y=10,x=10)

    light_dark = customtkinter.CTkButton(settingsmainframe, text="Change Light/dark", command=changelightdark)
    light_dark.place(y=50,x=10)

def history_frame():
    # Clearing everything in the main frame out of memory using the destroy() method then I can pack the new frames/ wdigets into the main frame for this page 
    for widget in main_frame.winfo_children():
        widget.destroy()

    titleframe = customtkinter.CTkFrame(master=main_frame,
                                        width=1100,
                                        height=125,
                                        fg_color="transparent")
    titleframe.pack(anchor="center")
    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)
    title = customtkinter.CTkLabel(titleframe, text="History", font=title_font, text_color="blue")
    title.place(x=10,y=10)

    introphrase = customtkinter.CTkLabel(titleframe,
                                         text="In this page you can read about your feedback from your most recent interview practice. Want your feedback from interview pratices longer ago - remember they have all been emailed to you!.",
                                         wraplength=900)
    introphrase.place(x=10,y=100)

def enternewresetpassword(): 
    for widget in main_frame.winfo_children():
       widget.destroy()

    bottomframe = customtkinter.CTkFrame(main_frame,
                                         width=500,
                                         height=150)
    bottomframe.place(x=250,y=300)
    headerframe = customtkinter.CTkFrame(main_frame,
                                     width=800,
                                     height=140)
    headerframe.place(x=10,y=10)

    def resetpassword():
        global userloggedin_ID
        global loginpage
        global password11
        global password22

        password11 = password1.get()
        password22 = password2.get()

        if password11 == password22:
            if len(password11) >= 8: # Checking the password is at least 8 characters long
                number = any(char.isdigit() for char in password11) # Searches for any numerical digits within the password. Returns True or False (boolean) if there are digits or not 
                if number:
                    regex = re.compile('[@_!#$%^&*()<>?/}{~:]')
                    if regex.search(password11) == None:
                        subprocess.Popen([sys.executable, "error message for password.py"])
                    else: 
                        print('passwords match')
                        x = f"UPDATE USERS SET password = '{password11}' WHERE id = {userloggedin_ID}"
                        cur.execute(x) 
                        db.commit()
                        print('password changed')

                        cur.execute(f"SELECT username FROM USERS WHERE id = {userloggedin_ID}")
                        usernamereturn = cur.fetchone()
                        if usernamereturn == None:
                            sys.exit()
                        else:
                            username = usernamereturn[0]
                            print(username)

                            msg = EmailMessage()
                            msg.set_content(f'''
Hello {username},
                    
This is just a quick update to let you know that your password has been changed. If this wasn't you changed it contact us immediately (email address below) and change your password. 

Get ready for your interview:
- Practice makes perfect! Simulate real interview scenarios on our interactive platform. The more details you provide about your target job, the better the interview and feedback will be.                   
- Receive personalized feedback. This will be emailed to this email address after each interview practice. Analyze your performance and identify areas for improvement.
- Build your confidence. Walk into your next interview feeling prepared and ready to impress!

We are excited to help you on your journey to landing your dream job. Feel free to explore the platform and do not hesitate to reach out if you have any questions or concerns. 
Please send an email to interviewlabcommunications@gmail.com with any questions or queries.

Happy interviewing!
Best regards,
Interview lab team''')

                            msg['Subject'] = 'Password changed'
                            msg['From'] = 'interviewlabcommunications@gmail.com'

                            cur.execute(f"SELECT email FROM USERS WHERE id = {userloggedin_ID}")
                            x = cur.fetchone()
                            emailtosend = x[0]

                            msg['To'] = emailtosend

                            sender_password = 'ejkm dimq vdoi ktmd'

                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login('interviewlabcommunications@gmail.com', sender_password)
                            server.send_message(msg)
                            print('email sucessfully sent')

                            subprocess.Popen([sys.executable, "password changed sucess.py"])

                            account_frame()

                else:
                    subprocess.Popen([sys.executable, "error message for password.py"])
            else: 
                subprocess.Popen([sys.executable, "error message for password.py"])
        else: 
            print('passwords do not match')
            subprocess.Popen([sys.executable, "error message for passwords unmatched.py"]) # Opens to the home page and passes the variable userloggedin_id into the home page script to ensure the home page can be specific to the user

    instruction = customtkinter.CTkLabel(headerframe,
                                        text='To reset your password please enter a new password in the first entry then re-enter the password again in the second entry box',
                                        fg_color="transparent")
    instruction.place(x=20,y=80)

    password1 = customtkinter.CTkEntry(master=bottomframe,
                                    placeholder_text="Please enter your new password here",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    password1.place(x=0,y=0)

    password2 = customtkinter.CTkEntry(master=bottomframe,
                                    placeholder_text="Now re-enter your password here",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    password2.place(x=0,y=50)

    reset_password = customtkinter.CTkButton(master=bottomframe,
                                            width=300,
                                            height=40,
                                            border_width=0,
                                            corner_radius=8,
                                            text="Reset password",
                                            command=resetpassword)
    reset_password.place(x=100,y=110)

    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)

    header = customtkinter.CTkLabel(headerframe,
                                    text="Password reset",
                                    font=title_font,
                                    text_color="blue",
                                    fg_color="transparent")
    header.place(x=20,y=10)

# Creating the options bar to switch between the different frames 
options_frame = customtkinter.CTkFrame(home_page)
options_frame.pack(side="left")
options_frame.pack_propagate(False) # Prevents the frame from shrinking depending on what it has got in it
options_frame.configure(width=150,height=800)

main_frame = customtkinter.CTkFrame(home_page, fg_color="transparent")
main_frame.pack(side="left")
main_frame.pack_propagate(False)
main_frame.configure(width=2000,height=800)

introlabelprompt = customtkinter.CTkLabel(main_frame, text="To get started please select from one of the options on the left handside of the window!")
introlabelprompt.place(x=50,y=100)

introlabelprompt = customtkinter.CTkLabel(main_frame, text="If you have just finished an interview practice session then head over to the history section on the left handside of the screen to review your feedback. Your feedback has also been emailed to you.", wraplength=800)
introlabelprompt.place(x=50,y=150)

logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),
size=(140,140))

logoframe = customtkinter.CTkFrame(options_frame,
                                width=140,
                                height=140)
logoframe.place(x=5,y=5)

imagelabel = customtkinter.CTkLabel(logoframe,
                                    image=logoimage,
                                    text="")
imagelabel.place(x=0,y=0)

home_pagebtn = customtkinter.CTkButton(options_frame, text="Home page", width=100,height=30, command=home_page_frame)
home_pagebtn.place(x=25,y=190)

accountbtn = customtkinter.CTkButton(options_frame, text="Your account", width=100,height=30, command=account_frame)
accountbtn.place(x=25,y=240)

settingsbtn = customtkinter.CTkButton(options_frame, text="Settings", width=100,height=30, command=settings_frame)
settingsbtn.place(x=25,y=290)

historybtn = customtkinter.CTkButton(options_frame, text="History", width=100,height=30, command=history_frame)
historybtn.place(x=25,y=340)

home_page.mainloop()

