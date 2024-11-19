import customtkinter as ctk

janela = ctk.CTk()


janela.geometry('500x500')

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


text = ctk.CTkLabel(janela,text= "flamengo e horrivel")
text.pack()
text.place(x=225,y=100)

imput = ctk.CTkEntry(janela,placeholder_text=("flamengo e ruim"))
imput.pack()
janela.mainloop()