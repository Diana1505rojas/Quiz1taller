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

# la clase  Stentcoronario  en  hereda tambien de ImplanteMedico pero con la adicionalidad de tener atributos propios
    def __init__(self, material, tamaño, longitud, diametro):
        super().__init__("Stent Coronario", material, tamaño)
        self.__longitud = longitud
        self.__diametro = diametro

    def __str__(self):
        return f"{super().__str__()}\nLongitud: {self.__longitud}\nDiámetro: {self.__diametro}"

    def get_longitud(self):
        return self.__longitud

    def get_diametro(self):
        return self.__diametro
    

# la clase de implante dental  tiene como padre a la clase de Implantable
class ImplanteDental(ImplanteMedico):
    def __init__(self, material, tamaño, forma, sistema_fijacion):
        super().__init__("Implante Dental", material, tamaño)
        self.__forma = forma
        self.__sistema_fijacion = sistema_fijacion

# se utiliza el metodo str de la clase padre para mostrar los atributos comunes a ambas clases
    def __str__(self):
        return f"{super().__str__()}\nForma: {self.__forma}\nSistema de Fijación: {self.__sistema_fijacion}"

    def get_forma(self):
        return self.__forma

    def get_sistema_fijacion(self):
        return self.__sistema_fijacion

# la clase EsmalteDental hereda de la clase ImplanteDental pero sobreescribe al método __str__
# para que muestre información adicional especifica de ella
    

 
class ImplanteRodilla(ImplanteMedico):
    def __init__(self, material, tamaño, tipo_fijacion):
        super().__init__("Implante de Rodilla", material, tamaño)
        self.__tipo_fijacion = tipo_fijacion

# se llama al método __str__ de la clase padre y se le agregan  los atributos nuevos  de esta clase

    def __str__(self):
        return f"{super().__str__()}\nTipo de Fijación: {self.__tipo_fijacion}"

    def get_tipo_fijacion(self):
        return self.__tipo_fijacion
    
    # el def__init__  es igual al de la clase padre con la diferencia de que se le agrega un tercer parametro

class ProtesisCadera(ImplanteMedico):
    def __init__(self, material, tamaño, tipo_fijacion):
        super().__init__("Prótesis de Cadera", material, tamaño)
        self.__tipo_fijacion = tipo_fijacion

    def __str__(self):
        return f"{super().__str__()}\nTipo de Fijación: {self.__tipo_fijacion}"

    def get_tipo_fijacion(self):
        return self.__tipo_fijacion
    
# la class paciente  tiene todos los metodos de la clase PacienteMedico mas uno nuevo llamado mostrar_implantes
class Paciente:
    def __init__(self, nombre, id_paciente):
        self.__nombre = nombre
        self.__id_paciente = id_paciente
        self.__implantes_asociados = []

    def asignar_implante(self, implante, fecha_implantacion, medico_responsable, estado):
        implante.set_fecha_implantacion(fecha_implantacion)
        implante.set_medico_responsable(medico_responsable)
        implante.set_estado(estado)
        self.__implantes_asociados.append(implante)

# def asignar implante esta bien porque  no hay conflicto entre las funciones del mismo nombre en las clases hijas

    def __str__(self):
        implantes = "\n".join([f"- {implante.get_tipo()}" for implante in self.__implantes_asociados])
        return f"Nombre: {self.__nombre}\nID: {self.__id_paciente}\nImplantes asociados:\n{implantes}"

    def get_nombre(self):
        return self.__nombre

    def get_id_paciente(self):
        return self.__id_paciente

    def get_implantes_asociados(self):
        return self.__implantes_asociados
    
# los getters  y setter son metodos que permiten manipular las propiedades privadas de una clase


    



