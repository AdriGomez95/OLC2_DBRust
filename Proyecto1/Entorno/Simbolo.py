from Entorno.RetornoType import TIPO_DATO


class Simbolo:

    def __init__(self):
        self.linea = 0
        self.columna = 0
        self.identificador = ""
        self.valor = None
        self.tipo = TIPO_DATO.NULL
        self.constante = False

        self.parametros = []
        self.instrucciones =[]



        # simbolo de instancia
        self.idClase = ""
        self.entornoInstancia = None


        # referencia
        self.entornoReferencia = None
        self.valorReferencia = None

    def iniciarSimboloPrimitivo(self, identificador, valor, tipo, constante=False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.constante = constante


    def iniciarSimboloFuncion(self, identificador, listaParametros, listaInstrucciones, tipo):
        self.identificador = identificador
        self.parametros = listaParametros
        self.instrucciones = listaInstrucciones
        self.tipo = tipo


    def iniciarSimboloClase(self, idClase, listaInstrucciones):
        self.identificador = idClase
        self.instrucciones = listaInstrucciones


    def iniciarSimboloInstancia(self, idClase, idInstancia, entornoInstancia, tipo):
        self.idClase = idClase
        self.identificador = idInstancia
        self.entornoInstancia = entornoInstancia
        self.tipo = tipo

    def iniciarSimboloArreglo(self, tipo, dimensiones, valores):
        self.dimensiones =dimensiones
        self.valores = valores
        self.tipo = tipo

    def iniciarSimboloVector(self,nombreVectorcito, tipo, valores, tamanioVectorcito):
        self.nombreVectorcito = nombreVectorcito
        self.valores = valores
        self.tipo = tipo
        self.tamanioVectorcito = tamanioVectorcito

