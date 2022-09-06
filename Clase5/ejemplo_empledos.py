from abc import ABC, abstractmethod

"""
Clase abstracta de Empleado
"""
class Empleado(ABC):

    def __init__(self,nombre,apellido):
        self.__nombre=nombre
        self.__apellido=apellido
    
    def __str__(self):
        return f"Empleado: {self.__apellido}"

    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass

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
nomina_empleados.agregar_empleado(empleado_uno)
nomina_empleados.agregar_empleado(EmpleadoPorHora('Gustavo','Balvorin',40,1500))
nomina_empleados.agregar_empleado(33)
nomina_empleados.print()
print(nomina_empleados._Nomina__lista_empleados[2])
