from google import genai
from google.genai import types
import sqlite3
import os
import sys
import subprocess
from email.message import EmailMessage
import smtplib
import customtkinter

customtkinter.set_appearance_mode('light') #set light mode 
customtkinter.set_default_color_theme('blue') #set colour scheme to blue

loadingpage = customtkinter.CTk() #create the output app
loadingpage.title('Loading...') #set a title for the program window 
loadingpage.geometry('800x500')  # Set window size

text = customtkinter.CTkLabel(loadingpage,text="Loading and emailing your personalised feedback from your recent interview practice session...")
text.pack(pady=20,padx=20)

print('yep moving porgr')

db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

userloggedin_ID = 0
with open("useridloggedin.txt") as f:
    userloggedin_ID = (f.read())

cur.execute(f"SELECT email FROM USERS where id = {userloggedin_ID}")
result = cur.fetchone()
useremail = result[0]

cur.execute(f"SELECT username FROM USERS where id = {userloggedin_ID}")
result = cur.fetchone()
username = result[0]

modified = []

client = genai.Client(api_key="AQ.Ab8RN6LZa2jmY-lpucIY2xXegfaD0EDPlkWbPpHP7CYxn65fyw")

file = open('conversation_log.txt', 'r')
data = file.readlines()

for line in data:
    modified.append(line.strip())

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=f"Summarise the conversation {modified}"
)

feedback = (response.text)

questiontypesdb = (f"UPDATE USERS SET questiondomainsselected = {feedback} WHERE id = '{userloggedin_ID}'")
cur.execute(questiontypesdb)
db.commit()

os.remove("conversation_log.txt")
os.remove("useridloggedin.txt")

msg = EmailMessage()
msg.set_content(f'''
Hello {username},
                            
Dear [Username],

Congratulations on completing your recent interview practice session! Taking the time to sharpen your skills and prepare thoroughly says a lot about your dedication, and we were thrilled to sync up with you.
We appreciate the energy and focus you brought to the session. Continuous improvement is the secret weapon to acing the real deal, and you're already putting in the work.

As promised, here is the direct feedback from your session:

{feedback}

We hope these insights help you fine-tune your approach and build even more confidence. If you have any questions about these notes or want to schedule another round to test out adjustments, just let us know.
Keep up the fantastic momentum, and best of luck with your upcoming preparation!

Best regards,
Interview lab team''')

msg['Subject'] = 'Feedback from your recent interview practice session'
msg['From'] = 'interviewlabcommunications@gmail.com'
msg['To'] = f'{useremail}'

sender_password = 'ejkm dimq vdoi ktmd'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('interviewlabcommunications@gmail.com', sender_password)
server.send_message(msg)
print('email sucessfully sent')

subprocess.Popen([sys.executable, "home_page_2.py", str(userloggedin_ID)])
sys.exit()

loadingpage.mainloop()
