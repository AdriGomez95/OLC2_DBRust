from enum import  IntEnum


class TIPO_DATO(IntEnum):
    ENTERO = 0,
    DECIMAL = 1,
    CADENA = 2,
    BOOLEAN = 3,
    VOID = 4,
    NULL = 5,
    CADENA2 = 6,
    CHAR = 7,
    FN = 8,
    OBJETO = 9,
    ARRAY = 10,
    VECTOR = 11,
    STRUCT = 12,
    BREAK = 13,
    CONTINUE_STR = 14


class RetornoType:
    
    def __init__(self, tipo=TIPO_DATO.NULL):
        self.codigo = ""
        self.etiqueta = ""
        self.temporal = ""
        self.tipo = tipo
        self.etiquetaV = ""
        self.etiquetaF = ""
        self.valor = None

    def iniciarRetorno(self, codigo, etiqueta, temporal, tipo):
        self.codigo = codigo
        self.temporal = temporal
        self.etiqueta = etiqueta
        self.tipo = tipo

    def iniciarRetornoInstancia(self, codigo, temporal, tipo, OBJETO):
        self.codigo = codigo
        self.temporal = temporal
        self.tipo = tipo
        self.valor = OBJETO
