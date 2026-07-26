import customtkinter
import sqlite3
import sys
import subprocess
import validators
from email.message import EmailMessage
import smtplib
import random
from PIL import Image
import re

currentloggedinID = 0
user_name = 0 
pass_word = 0 
emailcode = 0
useremailtochangepassword = " "

connection = sqlite3.connect('Interview_lab_database.db') #creating database file
cursor = connection.cursor() #create cursor function to use the information in the table

#creating a table for storing user information
command1 = ('''
    CREATE TABLE IF NOT EXISTS
    USERS(id integer primary key autoincrement, username Text, email Text, password Text, recentjobinfo Text, questiondomainsselected Text, lengthofinterview Text, interviewerpersona Text, difflevel Text, lastinterviewtranscript Text, lastfeedbacksession Text)
              ''')
cursor.execute(command1)

customtkinter.set_appearance_mode('light') #set light mode 
customtkinter.set_default_color_theme('blue') #set colour scheme to blue

login_page = customtkinter.CTk() #create the output app
login_page.title('User login') #set a title for the program window 
login_page.geometry('1200x500')  # Set window size


def forgot_password(): 
    global login_page
    global loginpage
    global emailcodeandresetopen
    global emailcode

    for widget in login_page.winfo_children():
       widget.destroy()

    def checkcode():
        global emailcode
        global emailinput

        codeentered = codesubmit.get()
        emailinput = emailenter.get()

        if codeentered == emailcode:
            enternewresetpassword()
        else:
            subprocess.Popen([sys.executable, "error_reset_password_code from forgot password.py"]) 

    def emailcodeandresetopen():
        global emailcode
        global useremailtochangepassword

        def generate_email_code():
            digits = "0123456789"
            otp = ""
            for i in range(6):
                otp += random.choice(digits)
                i=i+1
            return otp
        
        emailinput = emailenter.get()
        useremailtochangepassword=emailinput 
        print(emailinput)

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

    topframe = customtkinter.CTkFrame(login_page,
                                    width=800,
                                    height=150)
    topframe.place(x=200,y=10)
    secondframe = customtkinter.CTkFrame(login_page,
                                        width=500,
                                        height=210)
    secondframe.place(x=350,y=180)
    endframe = customtkinter.CTkFrame(login_page,
                                      width=200,
                                      height=30)
    endframe.place(y=430,x=500)

    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)

    header = customtkinter.CTkLabel(topframe,
                                    text="Forgotten password reset",
                                    font=title_font,
                                    text_color="blue")
    header.place(x=10,y=10)   

    displaymessage = customtkinter.CTkLabel(master=topframe,
                                            wraplength=760,
                                            text='To reset your password please enter your email address below. A security key will be sent to it which you can then enter on the next page to reset your password.')
    displaymessage.place(x=10,y=90)

    emailenter = customtkinter.CTkEntry(secondframe,
                                    placeholder_text="Please enter your email here.",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    emailenter.place(x=0,y=0)

    sendcodebtn = customtkinter.CTkButton(secondframe,
                                            width=300,
                                            height=40,
                                            border_width=0,
                                            corner_radius=8,
                                            text="Send password reset code to email",
                                            command=emailcodeandresetopen)
    sendcodebtn.place(y=60,x=100)

    codesubmit = customtkinter.CTkEntry(secondframe,
                                    placeholder_text="Please the code here once you have recieved it in your email.",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    codesubmit.place(y=110,x=0)

    submitcodebtn = customtkinter.CTkButton(secondframe,
                                            width=300,
                                            height=40,
                                            border_width=0,
                                            corner_radius=8,
                                            text="Submit code",
                                            command=checkcode)
    submitcodebtn.place(y=170,x=100)

    logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),
	size=(80,80))

    logoframe = customtkinter.CTkFrame(login_page,
                                    width=80,
                                    height=80)
    logoframe.place(x=5,y=5)

    imagelabel = customtkinter.CTkLabel(logoframe,
                                        image=logoimage,
                                        text="")
    imagelabel.place(x=0,y=0)

    backtologin = customtkinter.CTkButton(endframe,
                                            text='Return to log in',
                                            width=200,
                                            height= 30,
                                            corner_radius=8,
                                            command=loginpage)
    backtologin.place(y=0,x=0)

