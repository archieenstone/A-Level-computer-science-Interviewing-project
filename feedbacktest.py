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

text = customtkinter.CTkLabel(loadingpage,text="Loading and emailing your personalised feedback from your recent interview practice session... Once the email has been reset you will be redirected back to the home page where you can visit the history tab to recieve your feedback.",
                              wraplength=500)
text.pack(pady=20,padx=20)

print('yep omving porgr')

db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

userloggedin_ID = 0
with open("useridloggedin.txt") as f:
    userloggedin_ID = (f.read())
    f.close()

cur.execute(f"SELECT email FROM USERS where id = {userloggedin_ID}")
resultemail = cur.fetchone()
useremail = resultemail[0]

cur.execute(f"SELECT username FROM USERS where id = {userloggedin_ID}")
resultusername = cur.fetchone()
username = resultusername[0]

modified = []

client = genai.Client(api_key="AQ.Ab8RN6LZa2jmY-lpucIY2xXegfaD0EDPlkWbPpHP7CYxn65fyw")

file = open('conversation_log.txt', 'r')
data = file.readlines()

for line in data:
    modified.append(line.strip())

print(data)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=f"""
You are an elite Executive Interview Coach and Behavioral Analyst. Your objective is to analyze a timestamped interview transcript between an Interviewer and a Candidate. 

You must provide a highly structured, objective, and constructive feedback report for the candidate. Use the timestamps to cite specific moments in the transcript to back up your feedback (e.g., "At [04:15], you provided a great example of..."). 

Always balance constructive criticism with positive reinforcement. Format your response EXACTLY using the following markdown headers and bullet points. Do not deviate from this 12-section structure.

### 1. Overall Performance Summary
* Provide a 3-4 sentence executive summary of the candidate's overall performance, highlighting their strongest trait and their biggest area for improvement.

### 2. The STAR Method Application (Situation, Task, Action, Result)
* Analyze how well the candidate structured their behavioral answers. 
* Cite a specific timestamp where they used it perfectly, or a timestamp where they missed an opportunity to use it.

### 3. Filler Words & Vocal Tics
* Identify any repetitive filler words ("um," "uh," "like," "you know," "essentially"). 
* Note if they appear clustered around specific types of questions (e.g., "You used 'um' frequently during the technical questions around [08:30]").

### 4. Clarity & Articulation
* Did the candidate explain complex concepts simply and clearly?
* Highlight any timestamps where an explanation became convoluted or hard to follow.

### 5. Pacing, Pauses & Timing
* Use the timestamps to analyze the length of the candidate's answers. 
* Were there uncomfortably long pauses before answering? Did any answer run on for too long (over 3 minutes)? 

### 6. Relevance & Question Comprehension
* Did the candidate actually answer the questions being asked, or did they dodge them/go off on a tangent? 
* Cite specific timestamps where they stayed highly focused or drifted away from the core question.

### 7. Confidence & Assertiveness
* Analyze the candidate's tone based on their language choices. 
* Identify passive language (e.g., "I think I helped," "We sort of tried") versus active, confident language (e.g., "I led," "I successfully implemented").

### 8. Professionalism & Vocabulary
* Was the candidate's language appropriate for a professional setting? 
* Did they use industry-standard terminology correctly to demonstrate domain expertise?

### 9. Action-Oriented Focus (The "I" vs. "We" Balance)
* Did the candidate take ownership of their achievements? 
* Note if they relied too heavily on "we" instead of clearly stating their individual contributions ("I").

### 10. Handling Pressure & Curveballs
* How did the candidate react to difficult, unexpected, or multi-part questions? 
* Did they maintain composure, ask clarifying questions, or rush into a poorly thought-out answer? Cite timestamps.

### 11. Active Listening & Engagement
* Did the candidate acknowledge the interviewer's statements? 
* Did they seamlessly build on conversational threads, or did it feel like two people talking at each other?

### 12. Actionable Next Steps
* Provide 3 concrete, highly specific exercises or focus areas the candidate should practice before their next real interview.

---
### INTERVIEW TRANSCRIPT FOR ANALYSIS:
[INSERT_TIMESTAMPED_TRANSCRIPT_HERE]

"""
)

file.close()

feedback = (response.text)
print(feedback)

questiontypesdb = ("UPDATE USERS SET lastfeedbacksession = ? WHERE id = ?")
cur.execute(questiontypesdb, (feedback, userloggedin_ID))
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
