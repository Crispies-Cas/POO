class Persona:
    def __init__(self):
        self.__nombre= "nombres"
        self.__cedula= "cédula"
        self.__edad= "edad"
        self.__genero= "género"
    
    def ingresar_nombre(self, a):
        self.__nombre= a
    def ingresar_cedula(self, a):
        self.__cedula= a
    def ingresar_edad(self, a):
        self.__edad= a
    def ingresar_genero(self, a):
        self.__genero= a
    def mostrar_nombre(self):
        print(self.__nombre)
    def mostrar_cedula(self):
        print(self.__cedula)
    def mostrar_edad(self):
        print(self.__edad)
    def mostrar_genero(self):
        print(self.__genero)
    
    def __str__(self):
        cadena=f"{self.__cedula}|{self.__nombre}"
        return cadena

class Paciente(Persona):
    def __init__(self):
        super().__init__()
        self.__servicio= 'servicio'
    def ingresar_servicio(self, a):
        self.__servicio= a
    def mostrar_servicio(self):
        print(self.__servicio)
        
class Sistema:
    def __init__(self):
        self.__lista_pacientes= []
    def ingresar_paciente(self, paciente:Paciente):
        self.__lista_pacientes.append(paciente)
        
    #Este método debería utilizar el ciclo for para mostrar todos los pacientes 1 por 1
    #Luego, pedir al usuario que seleccione un paciente para retornarlo
    def escoger_paciente(self):
        i=1
        for paciente in self.__lista_pacientes:
            print(f'{i}. {paciente}')
            i=i+1
        sel= int(input('escoja su paciente (con el índice): '))
        pac:Paciente=self.__lista_pacientes[sel-1]
        pac.mostrar_nombre
        pac.mostrar_cedula
        pac.mostrar_edad
        pac.mostrar_genero
        return pac
    def __str__(self):
        cadena= f'El sistema tiene {len(self.__lista_pacientes)} pacientes'
        return cadena
#---------------------------------------------------------
Salmon=Sistema()
print(Salmon)

#este paciente es de prueba
pj=Paciente()
pj.ingresar_cedula('1020')
pj.ingresar_edad('24')
pj.ingresar_genero('m')
pj.ingresar_nombre('Jose Luis')
pj.ingresar_servicio('vasec')
Salmon.ingresar_paciente(pj)
print(Salmon)
#--------------------------
while True:
    menu=input('1.Ingresar paciente\n2.escoger paciente\n3.Salir\n--->')
    if menu=='1':
        pj=Paciente()
        print('--Ingrese paciente--')
        name=input('ingrese un nombre:')
        pj.ingresar_nombre(name)
        cc=input('ingrese cédula: ')
        pj.ingresar_cedula(cc)
        age=input('edad: ')
        pj.ingresar_edad(age)
        genero=input('genero: ')
        pj.ingresar_genero(genero)
        service=input('servicio que desea: ')
        pj.ingresar_servicio(service)
        Salmon.ingresar_paciente(pj)
        print(pj)
        print(Salmon)
    elif menu=='2':
        #Esta parte debería aprovechar el método .escoger_paciente de la clase sistema
        #de esta forma mostraría todos los pacientes y al retornar un paciente poder editarlo luego
        
        Salmon.escoger_paciente
        pac:Paciente=Salmon.escoger_paciente()
        menu2=input('desea editar el paciente?\n1.Sí\n2.No\n--->')
        if menu2=='1':
            menu3=input('1.Servicio\n2.Edad\3.Nombre\n4.Género\n5Salir')
            if menu3=='1':
                service=input('Nuevo servicio: ')
                pac.ingresar_servicio(service)
                print('se ha guardado con exito')
            elif menu3=='2':
                pac.ingresar_edad(input('Nueva edad: '))
                print('se ha guardado con exito')
            elif menu3=='3':
                pac.ingresar_nombre(input('Nuevo nombre: '))
                print('se ha guardado con exito')
            elif menu3=='4':
                pac.ingresar_genero(input('Nueva Género: '))
                print('se ha guardado con exito')
            elif menu3=='5':
                pass
            else:
                print('--Error de digitación--')
        elif menu2=='2':
            pass
        else:
            print('--Error de digitación--')
    elif menu == '3':
        print(Salmon)
        break
    else:
        print('--Error de digitación--')
#
#

#
#