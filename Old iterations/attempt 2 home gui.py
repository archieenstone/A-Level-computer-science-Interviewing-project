import tkinter as tk
import subprocess
import sys
from interview_setup_options import *
import sqlite3

# Create the main window
root = tk.Tk()
root.state("zoomed")  # Set window size
root.title("Interview lab")  # Set window title


def save_to_file():
    textinputted = txtinput.get("1.0", "end-1c")
    with open("user_input.txt", "w") as f:  
        f.write(textinputted)

# Create a StringVar to associate with the label
welcome = tk.StringVar()
welcome.set("Welcome to Interview lab")

# Create the label widget with all options
welcome = tk.Label(root, 
                 textvariable=welcome, 
                 anchor=tk.CENTER,       
                 bg="lightblue",      
                 height=3,              
                 width=300,                              
                 font=("Calibri", 30, "bold"),    
                 fg="dark blue",             
                 padx=10,               
                 pady=10,                
                 justify=tk.CENTER,                            
                )

# Pack the label into the window
welcome.pack(pady=0)  # Add some padding to the top

#creating text variable 2
tagline = tk.StringVar()
tagline.set("Where interview preparation becomes interview success")

tagline = tk.Label(root, 
                 textvariable=tagline, 
                 anchor=tk.CENTER,       
                 bg="dark blue",      
                 height=1,              
                 width=300,                              
                 font=("Calibri", 13),    
                 fg="white",             
                 padx=10,               
                 pady=10,                
                 justify=tk.CENTER,                            
                )

tagline.pack(pady=0)

instruction1 = tk.StringVar()
instruction1.set("Please enter all the details about your job interview into the text input box below, including any links and written information you have. Use the “Upload File” button to add your CV, the job description, job specification, or any other documents that will help us tailor your interview practice specifically to the role you're applying for. Once completed press 'Progress to interview simulation' below.")
instruction1 = tk.Label(root,
                        textvariable=instruction1,
                        wraplength=900,)

instruction1.pack(pady=10)

txtinput = tk.Text(root, height=15, width=130)
txtinput.pack()

submit_info = tk.Button(text="Progress to interview simulation",
                        height=4,
                        width=50)
submit_info.pack(pady=10)

# Run the main event loop
root.mainloop()