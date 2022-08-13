from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

#from flask import g

import Gramatica.gramatica as g
from Entorno.EntornoTabla import EntornoTabla


class Adriana:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('1100x750')
        self.ventana.configure(bg = 'pink')
        self.ventana.title('Proyecto 1 - Compiladores 2')


        #----------------------------------- BARRA MENU ----------------------------------------------
        barra = Menu(self.ventana)
        barra.activate
        #creando cada menu
        menu_Ejecutar = Menu(barra)
        menu_Reportes = Menu(barra)
        menu_AcercaDe = Menu(barra)

        #crear comandos de los menu
        menu_Ejecutar.add_command(label = 'Compilar', command = self.ejecutar)

        menu_Reportes.add_command(label = 'Tabla de simbolos')
        menu_Reportes.add_command(label = 'Tabla de Errores')
        menu_Reportes.add_command(label = 'Tablas de BD')
        menu_Reportes.add_command(label = 'BD existentes')

        menu_AcercaDe.add_command(label = 'Info',  command = self.muestra_info)

        #agregar menu en cascada
        barra.add_cascade(label = 'Ejecutar', menu = menu_Ejecutar)
        barra.add_cascade(label = 'Reportes', menu = menu_Reportes)
        barra.add_cascade(label = 'Acerca de', menu = menu_AcercaDe)

        #agregar la barra a la ventana
        self.ventana.config(menu = barra)







        #----------------------------------- COMPONENTES ----------------------------------------------
        etiqueta = Label(self.ventana, text = 'es de noche')
        #etiqueta.pack(side = RIGHT)
        btnPrueba = Button(self.ventana, text = 'presiona')#, command = self.presiona_boton)
        #btnPrueba.pack()

        #Textbox entrada y salida        
        Tipo_Fuente = tkFont.Font(family='Comic Sans MS', size=10)
        lblEntrada = Label(self.ventana, text='Entrada', bg='pink', font='courier, 15')
        lblEntrada.place(x=20, y=25)
        self.txtEntrada = Text(self.ventana, font=Tipo_Fuente)
        self.txtEntrada.place(x=20, y=50, width=500, height=650)

        lblSalida = Label(self.ventana, text = 'Salida', bg = 'pink',  font = 'courier, 15')
        lblSalida.place(x=550, y=25)
        self.txtSalida = Text(self.ventana, bg = 'black', fg = 'white', font=Tipo_Fuente)
        self.txtSalida.place(x=550, y=50, width=500, height=650)








    def muestra_info(self):
        messagebox.showinfo(message = 'Adriana Marié Gómez Dávila \n201504236 \nProyecto 1 \nCompiladores 2', title = 'Información')

    def ejecutar(self):
        texto = self.txtEntrada.get(1.0, END)

        self.txtSalida.delete('1.0', 'end')
        ENTORNO_RAIZ = EntornoTabla(None)

        if texto != '':
            resultado = g.parse(texto)
            for i in resultado:
                i.ejecutarInstruccion(ENTORNO_RAIZ, self.txtSalida)





if __name__ == "__main__":
    ventana = Tk()
    aplicacion = Adriana(ventana)
    ventana.mainloop()


