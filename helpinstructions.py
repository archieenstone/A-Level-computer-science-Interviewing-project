import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

help = customtkinter.CTk()
help.title('Program support page') 
help.geometry('1000x700')

title_font = customtkinter.CTkFont(size=60,weight="bold",family='Roboto', underline=True)
title = customtkinter.CTkLabel(help, text="Software support", font=title_font, text_color="blue")
title.place(x=10,y=10)

helptext = """Interview Lab Help & Support Center

Welcome to the Interview Lab Help Center! If you run into any issues or have questions about how to use the application, follow the guides below to get back on track.


Performance & Loading Note

Patience is Key: The interview simulation uses advanced AI processing to render your real-time practice environment. Pages or modules may occasionally take a few moments to load.
What to do: Please allow each page or popup window to load fully before clicking away or refreshing.


How to Run an Interview Simulation

Step 1: Inputting Job Details

First-Time Setup: Enter your Target Job Title, Job Description/Specification, and any extra context (e.g., key skills, company background) into the provided fields, then click Continue.
Returning Users: If you have used Interview Lab before, your previously entered details are saved automatically! Simply scroll down the Home Page and click Start Saved Simulation to skip re-entering your information.

Step 2: Customizing Your Session

Once your job info is loaded, click Continue to move to the customization menu. Here, you can select:

Interview Duration: Set your desired timer length.
Interviewer Persona: Choose the style/tone of your interviewer (e.g., Friendly, Strict, Technical).
Question Type: Select behavioral, technical, situational, or mixed questions.
Pitch Practice Mode (Optional): If you want to practice an elevator pitch or personal introduction, select this option to jump straight into a specialized pitch practice session.

Step 3: The Interview Interface

Camera Setup: Upon entering the simulation room, you will see your self-view on screen (make sure your webcam permissions are enabled).
Starting: Click Start Interview. The timer will initialize. Note: It may take up to 30 seconds for the AI interviewer to initialize and ask the first question.
Answering: Speak directly to the interviewer as you would in a real session.
Ending Early: If you need to stop before the timer runs out, click End Interview, then confirm your choice by clicking End Interview again on the popup confirmation window. You will still get feedback even if you didn't finish the interview. 
Automatic Completion: When the timer runs out, the session will automatically wrap up and redirect you to the Feedback page.


Getting Your Feedback

Once the simulation ends, you will arrive at the Feedback Page.
Click the Get My Feedback button to generate your detailed performance report.
Delivery: Once generated, your complete feedback analysis will automatically be emailed to your registered account, and you will be redirected back to the Home Page.


Account & General Settings

Forgotten Password

Click on Forgot Password? at the login screen.
Enter your registered email address to receive a secure password reset link.

Updating Your Username or Profile Details

Navigate to Settings.
Enter your new details and click Save Changes.

Dark Mode / Light Mode

Go to Settings. Toggle between Light Mode and Dark Mode according to your preference. 


Still having trouble operating Interview Lab? Drop us an email at interviewlabcommunications@gmail.com and we will repond as soon as possible to help you get it sorted. 


"""

mainframe = customtkinter.CTkScrollableFrame(help,width=850,height=500)
mainframe.place(x=50,y=100)

helpinstructions = customtkinter.CTkLabel(mainframe, text=helptext, width=800, wraplength=800, justify="left")
helpinstructions.pack(anchor="w")


help.mainloop()

