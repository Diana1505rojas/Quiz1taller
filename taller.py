#Diana Sofia Rojas-Mateo Restrepo Hincapie
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
class StentCoronario(ImplanteMedico):
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
    

class SistemaGestionImplantes:
    def __init__(self):
        self.__implantes = []
        self.__pacientes = []

# la class sistemagestionimplantes  es un singleton porque tiene un constructor privado y  se accede a ella mediante el metodo get

    def agregar_implante(self, implante):
        self.__implantes.append(implante)

    def eliminar_implante(self, index):
        if index < len(self.__implantes):
            del self.__implantes[index]


    def editar_implante(self, index):
        if index < len(self.__implantes):
            implante = self.__implantes[index]
            print("Información actual del implante:")
            print(implante)
            material = input("Ingrese el nuevo material: ")
            tamaño = input("Ingrese el nuevo tamaño: ")

                # Editar los atributos específicos según el tipo de implante
            if isinstance(implante, Marcapasos):
                electrodos = int(input("Ingrese el nuevo número de electrodos: "))
                alambrico = input("¿Es alámbrico? (s/n): ").lower() == "s"
                frecuencia_estimulacion = input("Ingrese la nueva frecuencia de estimulación: ")
                self.__implantes[index] = Marcapasos(material, tamaño, electrodos, alambrico, frecuencia_estimulacion)
            elif isinstance(implante, StentCoronario):
                    longitud = input("Ingrese la nueva longitud: ")
                    diametro = input("Ingrese el nuevo diámetro: ")
                    self.__implantes[index] = StentCoronario(material, tamaño, longitud, diametro)
            elif isinstance(implante, ImplanteDental):
                    forma = input("Ingrese la nueva forma: ")
                    sistema_fijacion = input("Ingrese el nuevo sistema de fijación: ")
                    self.__implantes[index] = ImplanteDental(material, tamaño, forma, sistema_fijacion)
            elif isinstance(implante, ImplanteRodilla):
                    tipo_fijacion = input("Ingrese el nuevo tipo de fijación: ")
                    self.__implantes[index] = ImplanteRodilla(material, tamaño, tipo_fijacion)
            elif isinstance(implante, ProtesisCadera):
                    tipo_fijacion = input("Ingrese el nuevo tipo de fijación: ")
                    self.__implantes[index] = ProtesisCadera(material, tamaño, tipo_fijacion)
            else:
                    # Si no es un tipo específico conocido, simplemente actualiza material y tamaño
                    self.__implantes[index].__material = material
                    self.__implantes[index].__tamaño = tamaño
            print("Implante editado con éxito.")
        else:
                print("Número de implante inválido.")

    def visualizar_inventario(self):
        for i, implante in enumerate(self.__implantes, 1):
            print(f"{i}. {implante}")

    def registrar_paciente(self, paciente):
        self.__pacientes.append(paciente)

    def asignar_implante_a_paciente(self):
        print("Pacientes registrados:")
        for i, paciente in enumerate(self.__pacientes, 1):
            print(f"{i}. {paciente}")
        paciente_index = int(input("Seleccione el número del paciente: ")) - 1
        if paciente_index < len(self.__pacientes):
            paciente = self.__pacientes[paciente_index]
            print("Implantes disponibles para asignar:")
            self.visualizar_inventario()
            implante_index = int(input("Seleccione el número del implante a asignar: ")) - 1
            if implante_index < len(self.__implantes):
                implante = self.__implantes[implante_index]
                fecha_implantacion = datetime.now().strftime("%Y-%m-%d")
                medico_responsable = input("Ingrese el médico responsable: ")
                estado = input("Ingrese el estado del implante (activo/inactivo): ")
                paciente.asignar_implante(implante, fecha_implantacion, medico_responsable, estado)
                print("Implante asignado con éxito.")
            else:
                print("Número de implante inválido.")
        else:
            print("Número de paciente inválido.")   

    def mostrar_seguimiento_implantes(self):
        print("Seguimiento de Implantes:")
        for paciente in self.__pacientes:
            print(f"Paciente: {paciente.get_nombre()}")
            for implante in paciente.get_implantes_asociados():
                print(f"Implante: {implante.get_tipo()}, Fecha de Implantación: {implante.get_fecha_implantacion()}, Médico: {implante.get_medico_responsable()}, Estado: {implante.get_estado()}")

    #Se crearon los menus paras poder acceder a las clases y poder realizar las acciones
                    #se tiene primero el mdenu principal

