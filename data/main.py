from scrapping import Scrapping
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='darkly')
root.title('Salvar Notas')
root.geometry('500x300')
root.resizable(False, False)
root.iconbitmap('./images/SESI.ico')

estilo = tb.Style()
estilo.configure('success.TButton', font=('Bahnschrift', 26))


label_login = tb.Label(text='LOGIN:',
                              font=('Bahnschrift light', 26),
                              bootstyle=(INFO))
label_login.place(x=30,
                y=10)

entry_login = tb.Entry(root,
                       bootstyle=DARK,
                       font=('Comic Sans', 20))
entry_login.place(x=170,
                  y=10)

label_senha = tb.Label(text='SENHA:',
                              font=('Bahnschrift light', 26),
                              bootstyle=(INFO))
label_senha.place(x=30,
                y=100)

entry_senha = tb.Entry(root,
                       bootstyle=DARK,
                       font=('Comic Sans', 20))
entry_senha.place(x=170,
                  y=100)

botao_logar = tb.Button(text='LOGAR',
                        bootstyle='success',
                        width=12,
                        style='success.TButton')
botao_logar.place(x=130,
                  y=200)

root.mainloop()