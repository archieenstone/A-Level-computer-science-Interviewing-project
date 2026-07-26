import customtkinter

customtkinter.set_appearance_mode('light') #set light mode 
customtkinter.set_default_color_theme('blue') #set colour scheme to blue

home_page = customtkinter.CTk() #create the output app
home_page.title('Interview lab') #set a title for the program window 
home_page.geometry('1200x800')

#creating a frame for the whole page. this will allow scrolling
scrollingframe = customtkinter.CTkFrame(home_page)
scrollingframe.pack(fill="both", expand=1)

#creating a canvas
canvas = customtkinter.CTkCanvas(scrollingframe)
canvas.pack(side="left", fill="both", expand=1)

#add a scrollbar to the canvas 
scrollbar = customtkinter.CTkScrollbar(scrollingframe, orientation="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

#configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#create another frame inside the canvas 
editingframe = customtkinter.CTkFrame(canvas, fg_color="transparent")

#add that new frame to a window in the canvas 
canvas.create_window((0,0), window=editingframe, anchor="nw")
