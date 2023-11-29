from scrapping import Scrapping
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename='darkly')
root.title('Salvar Notas')
root.geometry('600x350')
root.resizable(False, False)
root.iconbitmap('./images/SESI.ico')

label_inserir_info = tb.Label(text='Insira seu login e senha:',
                              font=('Bahnschrift light', 26),
                              bootstyle=LIGHT)
label_inserir_info.place(x=100,
                         y=20)

root.mainloop()