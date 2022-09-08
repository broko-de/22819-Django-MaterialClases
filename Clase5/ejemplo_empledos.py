from abc import ABC, abstractmethod

"""Clase abstracta de Empleado
"""
class Empleado(ABC):

    def __init__(self,nombre,apellido):
        self.__nombre=nombre
        self.__apellido=apellido
    
    def __str__(self):
        return f"Empleado: {self.__apellido}"

    #GETTER
    @property
    def apellido(self):
        return self.__apellido

    #SETTER
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self.__apellido = nuevo_apellido
        
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass

    def metodo_uno(self):
        return 10

#empleado_uno = Empleado('fede','liquin')

"""
Subclase que hereda de la clase abstracta Empleado
"""
class EmpleadoFullTime(Empleado):

    def __init__(self, nombre, apellido,salario):
        #propiedades heredadas
        super().__init__(nombre, apellido)
        self.__salario = salario

    def __str__(self):
        return super().__str__()

    @property
    def salario(self):
        return self.__salario

"""
Subclase que hereda de la clase abstracta Empleado
"""
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido,horas_trabajadas,valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * self.__valor_hora


class Nomina:
    
    def __init__(self):
        self.__lista_empleados = []

    def agregar_empleado(self,empleado):
        self.__lista_empleados.append(empleado)

    def print(self):
        for empleado in self.__lista_empleados:
            if isinstance(empleado,Empleado):
                print(f"{empleado.nombre_completo} - $ {empleado.salario}")
            else:
                print(f"En la nomina hay un no empleado: {empleado}")


nomina_empleados = Nomina()

empleado_uno = EmpleadoFullTime('Mario','Lobo',90000)
# print(empleado_uno.apellido)
#USO DEL SETTER
empleado_uno.apellido = 'pepito'
#USO DE GETTER
print(empleado_uno.apellido)
nomina_empleados.agregar_empleado(empleado_uno)
nomina_empleados.agregar_empleado(EmpleadoPorHora('Gustavo','Balvorin',40,1500))
nomina_empleados.agregar_empleado(33)
# nomina_empleados.print()
# print(nomina_empleados._Nomina__lista_empleados[2])


class Estudiante():

    def __init__(self,legajo):
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo
    
    def metodo_uno(self):
        return 100000
    

class EstudiantePasante(Empleado,Estudiante):

    def __init__(self, nombre, apellido,legajo):
        Empleado.__init__(self,nombre, apellido)
        Estudiante.__init__(self,legajo)

    
    @property
    def salario(self):
        return 0
    
    def __str__(self):
        return f"{self.nombre_completo}, Legajo: {self.legajo}"


estudiante_uno = EstudiantePasante('Pablo','Perez','IF-5564')
print(estudiante_uno.metodo_uno())
print(estudiante_uno)

nomina_empleados.agregar_empleado(estudiante_uno)
nomina_empleados.print()