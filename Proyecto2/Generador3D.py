


class Generador3D:
    def __init__(self):
        self.temporales = 0
        self.etiquetas = 0
        self.codigo = ""
        self.main = ""
        self.funciones = ""


    
    def obtenerTemporal(self):
        temp = 't'+self.temporales.__str__()
        self.temporales += 1
        return temp



    def obtenerEtiqueta(self):
        et = 'L'+self.etiquetas.__str__()
        self.etiquetas += 1
        return et



    def generarEncabezado(self):
        encabezado = ''
        encabezado += '''
#include <stdio.h>
#include <math.h>
float Stack[10000];
float Heap[10000];
int SP = 0;
int HP = 0;

'''
        if self.temporales > 0:
            encabezado += "float "
        for i in range(0, self.temporales):
            if i % 15 == 0 and i > 0:
                encabezado += "\n"
            encabezado += f"t{i}"
            if i < self.temporales - 1:
                encabezado += ", "
            
        if self.temporales > 0:
            encabezado += '; \n\n'
        
        return encabezado



    def agregarInstruccion(self,codigo):
        if(codigo != None):
            self.main += codigo + '\n'



    def generarMain(self):
        codigo = self.generarEncabezado()
        codigo += self.codigo +'\n'
        codigo += self.funciones
        codigo += "int main(){ \n" \
                  f"{self.main} \n" \
                  f"    return 0;" \
                  "\n}"
        return codigo



    def agregarFuncion(self,codigo):
        self.funciones += codigo
        self.funciones += "\n"



    def reiniciarGenerador(self):
        self.temporales = 0
        self.etiquetas = 0
        self.codigo = ""
        self.funciones = ""
        self.main = ""


