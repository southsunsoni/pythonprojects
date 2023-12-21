import main as MAin
import tkinter as tk
from tkinter import *
def Game(cardre):
    pass
window=Tk()
window.geometry('400x400')
window.title('serpent')
window['bg']='red'
window.resizable(height=False,width=False)
botton1=Button(window,text='◄',bg='blue').place(x=150,y=350)
botton2=Button(window,text='►',bg='blue').place(x=250,y=350)
botton3=Button(window,text='▲',bg='blue').place(x=200,y=320)
botton4=Button(window,text='▼',bg='blue').place(x=200,y=370)
cardre_jeux=tk.Frame(window,width=400,height=200,bg="white")
cardre_jeux.place(x=0,y=50)

window.mainloop()