if __name__ == "__main__":
    sistema_implantes = SistemaGestionImplantes()

    while True:
        print("----- Menú -----")
        print("1. Agregar implante")
        print("2. Eliminar implante")
        print("3. Editar información de implante")
        print("4. Visualizar inventario de implantes")
        print("5. Registrar paciente")
        print("6. Asignar implante a paciente")
        print("7. Mostrar seguimiento de implantes")
        print("8. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

#se creo otro menu para poder seleccionar el tipo de implante 
#el codigo funciona de la manera que primero se agrega un implante y se pueden agregar mas, ya despues se
# puede agregar un paciente y una vez agregado el paciente podemos agregarle un implante al paciente
#nos aparecera la lista de los pacientes guardados y una vez se seleccione el paciente nos aparecera la lista de 
#los implantes guardados y ya al seleccionar el implante este se guardara con el paciente que se selecciono.
        if opcion == "1":
            print("Tipos de implante:")
            print("1. Marcapasos")
            print("2. Stent Coronario")
            print("3. Implante Dental")
            print("4. Implante de Rodilla")
            print("5. Prótesis de Cadera")

#el siguiente es para poder realizar las opciones del menu anterior
            tipo_implante = input("Seleccione el tipo de implante: ")
            if tipo_implante == "1":
                material = input("Ingrese el material del marcapasos: ")
                tamaño = input("Ingrese el tamaño del marcapasos: ")
                electrodos = int(input("Ingrese el número de electrodos: "))
                alambrico = input("¿Es alámbrico? (s/n): ").lower() == "s"
                frecuencia_estimulacion = input("Ingrese la frecuencia de estimulación: ")
                implante = Marcapasos(material, tamaño, electrodos, alambrico, frecuencia_estimulacion)
            elif tipo_implante == "2":
                material = input("Ingrese el material del stent coronario: ")
                tamaño = input("Ingrese el tamaño del stent coronario: ")
                longitud = input("Ingrese la longitud del stent coronario: ")
                diametro = input("Ingrese el diámetro del stent coronario: ")
                implante = StentCoronario(material, tamaño, longitud, diametro)
            elif tipo_implante == "3":
                material = input("Ingrese el material del implante dental: ")
                tamaño = input("Ingrese el tamaño del implante dental: ")
                forma = input("Ingrese la forma del implante dental: ")
                sistema_fijacion = input("Ingrese el sistema de fijación del implante dental: ")
                implante = ImplanteDental(material, tamaño, forma, sistema_fijacion)
            elif tipo_implante == "4":
                material = input("Ingrese el material del implante de rodilla: ")
                tamaño = input("Ingrese el tamaño del implante de rodilla: ")
                tipo_fijacion = input("Ingrese el tipo de fijación del implante de rodilla: ")
                implante = ImplanteRodilla(material, tamaño, tipo_fijacion)
            elif tipo_implante == "5":
                material = input("Ingrese el material de la prótesis de cadera: ")
                tamaño = input("Ingrese el tamaño de la prótesis de cadera: ")
                tipo_fijacion = input("Ingrese el tipo de fijación de la prótesis de cadera: ")
                implante = ProtesisCadera(material, tamaño, tipo_fijacion)
            else:
                print("Opción inválida. Intente de nuevo.")
                continue
            sistema_implantes.agregar_implante(implante)
            print("Implante agregado con éxito.")

 #Para poder elimininar un implante
        elif opcion == "2":
            print("Implantes disponibles para eliminar:")
            sistema_implantes.visualizar_inventario()
            index = int(input("Ingrese el número del implante que desea eliminar: ")) - 1
            sistema_implantes.eliminar_implante(index)
            print("Implante eliminado con éxito.")
        elif opcion == "3":
            print("Implantes disponibles para editar:")
            sistema_implantes.visualizar_inventario()
            index = int(input("Ingrese el número del implante que desea editar: ")) - 1
            sistema_implantes.editar_implante(index)
        elif opcion == "4":
            sistema_implantes.visualizar_inventario()
        elif opcion == "5":
            nombre = input("Ingrese el nombre del paciente: ")
            id_paciente = input("Ingrese el ID del paciente: ")
            paciente = Paciente(nombre, id_paciente)
            sistema_implantes.registrar_paciente(paciente)
            print("Paciente registrado con éxito.")
        elif opcion == "6":
            sistema_implantes.asignar_implante_a_paciente()
        elif opcion == "7":
            sistema_implantes.mostrar_seguimiento_implantes()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")





    



