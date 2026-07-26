import customtkinter
import tkinter as tk
import sys
import subprocess
import sqlite3
import validators
import smtplib
from email.message import EmailMessage

# Connect to the database that was created in the login page script. Then set cur as the object that allows interact with the database 
db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

# Set the appearance mode to light and then set the colour scheme to blue 
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

# Create the output window. Set the title of the page to be User create account then also set the side of the page to be 1200 x 500 pixels 
login_page = customtkinter.CTk() 
login_page.title('User create account')  
login_page.geometry('1200x500')  

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
    e = check_database_email_and_validity()
    y = check_database_username() # Perform the function check_database_username 
    emailinputted = email_input.get()
    usernameinputted = user_name.get()
    passwordinputted = pass_word.get()
    if y == 1 and e == 1:
        if len(passwordinputted) >= 8: # Checking the password is at least 8 characters long
            number = any(char.isdigit() for char in passwordinputted) # Searches for any numerical digits within the password. Returns True or False (boolean) if there are digits or not 
            if number:
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
                subprocess.Popen([sys.executable, "login page.py"]) # Takes user back to login page as they have not successfully 

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

                sys.exit(0)
            else:
                subprocess.Popen([sys.executable, "error message for password.py"])
        else:
            subprocess.Popen([sys.executable, "error message for password.py"]) 

def back_login_page():
    subprocess.Popen([sys.executable, "login page.py"])
    sys.exit()

# Creating the different frames and expand them depending on what goes in them
topframe = customtkinter.CTkFrame(login_page)
topframe.pack(expand = True)
bottomframe = customtkinter.CTkFrame(login_page)
bottomframe.pack(expand = True)

introcomment = customtkinter.CTkLabel(master=topframe,
                                      text='Please enter your details to create your account')
introcomment.pack()

email_input = customtkinter.CTkEntry(bottomframe,
                                placeholder_text="Please enter your email below.",
                                placeholder_text_color="Light blue",
                                width=500,
                                height=50,
                                border_width=2,
                                corner_radius=30)
email_input.pack(pady=10)

user_name = customtkinter.CTkEntry(master=bottomframe,
                                   placeholder_text="Please choose a user name and type here.",
                                   placeholder_text_color="Light blue",
                                   width=500,
                                   height=50,
                                   border_width=2,
                                   corner_radius=30)
user_name.pack(pady=10)

pass_word = customtkinter.CTkEntry(master=bottomframe,
                                   placeholder_text="Please choose a secure password and type here",
                                   placeholder_text_color="Light blue",
                                   width=500,
                                   height=50,
                                   show="*",
                                   border_width=2,
                                   corner_radius=30)
pass_word.pack(pady=10)

logincontinue = customtkinter.CTkButton(master=bottomframe,
                                        width=300,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8,
                                        text="Create account",
                                        command=check_database_user_pass)
logincontinue.pack()

backtologin = customtkinter.CTkButton(master=bottomframe,
                                        width=300,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8,
                                        text="Return to login page",
                                        command=back_login_page)
backtologin.pack(pady=20)

login_page.mainloop()