def enternewresetpassword(): 
    global login_page
    global loginpage
    global useremailtochangepassword
    global passwordresetsuccess

    for widget in login_page.winfo_children():
       widget.destroy()

    bottomframe = customtkinter.CTkFrame(login_page,
                                         width=500,
                                         height=150)
    bottomframe.place(x=350,y=200)
    headerframe = customtkinter.CTkFrame(login_page,
                                     width=800,
                                     height=140)
    headerframe.place(x=200,y=10)
    endframe = customtkinter.CTkFrame(login_page,
                                      width=300,
                                      height=30)
    endframe.place(y=400,x=450)

    def returntologin():
        loginpage()

    def resetpassword():
        global useremailtochangepassword
        global userloggedin_ID
        global loginpage
        global password11
        global password22
        global passwordresetsuccess

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
                        x = f"UPDATE USERS SET password = '{password11}' WHERE email = '{useremailtochangepassword}'"
                        cursor.execute(x) 
                        connection.commit()
                        print('password changed')

                        cursor.execute(f"SELECT username FROM USERS WHERE email ='{useremailtochangepassword}'")
                        usernamereturn = cursor.fetchone()
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
                        msg['To'] = useremailtochangepassword

                        sender_password = 'ejkm dimq vdoi ktmd'

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login('interviewlabcommunications@gmail.com', sender_password)
                        server.send_message(msg)
                        print('email sucessfully sent')

                        passwordresetsuccess()
                else:
                    subprocess.Popen([sys.executable, "error message for password.py"])
            else: 
                subprocess.Popen([sys.executable, "error message for password.py"])
        else: 
            print('passwords do not match')
            subprocess.Popen([sys.executable, "error message for passwords unmatched.py"]) # Opens to the home page and passes the variable userloggedin_id into the home page script to ensure the home page can be specific to the user

    instruction = customtkinter.CTkLabel(headerframe,
                                        text='To reset your password please enter a new password in the first entry then re-enter the password again in the second entry box')
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
                                    text_color="blue")
    header.place(x=20,y=10)

    backtologin = customtkinter.CTkButton(endframe,
                                            text='Return to log in and cancel reset password request',
                                            width=300,
                                            height= 30,
                                            corner_radius=8,
                                            command=returntologin)
    backtologin.place(y=0,x=0)

