import tkinter as tk 
from tkinter import *



class WindowMain():
    def __init__(self, titulo, largura, altura):
        self.root = Tk()
        self.root.geometry(f"{largura}x{altura}")
        
        self.framePrimeiro()
        
        self.root.mainloop()
    def framePrimeiro(self):
        self.frame =  Frame(self.root, width=500, height=200)
        
        self.lbl1 = Label(self.frame,text='Valor:')
        self.inp_valor = Entry(self.frame, width=12)
        self.spin_src = Spinbox(
            self.frame, values=['BTC','USD','BRL'],width=7)
        self.spin_dst = Spinbox(
            self.frame, values=['BTC','USD','BRL'],width=7)
        self.lbl_2 = Label(self.frame, text='->')
        
        self.btn_converte = Button(
            self.frame, text='Converter', command=self.converterMoedas,
            relief='flat')
        
        self.frame.pack()    
        
        self.lbl1.place(x=10, y=40)
        self.inp_valor.place(x=60, y=40)
        self.spin_src.place(x=170, y=40)
        self.lbl_2.place(x=250, y=40)
        self.spin_dst.place(x=280, y=40)
        self.btn_converte.place(x=360, y=38)
    
    
    def converterMoedas(self):
        self.valor = self.inp_valor.get()
        self.origen = self.spin_src.get()
        self.destino = self.spin_dst.get()
        print(self.valor)
        print(self.origen)
        print(self.destino)
if __name__ == "__main__":
    window = WindowMain("Cotação", 500,400)
