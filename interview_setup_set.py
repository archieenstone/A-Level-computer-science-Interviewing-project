import customtkinter
import subprocess 
import sys
import sqlite3

userloggedin_ID = int(sys.argv[1])

db = sqlite3.connect('Interview_lab_database.db')
cur = db.cursor()

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

u_error_page = customtkinter.CTk()
u_error_page.title('Interview set up options') 
u_error_page.geometry('800x600') 

def startinterview():
    length = lengthoption.get()
    lengthdb = (f"UPDATE USERS SET lengthofinterview = '{length}' WHERE id = '{userloggedin_ID}'")
    cur.execute(lengthdb)
    db.commit()

    interviewpersona = persona.get()
    personadb = (f"UPDATE USERS SET interviewerpersona = '{interviewpersona}' WHERE id = '{userloggedin_ID}'")
    cur.execute(personadb)
    db.commit()

    difficultylevel = diflevel.get()
    diffdb = (f"UPDATE USERS SET difflevel = '{difficultylevel}' WHERE id = '{userloggedin_ID}'")
    cur.execute(diffdb)
    db.commit()

    numberofselects = 0
    questiondomainoptionsselected = []

    if ssvar.get() == 1:
        questiondomainoptionsselected.append('Situational and scenario based')
        numberofselects = numberofselects + 1 

    if rstk.get() == 1: 
        questiondomainoptionsselected.append('Role specific technical skills')
        numberofselects = numberofselects + 1 

    if lam.get() == 1:
        questiondomainoptionsselected.append('Leadership and management')
        numberofselects = numberofselects + 1 

    if caa.get() == 1: 
        questiondomainoptionsselected.append('Creative and abstract')
        numberofselects = numberofselects + 1 

    if ccm.get() == 1: 
        questiondomainoptionsselected.append('Company culture and motivation')
        numberofselects = numberofselects + 1 

    if hbc.get() == 1: 
        questiondomainoptionsselected.append('History, behaviour and compentency')
        numberofselects = numberofselects + 1 

    res = ""                
    for x in questiondomainoptionsselected:
        res += x + " and "

    questiontypesdb = (f"UPDATE USERS SET questiondomainsselected = '{res}' WHERE id = '{userloggedin_ID}'")
    cur.execute(questiontypesdb)
    db.commit()

    subprocess.Popen([sys.executable, "interviewgui.py", str(userloggedin_ID)])
    sys.exit()

difficultyoptions = ['Easy', 'Medium', 'Hard', 'Very challenging']

timeoption = ['10mins', '15mins', '20mins', '30mins', '45mins', '60mins']

interviewerpersona = ['Corporate and structured', 'Strict and intimidating', 'Relax and conversational']

questiondomains = ['Situational and scenario based', 'Role specific technical skills', 'Leadership and management', 'Creative and abstract', 'Company culture and motivation', 'History, behaviour and compentency']

toptopframe = customtkinter.CTkFrame(u_error_page,
                                     width=600,
                                     height=80)
toptopframe.place(x=100,y=0)

dropdownframe = customtkinter.CTkFrame(u_error_page,
                                       width=500,
                                       height=400)
dropdownframe.pack_propagate(False)
dropdownframe.place(x=130,y=130)

title_font = customtkinter.CTkFont(size=30,weight="bold",family='Roboto', underline=True)

title = customtkinter.CTkLabel(toptopframe,
                               font=title_font,
                               text="Interview preferences",
                               text_color="blue",
                               width=500,
                               justify="center")
title.pack(padx=10,pady=10)

displaymessage = customtkinter.CTkLabel(master=toptopframe,
                                        wraplength=600,
                                        text='Please select the options from the drop down menus to how you want your interview to run to make it as personalised and relevant as possible')
displaymessage.pack(padx=10,pady=10)

label1 = customtkinter.CTkLabel(dropdownframe, text="Question domains")
label1.place(y=5,x=150)
ssvar = customtkinter.IntVar(value=0)
questiondomainsoptions = customtkinter.CTkCheckBox(dropdownframe, text='Situational and scenario based', variable=ssvar, onvalue=1, offvalue=0, command=startinterview)
questiondomainsoptions.place(x=140,y=30)
rstk = customtkinter.IntVar(value=0)
questiondomainsoptions = customtkinter.CTkCheckBox(dropdownframe, text='Role specific technical skills', variable=rstk, onvalue=1, offvalue=0)  
questiondomainsoptions.place(x=140,y=55)
lam = customtkinter.IntVar(value=0)
questiondomainsoptions = customtkinter.CTkCheckBox(dropdownframe, text='Leadership and management', variable=lam, onvalue=1, offvalue=0)
questiondomainsoptions.place(x=140,y=80)
caa = customtkinter.IntVar(value=0)
questiondomainsoptions = customtkinter.CTkCheckBox(dropdownframe, text='Creative and abstract', variable=caa, onvalue=1, offvalue=0)
questiondomainsoptions.place(x=140,y=105)
ccm = customtkinter.IntVar(value=0)
questiondomainsoptions = customtkinter.CTkCheckBox(dropdownframe, text='Company culture and motivation', variable=ccm ,onvalue=1, offvalue=0)
questiondomainsoptions.place(x=140,y=130)
hbc = customtkinter.IntVar(value=0)
questiondomainsoptions = customtkinter.CTkCheckBox(dropdownframe, text='History, behaviour and compentency', variable=hbc, onvalue=1, offvalue=0)
questiondomainsoptions.place(x=140,y=155)

label2 = customtkinter.CTkLabel(dropdownframe, text="Length of interview")
label2.place(x=150,y=190)
lengthoption = customtkinter.CTkOptionMenu(dropdownframe, values=timeoption)
lengthoption.place(x=150,y=215)

label3 = customtkinter.CTkLabel(dropdownframe, text="Interviewer persona")
label3.place(x=150,y=250)
persona = customtkinter.CTkOptionMenu(dropdownframe, values=interviewerpersona)
persona.place(x=150,y=275)

label4 = customtkinter.CTkLabel(dropdownframe, text="Difficulty level")
label4.place(x=150,y=310)
diflevel = customtkinter.CTkOptionMenu(dropdownframe, values=difficultyoptions)
diflevel.place(x=150,y=335)

continuebtn = customtkinter.CTkButton(u_error_page,
                                   text="Continue",
                                   width=50,
                                   height=30,
                                   command=startinterview)
continuebtn.place(x=300,y=550)

u_error_page.mainloop()
