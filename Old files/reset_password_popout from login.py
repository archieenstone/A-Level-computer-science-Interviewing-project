import customtkinter
import sqlite3
import sys
import subprocess

useremailtochangepassword = sys.argv[1]
print(useremailtochangepassword)

connection = sqlite3.connect('Interview_lab_database.db') #creating database file
cursor = connection.cursor() #create cursor function to use the information in the table

customtkinter.set_appearance_mode('light') #set light mode 
customtkinter.set_default_color_theme('blue') #set colour scheme to blue

page = customtkinter.CTk() #create the output app
page.title('Password reset') #set a title for the program window 
page.geometry('1200x500')  # Set window size

topframe = customtkinter.CTkFrame(page)
topframe.pack(expand = True)
bottomframe = customtkinter.CTkFrame(page)
bottomframe.pack(expand = True)

def resetpassword():
    global useremailtochangepassword
    useremailtochangepassword = str(useremailtochangepassword)
    global userloggedin_ID
    password11 = password1.get()
    password22 = password2.get()
    if password11 == password22:
        print('passwords match')
        x = f"UPDATE USERS SET password = '{password11}' WHERE email = '{useremailtochangepassword}'"
        cursor.execute(x) 
        connection.commit()
        print('password changed')
        sys.exit()
    else: 
        print('passwords do not match')
        subprocess.Popen([sys.executable, "error message for passwords unmatched.py"]) # Opens to the home page and passes the variable userloggedin_id into the home page script to ensure the home page can be specific to the user

instruction = customtkinter.CTkLabel(master=topframe,
                                      text='To reset your password please enter a new password in the first entry then re-enter the password again in the second entry box')
instruction.pack()

password1 = customtkinter.CTkEntry(master=bottomframe,
                                   placeholder_text="Please enter your new password here",
                                   placeholder_text_color="Light blue",
                                   width=500,
                                   height=50,
                                   border_width=2,
                                   corner_radius=30)
password1.pack(pady=10)

password2 = customtkinter.CTkEntry(master=bottomframe,
                                   placeholder_text="Now re-enter your password here",
                                   placeholder_text_color="Light blue",
                                   width=500,
                                   height=50,
                                   border_width=2,
                                   corner_radius=30)
password2.pack(pady=10)

reset_password = customtkinter.CTkButton(master=bottomframe,
                                        width=300,
                                        height=40,
                                        border_width=0,
                                        corner_radius=8,
                                        text="Reset password",
                                        command=resetpassword)
reset_password.pack()

page.mainloop()
