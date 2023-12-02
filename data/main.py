from main_scrapping import Scrapping
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb

def exec_botao():
    login = entry_login.get()
    senha = entry_senha.get()
    ano = combo.get()

    if 'Ano' not in ano:
        messagebox.showerror('ERRO', 'Selecione um ano válido')
    else:
        Scrapping(login, senha, ano)

root = tb.Window(themename='darkly')
root.title('Salvar Notas')
root.geometry('500x400+200+200')
root.resizable(False, False)
root.iconbitmap('./images/SESI.ico')

estilo = tb.Style()
estilo.configure('success.TButton', font=('Bahnschrift', 26))


label_login = tb.Label(text='LOGIN:',
                              font=('Bahnschrift light', 26),
                              bootstyle=(INFO))
label_login.place(x=30,
                y=20)

entry_login = tb.Entry(root,
                       bootstyle=DARK,
                       font=('Comic Sans', 20))
entry_login.place(x=170,
                  y=20)

label_senha = tb.Label(text='SENHA:',
                              font=('Bahnschrift light', 26),
                              bootstyle=(INFO))
label_senha.place(x=28,
                y=100)

entry_senha = tb.Entry(root,
                       bootstyle=DARK,
                       font=('Comic Sans', 20))
entry_senha.place(x=170,
                  y=100)


label_ano = tb.Label(text='ANO:',
                              font=('Bahnschrift light', 26),
                              bootstyle=(INFO))
label_ano.place(x=28,
                y=170)
anos = ['1ª Série', '2ª Série', '3ª Série']

combo = tb.Combobox(root,
                    bootstyle=LIGHT,
                    values=anos)
combo.current(0)
combo.place(x=170,
            y=181)

botao_logar = tb.Button(text='LOGAR',
                        bootstyle='success',
                        width=12,
                        style='success.TButton',
                        command=exec_botao)
botao_logar.place(x=125,
                  y=300)

root.mainloop()