import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

u_error_page = customtkinter.CTk()
u_error_page.title('Incorrect code entered report') 
u_error_page.geometry('400x200') 

topframe = customtkinter.CTkFrame(u_error_page)
topframe.pack(expand = True)

displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=200,
                                        text='Unfortunately that code is not correct. Please close this window then try again to enter the code correctly or close the window and send a new code by pressing "Email security key" again')
displaymessage.pack()

u_error_page.mainloop()