def loginpage():
    global login_page
    global user_name
    global pass_word

    for widget in login_page.winfo_children():
       widget.destroy()

    def checkusernameandpassword (): 
        global user_name
        global pass_word

        usernameinputted = user_name.get()
        passwordinputted = pass_word.get()
        cursor.execute(f"SELECT username FROM USERS where username = '{usernameinputted}' and password = '{passwordinputted}'") 
        checkifexists = cursor.fetchone()
        if checkifexists == None:
            subprocess.Popen([sys.executable, "error message for incorrect login.py"]) 
        else:
            cursor.execute(f"SELECT id FROM USERS where username = '{usernameinputted}' and password = '{passwordinputted}'")
            result = cursor.fetchone()
            userloggedin_id = str(result[0])
            print(userloggedin_id)
            subprocess.Popen([sys.executable, "home_page_2.py", str(userloggedin_id)]) # Opens to the home page and passes the variable userloggedin_id into the home page script to ensure the home page can be specific to the user
            sys.exit(0)

    logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),
	size=(80,80))

    logoframe = customtkinter.CTkFrame(login_page,
                                    width=80,
                                    height=80)
    logoframe.place(x=5,y=5)

    imagelabel = customtkinter.CTkLabel(logoframe,
                                        image=logoimage,
                                        text="")
    imagelabel.place(x=0,y=0)

    topframe = customtkinter.CTkFrame(login_page)
    topframe.pack(expand = True)
    bottomframe = customtkinter.CTkFrame(login_page,
                                         height=150,
                                         width=500)
    bottomframe.pack(expand = True)
    framecreatenew = customtkinter.CTkFrame(login_page,
                                            height=70,
                                            width=200)
    framecreatenew.pack(expand = True)

    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)

    logintext = customtkinter.CTkLabel(topframe,text="Log in", font=title_font, text_color="blue")
    logintext.pack()

    introcomment = customtkinter.CTkLabel(master=topframe,
                                          wraplength=800,
                                        text='Welcome to interview lab. Your gateway to confident, sucessful interviews. Log in with your username (full name) and password, or click below to create a new account and get started on your journey.')
    introcomment.pack(pady=10, padx=10)

    user_name = customtkinter.CTkEntry(master=bottomframe,
                                    placeholder_text="Enter your username here",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    user_name.place(x=0,y=0)

    pass_word = customtkinter.CTkEntry(master=bottomframe,
                                    placeholder_text="Enter your password here",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30,
                                    show="*")
    pass_word.place(x=0,y=50)

    logincontinue = customtkinter.CTkButton(master=bottomframe,
                                            width=300,
                                            height=40,
                                            border_width=0,
                                            corner_radius=8,
                                            text="Log In",
                                            command=checkusernameandpassword)
    logincontinue.place(x=100,y=110)

    createnew = customtkinter.CTkButton(master=framecreatenew,
                                        text='Create a new account',
                                        width=200,
                                        height= 30,
                                        corner_radius=8,
                                        command=create_account)
    createnew.place(x=0,y=0)

    forgotpassword = customtkinter.CTkButton(framecreatenew,
                                            text='Forgotten password',
                                            width=200,
                                            height= 30,
                                            corner_radius=8,
                                            command=forgot_password)
    forgotpassword.place(y=40,x=0)

def create_account():
    global login_page
    global currentloggedinID

    for widget in login_page.winfo_children():
       widget.destroy()

    db = sqlite3.connect('Interview_lab_database.db')
    cur = db.cursor()
 
    def check_database_email_and_validity ():
        emailinputted = email_input.get() 
        cur.execute(f"SELECT email FROM USERS where email = '{emailinputted}'")  
        checkifexists = cur.fetchone()  
        if checkifexists == None:
            if validators.email(emailinputted):
                return 1
            else:
                subprocess.Popen([sys.executable, "error message for email_wrong_format.py"])

        else:
            subprocess.Popen([sys.executable, "error message for email_already_used.py"])
            return 0

    # Function for checking if the username entered is already in the database to avoid having two usernames of the same in the database
    def check_database_username ():
        usernameinputted = user_name.get() # This retreives the input the user entered into the entry box 
        cur.execute(f"SELECT username FROM USERS where username = '{usernameinputted}'")  # This is the SQL statement for retreiving user name. Using an f string here to allows me to insert the variable in the string 
        checkifexists = cur.fetchone() # This returns none if username has not been taken  
        if checkifexists == None:
            return 1 # This links to next function that the username is valid as that username has not already been taken 
        else:
            subprocess.Popen([sys.executable, "error message for username.py"]) # If username has already been taken output the error message window 
            return 0

    def check_database_user_pass():
        global currentloggedinID

        e = check_database_email_and_validity()
        y = check_database_username() # Perform the function check_database_username 
        emailinputted = email_input.get()
        usernameinputted = user_name.get()
        passwordinputted = pass_word.get()
        if y == 1 and e == 1:
            if len(passwordinputted) >= 8: # Checking the password is at least 8 characters long
                number = any(char.isdigit() for char in passwordinputted) # Searches for any numerical digits within the password. Returns True or False (boolean) if there are digits or not 
                if number:
                    regex = re.compile('[@_!#$%^&*()<>?/}{~:]')
                    if regex.search(passwordinputted) == None:
                        subprocess.Popen([sys.executable, "error message for password.py"])
                    else: 
                        usernameinputted = user_name.get() 
                        sqlite3_add = "INSERT INTO USERS (username) VALUES(?)" # SQL statement for inserting username into the database 
                        val = usernameinputted # Creating a new variable which will be passed into the database 
                        cur.execute(sqlite3_add, (val,)) # Executes the SQL statement 
                        db.commit() # Saves all the changes to the database 
                        sql00 = (f"UPDATE USERS SET email = '{emailinputted}' WHERE username = '{usernameinputted}'") # Basically a repeat of the code above for putting the password in now. Added to the SQL statement to ensure that the password and username are entered into the same record 
                        cur.execute(sql00)
                        db.commit()
                        sql = (f"UPDATE USERS SET password = '{passwordinputted}' WHERE username = '{usernameinputted}'") # Basically a repeat of the code above for putting the password in now. Added to the SQL statement to ensure that the password and username are entered into the same record 
                        cur.execute(sql)
                        db.commit()
                        
                        msg = EmailMessage()
                        msg.set_content(f'''
Hello {usernameinputted},
                            
Welcome to Interview Lab! We are thrilled to have you join our community!

At Interview Lab, we are all about helping you shine in your interviews. 
Think of this platform as your personal interview coach, providing you with realistic simulations, insightful feedback, and the tools you need to feel confident and prepared.

Get ready for your interview:
    - Practice makes perfect! Simulate real interview scenarios on our interactive platform. The more details you provide about your target job, the better the interview and feedback will be.                   
    - Receive personalized feedback. This will be emailed to this email address after each interview practice. Analyze your performance and identify areas for improvement.
    - Build your confidence. Walk into your next interview feeling prepared and ready to impress!

We are excited to help you on your journey to landing your dream job. Feel free to explore the platform and do not hesitate to reach out if you have any questions. 
Please send an email to interviewlabcommunications@gmail.com with any questions or queries.

Happy interviewing!
Best regards,
Interview lab team''')

                        msg['Subject'] = 'Welcome to interview lab!'
                        msg['From'] = 'interviewlabcommunications@gmail.com'
                        msg['To'] = f'{emailinputted}'

                        sender_password = 'ejkm dimq vdoi ktmd'

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login('interviewlabcommunications@gmail.com', sender_password)
                        server.send_message(msg)
                        print('email sucessfully sent')

                        cursor.execute(f"SELECT id FROM USERS where username = '{usernameinputted}'")
                        result = cursor.fetchone()
                        currentloggedinID = str(result[0])

                        print(currentloggedinID)

                        subprocess.Popen([sys.executable, "home_page_2.py", currentloggedinID])

                        subprocess.Popen([sys.executable, "account creation success.py"])

                        sys.exit()

                else:
                    subprocess.Popen([sys.executable, "error message for password.py"])
            else:
                subprocess.Popen([sys.executable, "error message for password.py"]) 

    oneframe = customtkinter.CTkFrame(login_page,
                                      width=800,
                                      height=120)
    oneframe.place(x=200,y=30)
    oneframe.pack_propagate(0)
    bottomframe = customtkinter.CTkFrame(login_page,
                                         width=500,
                                         height=200)
    bottomframe.place(y=200,x=350)
    bottomframe.pack_propagate(0)
    endframe = customtkinter.CTkFrame(login_page,
                                      width=200,
                                      height=30)
    endframe.place(y=430,x=500)
    endframe.pack_propagate(0)

    title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)

    header = customtkinter.CTkLabel(oneframe,
                                text="Create new account",
                                font=title_font,
                                text_color="blue")
    header.place(x=10,y=10)

    introcomment = customtkinter.CTkLabel(oneframe,
                                        text='Please enter your details to create your account')
    introcomment.place(x=10,y=80)

    logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),
	size=(80,80))

    logoframe = customtkinter.CTkFrame(login_page,
                                    width=80,
                                    height=80)
    logoframe.place(x=5,y=5)

    imagelabel = customtkinter.CTkLabel(logoframe,
                                        image=logoimage,
                                        text="")
    imagelabel.place(x=0,y=0)

    email_input = customtkinter.CTkEntry(bottomframe,
                                    placeholder_text="Please enter your email below.",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    email_input.pack()

    user_name = customtkinter.CTkEntry(master=bottomframe,
                                    placeholder_text="Please choose a username (full name) and type here.",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    border_width=2,
                                    corner_radius=30)
    user_name.pack()

    pass_word = customtkinter.CTkEntry(master=bottomframe,
                                    placeholder_text="Please choose a secure password and type here",
                                    placeholder_text_color="Light blue",
                                    width=500,
                                    height=50,
                                    show="*",
                                    border_width=2,
                                    corner_radius=30)
    pass_word.pack()

    create = customtkinter.CTkButton(master=bottomframe,
                                            width=300,
                                            height=40,
                                            border_width=0,
                                            corner_radius=8,
                                            text="Create account",
                                            command=check_database_user_pass)
    create.place(y=160,x=100)

    backtologin = customtkinter.CTkButton(endframe,
                                            text='Return to log in',
                                            width=200,
                                            height= 30,
                                            corner_radius=8,
                                            command=loginpage)
    backtologin.place(y=0,x=0)

def passwordresetsuccess(): 
    global login_page

    for widget in login_page.winfo_children():
       widget.destroy()

    logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),
	size=(80,80))

    logoframe = customtkinter.CTkFrame(login_page,
                                    width=80,
                                    height=80)
    logoframe.place(x=5,y=5)

    imagelabel = customtkinter.CTkLabel(logoframe,
                                        image=logoimage,
                                        text="")
    imagelabel.place(x=0,y=0)

    messageframe = customtkinter.CTkFrame(login_page,
                                          width=600,
                                          height=50)
    messageframe.place(x=300,y=10)
    btnframe = customtkinter.CTkFrame(login_page,
                                      width=300,
                                      height=40)
    btnframe.place(x=450,y=100)

    title_font = customtkinter.CTkFont(size=40,weight="bold",family='Roboto')

    message = customtkinter.CTkLabel(messageframe,
                                     text="Reset password success",
                                     font=title_font,
                                     text_color="blue")
    message.place(x=0,y=0)

    backtologinbtn = customtkinter.CTkButton(btnframe,
                               width=300,
                               height=40,
                               border_width=0,
                               corner_radius=8,
                               command = loginpage,
                               text="Click here to login with your new password")
    backtologinbtn.place(x=0,y=0)

    logoimage = customtkinter.CTkImage(light_image=Image.open("Celebration of account.png"),
    size=(400,275))

    logoframe = customtkinter.CTkFrame(login_page,
                                    width=400,
                                    height=275)
    logoframe.place(x=400,y=160)

    imagelabel = customtkinter.CTkLabel(logoframe,
                                        image=logoimage,
                                        text="")
    imagelabel.place(x=0,y=0)

