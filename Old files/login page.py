import customtkinter
import sqlite3
import sys
import subprocess

currentloggedinID = 0

def open_create_window():
    subprocess.Popen([sys.executable, "create_account.py"]) 
    sys.exit(0)

connection = sqlite3.connect('Interview_lab_database.db') #creating database file

cursor = connection.cursor() #create cursor function to use the information in the table

#creating a table for storing user information
command1 = ('''
    CREATE TABLE IF NOT EXISTS
    USERS(id integer primary key autoincrement, username Text, email Text, password Text)
              ''')

cursor.execute(command1)

customtkinter.set_appearance_mode('light') #set light mode 
customtkinter.set_default_color_theme('blue') #set colour scheme to blue

login_page = customtkinter.CTk() #create the output app
login_page.title('User login') #set a title for the program window 
login_page.geometry('1200x500')  # Set window size

#lines in this section create the different frames and expand them depending on what goes in them
topframe = customtkinter.CTkFrame(login_page)
topframe.pack(expand = True)
bottomframe = customtkinter.CTkFrame(login_page)
bottomframe.pack(expand = True)
framecreatenew = customtkinter.CTkFrame(login_page)
framecreatenew.pack(expand = True)

def forgotpassword(): 
    subprocess.Popen([sys.executable, "forgotpassword.py"]) 

def checkusernameandpassword (): 
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

introcomment = customtkinter.CTkLabel(master=topframe,
                                      text='Welcome to interview lab. Your gateway to confident, sucessful interviews. Log in with your username and password, or click below to create a new account and get started on your journey.')
introcomment.pack()

user_name = customtkinter.CTkEntry(master=bottomframe,
                                   placeholder_text="Username",
                                   placeholder_text_color="Light blue",
                                   width=500,
                                   height=50,
                                   border_width=2,
                                   corner_radius=30)
user_name.pack(pady=10)

pass_word = customtkinter.CTkEntry(master=bottomframe,
                                   placeholder_text="Password",
                                   placeholder_text_color="Light blue",
                                   width=500,
                                   height=50,
                                   border_width=2,
                                   corner_radius=30,
                                   show="*")
pass_word.pack(pady=10)

logincontinue = customtkinter.CTkButton(master=bottomframe,
                                        width=300,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8,
                                        text="Log In",
                                        command=checkusernameandpassword)
logincontinue.pack()

createnew = customtkinter.CTkButton(master=framecreatenew,
                                    text='Create a new account',
                                    width=200,
                                    height= 30,
                                    corner_radius=8,
                                    command=open_create_window)
createnew.pack(pady=10)

forgotpassword = customtkinter.CTkButton(framecreatenew,
                                         text='Forgotten password',
                                         width=200,
                                         height= 30,
                                         corner_radius=8,
                                         command = forgotpassword)
forgotpassword.pack(pady=10)

login_page.mainloop()