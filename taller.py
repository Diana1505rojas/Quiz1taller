#Diana Sofia Rojas-Mateo R3strepo Hincapie
from datetime import datetime
#se creo la clas implante medico con los atributos geenrales que tendran todos los implantes
class ImplanteMedico:
    def __init__(self, tipo, material, tamaño):
        self.__tipo = tipo
        self.__material = material
        self.__tamaño = tamaño
        self.__fecha_implantacion = None
        self.__medico_responsable = None
        self.__estado = None

    def __str__(self):
        return f"Tipo: {self.__tipo}\nMaterial: {self.__material}\nTamaño: {self.__tamaño}\nFecha de Implante: {self.__fecha_implantacion}\nMédico Responsable: {self.__medico_responsable}\nEstado: {self.__estado}"
#   se sobreescribe el metodo str para imprimir en pantalla un objeto de la clase ImplanteMedico

    def get_tipo(self):
        return self.__tipo
# se definen los getters y se   establecen las reglas de acceso a los atributos privados del objeto
# se defines los setters para  poder asignarle valores a esos atributos privados desde fuera de la clase
    def get_material(self):
        return self.__material

    def get_tamaño(self):
        return self.__tamaño

    def get_fecha_implantacion(self):
        return self.__fecha_implantacion

    def set_fecha_implantacion(self, fecha):
        self.__fecha_implantacion = fecha

    def get_medico_responsable(self):
        return self.__medico_responsable

    def set_medico_responsable(self, medico):
        self.__medico_responsable = medico

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

# se define una funcion que permite agregar un nuevo implante al sistema

# se creo la clase de marcapasos               
class Marcapasos(ImplanteMedico):
    def __init__(self, material, tamaño, electrodos, alambrico, frecuencia_estimulacion):
        super().__init__("Marcapasos", material, tamaño)
        self.__electrodos = electrodos
        self.__alambrico = alambrico
        self.__frecuencia_estimulacion = frecuencia_estimulacion

    def __str__(self):
        return f"{super().__str__()}\nElectrodos: {self.__electrodos}\nAlambrico: {self.__alambrico}\nFrecuencia de Estimulación: {self.__frecuencia_estimulacion}"

    def get_electrodos(self):
        return self.__electrodos

    def get_alambrico(self):
        return self.__alambrico

    def get_frecuencia_estimulacion(self):
        return self.__frecuencia_estimulacion
    
# los gettters  y setter de marcapasos heredan de ImplanteMedico
    # por lo tanto no es necesario  volver a definirlos en esta clase