logoimage = customtkinter.CTkImage(light_image=Image.open("Interview lab logo.png"),
	size=(80,80))

logoframe = customtkinter.CTkFrame(login_page,
                                   width=80,
                                   height=80)
logoframe.place(x=5,y=5)

imagelabel = customtkinter.CTkLabel(logoframe,
                                    image=logoimage,
                                    text="")
imagelabel.place(x=0,y=0)

topframe = customtkinter.CTkFrame(login_page,
                                  width=300,
                                  height=90)
topframe.place(x=400,y=250)

headerframe = customtkinter.CTkFrame(login_page,
                                     width=800,
                                     height=160)
headerframe.place(x=200,y=50)

title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)

header = customtkinter.CTkLabel(headerframe,
                                text="Welcome to Interview Lab...",
                                font=title_font,
                                text_color="blue")
header.place(x=20,y=10)
                                
subheader = customtkinter.CTkLabel(headerframe,
                                   text="Please choose an option from below to get started on your interview journey.")
subheader.place(x=20,y=100)

login = customtkinter.CTkButton(topframe,
                               width=300,
                               height=40,
                               border_width=0,
                               corner_radius=8,
                               command = loginpage,
                               text="Log in")
login.place(x=0,y=0)

createnew = customtkinter.CTkButton(topframe,
                               width=300,
                               height=40,
                               border_width=0,
                               corner_radius=8,
                               command = create_account,
                               text="Create new account")
createnew.place(x=0,y=50)

login_page.mainloop()

