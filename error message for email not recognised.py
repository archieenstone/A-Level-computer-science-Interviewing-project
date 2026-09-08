import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

u_error_page = customtkinter.CTk()
u_error_page.title('Email not recognised report') 
u_error_page.geometry('400x200') 

topframe = customtkinter.CTkFrame(u_error_page)
topframe.pack(expand = True)

displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=200,
                                        text='Unfortunately the email recognised is not recognised. Please check the details of your email and try again')
displaymessage.pack()

u_error_page.mainloop()
