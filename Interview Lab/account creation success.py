import customtkinter
from PIL import Image

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')

u_error_page = customtkinter.CTk()
u_error_page.title('Account creation success') 
u_error_page.geometry('600x400') 

topframe = customtkinter.CTkFrame(u_error_page)
topframe.place(x=50,y=50)

toptopframe = customtkinter.CTkFrame(u_error_page,
                                     width=560,
                                     height=50)
toptopframe.place(x=20,y=0)

title_font = customtkinter.CTkFont(size=30,weight="bold",family='Roboto', underline=True)

title = customtkinter.CTkLabel(toptopframe,
                               font=title_font,
                               text="Account created",
                               text_color="blue",
                               width=500)
title.place(x=0,y=0)

displaymessage = customtkinter.CTkLabel(master=topframe,
                                        wraplength=500,
                                        text='Congratulations on creating a new account on Interview lab! Please close this window and follow the on screen instructions')
displaymessage.pack()


logoimage = customtkinter.CTkImage(light_image=Image.open("Celebration of account.png"),
size=(400,275))

logoframe = customtkinter.CTkFrame(u_error_page,
                                width=400,
                                height=275)
logoframe.place(x=100,y=100)

imagelabel = customtkinter.CTkLabel(logoframe,
                                    image=logoimage,
                                    text="")
imagelabel.place(x=0,y=0)


u_error_page.mainloop()
