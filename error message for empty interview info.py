import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

u_error_page = customtkinter.CTk()
u_error_page.title('Interview info entry empty') 
u_error_page.geometry('400x200') 

topframe = customtkinter.CTkFrame(u_error_page)
topframe.pack(expand = True)

displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=200,
                                        text='Unfortunately you have not entered any information about yourself (such as your CV) or any job information. Please enter some information then press continue again')
displaymessage.pack()

u_error_page.mainloop()