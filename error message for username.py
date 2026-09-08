import customtkinter

customtkinter.set_appearance_mode('light') 
customtkinter.set_default_color_theme('blue') 

u_error_page = customtkinter.CTk() 
u_error_page.title('Username error report') 
u_error_page.geometry('400x200')  

topframe = customtkinter.CTkFrame(u_error_page)
topframe.pack(expand = True)

displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=200,
                                        text='Unfortunately that user name has already been taken. Please close this window and return to the create account page to enter a new username')
displaymessage.pack()

u_error_page.mainloop()
