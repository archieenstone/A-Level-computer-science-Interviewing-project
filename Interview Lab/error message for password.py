import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

u_error_page = customtkinter.CTk()
u_error_page.title('Password error report') 
u_error_page.geometry('400x200') 

topframe = customtkinter.CTkFrame(u_error_page)
topframe.pack(expand = True)

displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=200,
                                        text='Unfortunately that password is not acceptable. The password must be at least 8 characters long, contain at least 1 number and contain a special character ([@_!#$%^&*()<>?/}{~:]). Please close this window and enter a more acceptable password to continue to your interview practice')
displaymessage.pack()

u_error_page.mainloop()
