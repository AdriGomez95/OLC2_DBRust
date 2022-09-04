from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from AST.Definicion.Objetos.GuardarClase import GuardarClase
from AST.ReporteTS.ReporteTS import ReporteTS
from Entorno.Simbolos.Funcion import Funcion

#from flask import g

import Gramatica.gramatica as g
from Entorno.EntornoTabla import EntornoTabla
from AST.Errores.CustomError import CustomError

MisErrores = []
MisSimbolosTS = []
MisDB = []

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

        menu_Reportes.add_command(label = 'Tabla de simbolos', command = self.genera_tabla_simbolos)
        menu_Reportes.add_command(label = 'Tabla de Errores',  command = self.genera_reporte_errores)
        menu_Reportes.add_command(label = 'Tablas de BD', command = self.genera_tabla_db)
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




    def genera_tabla_db(self):
        textoSim = """<table class="container"><tbody>"""
        for i in range(len(MisDB)):
            textoSim += """<tr><td>"""
            textoSim += MisDB[i] 
            textoSim += """</td></tr> <br></br>"""
            #print(MisErrores[i])

        textoSim += """</tbody></table>"""

        archivo = open("Tablas_DB.html", "w")
        #texto = "\"mis perritos estan durmiendo\""
        

        texto2 = """<!DOCTYPE html>
                        <html lang="es">

                        <head>
                            <meta charset="utf-8" />
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1" />
                            <meta name="viewport" content="initial-scale=1, maximum-scale=1">
                            <title>Tablas en Base de Datos</title>
                            <style>
                                @charset "UTF-8";
                                @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);

                                body {
                                    font-family: 'Open Sans', sans-serif;
                                    font-weight: 300;
                                    line-height: 1.42em;
                                    color: #A7A1AE;
                                    background-color: #02B2B5;
                                }

                                h1 {
                                    font-size: 3em;
                                    font-weight: 300;
                                    line-height: 1em;
                                    text-align: center;
                                    color: #000000;
                                }

                                h2 {
                                    font-size: 1em;
                                    font-weight: 300;
                                    text-align: center;
                                    display: block;
                                    line-height: 1em;
                                    padding-bottom: 2em;
                                    color: #FB667A;
                                }

                                h2 a {
                                    font-weight: 700;
                                    text-transform: uppercase;
                                    color: #FB667A;
                                    text-decoration: none;
                                }

                                .blue {
                                    color: #185875;
                                }

                                .yellow {
                                    color: #FFF842;
                                }

                                .container th h1 {
                                    font-weight: bold;
                                    font-size: 1em;
                                    text-align: left;
                                    color: #185875;
                                }

                                .container td {
                                    font-weight: normal;
                                    font-size: 1em;
                                    -webkit-box-shadow: 0 2px 2px -2px #0E1119;
                                    -moz-box-shadow: 0 2px 2px -2px #0E1119;
                                    box-shadow: 0 2px 2px -2px #0E1119;
                                }

                                .container {
                                    text-align: left;
                                    overflow: hidden;
                                    width: 80%;
                                    margin: 0 auto;
                                    display: table;
                                    padding: 0 0 8em 0;
                                }

                                .container td,
                                .container th {
                                    padding-bottom: 2%;
                                    padding-top: 2%;
                                    padding-left: 2%;
                                }

                                /* Background-color of the odd rows */
                                .container tr:nth-child(odd) {
                                    background-color: #ffffff;
                                }

                                /* Background-color of the even rows */
                                .container tr:nth-child(even) {
                                    background-color: #2AA1B4;
                                }

                                .container th {
                                    background-color: #1F2739;
                                }

                                .container td:first-child {
                                    color: #000000;
                                }

                                .container tr:hover {
                                    background-color: #464A52;
                                    -webkit-box-shadow: 0 6px 6px -6px #0E1119;
                                    -moz-box-shadow: 0 6px 6px -6px #0E1119;
                                    box-shadow: 0 6px 6px -6px #0E1119;
                                }

                                .container td:hover {
                                    background-color: #FFF842;
                                    color: #403E10;
                                    font-weight: bold;

                                    box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
                                    transform: translate3d(6px, -6px, 0);

                                    transition-delay: 0s;
                                    transition-duration: 0.4s;
                                    transition-property: all;
                                    transition-timing-function: line;
                                }

                                @media (max-width: 800px) {

                                    .container td:nth-child(4),
                                    .container th:nth-child(4) {
                                        display: none;
                                    }
                                }
                            </style>
                        </head>

                        <body>
                        <h1> Tabla de simbolos </h1>
                        <br></br>"""
        texto2 += textoSim
        texto2 += """        </table>
                        </body>
                    </html>""" 
        archivo.write(texto2)
        archivo.close()




    def genera_tabla_simbolos(self):
        textoSim = """<table class="container"><tbody>"""
        for i in range(len(MisSimbolosTS)):
            textoSim += """<tr><td>"""
            textoSim += MisSimbolosTS[i] 
            textoSim += """</td></tr> <br></br>"""
            #print(MisErrores[i])

        textoSim += """</tbody></table>"""

        archivo = open("Tabla_Simbolos.html", "w")
        #texto = "\"mis perritos estan durmiendo\""
        

        texto2 = """<!DOCTYPE html>
                        <html lang="es">

                        <head>
                            <meta charset="utf-8" />
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1" />
                            <meta name="viewport" content="initial-scale=1, maximum-scale=1">
                            <title>Tabla de Simbolos</title>
                            <style>
                                @charset "UTF-8";
                                @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);

                                body {
                                    font-family: 'Open Sans', sans-serif;
                                    font-weight: 300;
                                    line-height: 1.42em;
                                    color: #A7A1AE;
                                    background-color: #02B2B5;
                                }

                                h1 {
                                    font-size: 3em;
                                    font-weight: 300;
                                    line-height: 1em;
                                    text-align: center;
                                    color: #000000;
                                }

                                h2 {
                                    font-size: 1em;
                                    font-weight: 300;
                                    text-align: center;
                                    display: block;
                                    line-height: 1em;
                                    padding-bottom: 2em;
                                    color: #FB667A;
                                }

                                h2 a {
                                    font-weight: 700;
                                    text-transform: uppercase;
                                    color: #FB667A;
                                    text-decoration: none;
                                }

                                .blue {
                                    color: #185875;
                                }

                                .yellow {
                                    color: #FFF842;
                                }

                                .container th h1 {
                                    font-weight: bold;
                                    font-size: 1em;
                                    text-align: left;
                                    color: #185875;
                                }

                                .container td {
                                    font-weight: normal;
                                    font-size: 1em;
                                    -webkit-box-shadow: 0 2px 2px -2px #0E1119;
                                    -moz-box-shadow: 0 2px 2px -2px #0E1119;
                                    box-shadow: 0 2px 2px -2px #0E1119;
                                }

                                .container {
                                    text-align: left;
                                    overflow: hidden;
                                    width: 80%;
                                    margin: 0 auto;
                                    display: table;
                                    padding: 0 0 8em 0;
                                }

                                .container td,
                                .container th {
                                    padding-bottom: 2%;
                                    padding-top: 2%;
                                    padding-left: 2%;
                                }

                                /* Background-color of the odd rows */
                                .container tr:nth-child(odd) {
                                    background-color: #ffffff;
                                }

                                /* Background-color of the even rows */
                                .container tr:nth-child(even) {
                                    background-color: #2AA1B4;
                                }

                                .container th {
                                    background-color: #1F2739;
                                }

                                .container td:first-child {
                                    color: #000000;
                                }

                                .container tr:hover {
                                    background-color: #464A52;
                                    -webkit-box-shadow: 0 6px 6px -6px #0E1119;
                                    -moz-box-shadow: 0 6px 6px -6px #0E1119;
                                    box-shadow: 0 6px 6px -6px #0E1119;
                                }

                                .container td:hover {
                                    background-color: #FFF842;
                                    color: #403E10;
                                    font-weight: bold;

                                    box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
                                    transform: translate3d(6px, -6px, 0);

                                    transition-delay: 0s;
                                    transition-duration: 0.4s;
                                    transition-property: all;
                                    transition-timing-function: line;
                                }

                                @media (max-width: 800px) {

                                    .container td:nth-child(4),
                                    .container th:nth-child(4) {
                                        display: none;
                                    }
                                }
                            </style>
                        </head>

                        <body>
                        <h1> Tabla de simbolos </h1>
                        <br></br>"""
        texto2 += textoSim
        texto2 += """        </table>
                        </body>
                    </html>""" 
        archivo.write(texto2)
        archivo.close()




    def genera_reporte_errores(self):
        textoError = """<table class="container"><tbody>"""
        for i in range(len(MisErrores)):
            textoError += """<tr><td>"""
            textoError += MisErrores[i] 
            textoError += """</td></tr> <br></br>"""
            #print(MisErrores[i])

        textoError += """</tbody></table>"""

        archivo = open("Reporte_Errores.html", "w")
        #texto = "\"mis perritos estan durmiendo\""
        

        texto = """<!DOCTYPE html>
                        <html lang="es">

                        <head>
                            <meta charset="utf-8" />
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1" />
                            <meta name="viewport" content="initial-scale=1, maximum-scale=1">
                            <title>Reporte de Errores</title>
                            <style>
                                @charset "UTF-8";
                                @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);

                                body {
                                    font-family: 'Open Sans', sans-serif;
                                    font-weight: 300;
                                    line-height: 1.42em;
                                    color: #A7A1AE;
                                    background-color: #02B2B5;
                                }

                                h1 {
                                    font-size: 3em;
                                    font-weight: 300;
                                    line-height: 1em;
                                    text-align: center;
                                    color: #000000;
                                }

                                h2 {
                                    font-size: 1em;
                                    font-weight: 300;
                                    text-align: center;
                                    display: block;
                                    line-height: 1em;
                                    padding-bottom: 2em;
                                    color: #FB667A;
                                }

                                h2 a {
                                    font-weight: 700;
                                    text-transform: uppercase;
                                    color: #FB667A;
                                    text-decoration: none;
                                }

                                .blue {
                                    color: #185875;
                                }

                                .yellow {
                                    color: #FFF842;
                                }

                                .container th h1 {
                                    font-weight: bold;
                                    font-size: 1em;
                                    text-align: left;
                                    color: #185875;
                                }

                                .container td {
                                    font-weight: normal;
                                    font-size: 1em;
                                    -webkit-box-shadow: 0 2px 2px -2px #0E1119;
                                    -moz-box-shadow: 0 2px 2px -2px #0E1119;
                                    box-shadow: 0 2px 2px -2px #0E1119;
                                }

                                .container {
                                    text-align: left;
                                    overflow: hidden;
                                    width: 80%;
                                    margin: 0 auto;
                                    display: table;
                                    padding: 0 0 8em 0;
                                }

                                .container td,
                                .container th {
                                    padding-bottom: 2%;
                                    padding-top: 2%;
                                    padding-left: 2%;
                                }

                                /* Background-color of the odd rows */
                                .container tr:nth-child(odd) {
                                    background-color: #ffffff;
                                }

                                /* Background-color of the even rows */
                                .container tr:nth-child(even) {
                                    background-color: #2AA1B4;
                                }

                                .container th {
                                    background-color: #1F2739;
                                }

                                .container td:first-child {
                                    color: #000000;
                                }

                                .container tr:hover {
                                    background-color: #464A52;
                                    -webkit-box-shadow: 0 6px 6px -6px #0E1119;
                                    -moz-box-shadow: 0 6px 6px -6px #0E1119;
                                    box-shadow: 0 6px 6px -6px #0E1119;
                                }

                                .container td:hover {
                                    background-color: #FFF842;
                                    color: #403E10;
                                    font-weight: bold;

                                    box-shadow: #7F7C21 -1px 1px, #7F7C21 -2px 2px, #7F7C21 -3px 3px, #7F7C21 -4px 4px, #7F7C21 -5px 5px, #7F7C21 -6px 6px;
                                    transform: translate3d(6px, -6px, 0);

                                    transition-delay: 0s;
                                    transition-duration: 0.4s;
                                    transition-property: all;
                                    transition-timing-function: line;
                                }

                                @media (max-width: 800px) {

                                    .container td:nth-child(4),
                                    .container th:nth-child(4) {
                                        display: none;
                                    }
                                }
                            </style>
                        </head>

                        <body>
                        <h1> Reporte de errores </h1>
                        <br></br>"""
        texto += textoError
        texto += """        </table>
                        </body>
                    </html>""" 
        archivo.write(texto)
        archivo.close()














    def muestra_info(self):
        messagebox.showinfo(message = 'Adriana Marié Gómez Dávila \n201504236 \nProyecto 1 \nCompiladores 2', title = 'Información')

    def ejecutar(self):
        texto = self.txtEntrada.get(1.0, END)

        self.txtSalida.delete('1.0', 'end')
        ENTORNO_RAIZ = EntornoTabla(self.txtSalida, None)

        if texto != '':
            AST = g.parse(texto)
            
            listaErrores = g.getErrores()
            for err_ in listaErrores:
                v:CustomError = err_
                #self.txtSalida.insert(END,v.toString()+"\n")
                MisErrores.append(v.toString())
            
            listaTS = g.getreporteTS()
            for ts_ in listaTS:
                c:ReporteTS = ts_
                MisSimbolosTS.append(c.toString())

            listaDB = g.getreporteDB()
            for db_ in listaDB:
                m:ReporteTS = db_
                MisDB.append(m.toString())

            #PASADA 1 PARA GUARDAR LAS INSTRUCCIONES
            for i in AST.listaInstrucciones:
                #validar tipos de instrucciones
                if isinstance(i, Funcion):
                    existeFuncion = ENTORNO_RAIZ.existeFuncion(i.identificador)
                
                    if not existeFuncion:
                        ENTORNO_RAIZ.agregarFuncion(i)

                
                elif isinstance(i, GuardarClase):
                    i.ejecutarInstruccion(ENTORNO_RAIZ)



            #PASADA 2 PARA EJECUTAR EL MAIN
            if ENTORNO_RAIZ.existeFuncion("main"):
                funcionMain = ENTORNO_RAIZ.obtenerFuncion("main")
                funcionMain.ejecutarInstruccion(ENTORNO_RAIZ)
            else:
                print(f"Error semantico, no existe funcion main")





if __name__ == "__main__":
    ventana = Tk()
    aplicacion = Adriana(ventana)
    ventana.mainloop()


