"""
Solucion Lucas
"""
def maxcomundiv(num_a :int,num_b :int):
    """Maximo comun divisor

    Args:
        num_a (int): Valor 1 tiene que ser el mas bajo
        num_b (int): Valor 2

    Returns:
        int: Devuelve el Maximo comun divisor entre Valor 1 y Valor 2
    """
    mcd = 0
    i = 1
    if (num_a > num_b) :
        num_b, num_a = num_a, num_b
        

    if (num_a < num_b):
        
        while(i<= num_a):
            
            if (num_a%i==0 and num_b%i == 0):
                    mcd = i
            i=i+1
                    
    return mcd
                    
if __name__ =='__main__':
    print(maxcomundiv(49,7))

"""
----------------------------------------------------------------------
Eugenio Vazquez
------------------------------------------------------------------------------
# 1. Escribir una función que calcule el máximo común divisor entre dos números.
"""  
def get_divisores(numero):
    resp = []
    if numero == 1:
        resp = [1]

    for i in range(2, numero + 1):
        if numero % i == 0:
            resp.append(i)
            resp += get_divisores(int(numero / i))
            break

    return resp


def orden_resultados(list_resultados):
    counts = dict()
    for i in sorted(list_resultados):
        counts[i] = counts.get(i, 0) + 1

    return counts


def maximo_comun_divisor(num1, num2):
    divisor = 1
    veces = 1

    if min(num1, num2) < 1:
        print('Ingrese 2 numeros positivos')
        return -1

    divisores1 = orden_resultados(get_divisores(num1))
    divisores2 = orden_resultados(get_divisores(num2))

    for i in divisores1:
        if i in divisores2:
            divisor = i
            veces = min(divisores1[i], divisores2[i])

    return divisor ** veces


try:
    numero1a = int(input("Ingrese el número 1: "))
    numero2a = int(input("Ingrese el número 2: "))
    respuesta = maximo_comun_divisor(numero1a, numero2a)
    if respuesta > 0:
        print(f'El Máximo Común Divisor entre {numero1a} y {numero2a} es {respuesta} ')

except Exception:
    print("Ingrese números correctos")

print("*" * 100)


"""
---------------------------------------
Andres
https://github.com/garzamorada/django-2022.git
---------------------------------------
"""

"""
EJERCICIO 1
"""
def maxcomundiv(num_a :int,num_b :int):
    """Maximo comun divisor

    Args:
        num_a (int): Valor 1 tiene que ser el mas bajo
        num_b (int): Valor 2

    Returns:
        int: Devuelve el Maximo comun divisor entre Valor 1 y Valor 2
    """
    mcd = 0
    i = 1
    if (num_a > num_b) :
        num_b, num_a = num_a, num_b
        

    if (num_a < num_b):
        
        while(i<= num_a):
            
            if (num_a%i==0 and num_b%i == 0):
                    mcd = i
            i=i+1
                    
    return mcd
                    
if __name__ =='__main__':
    print(maxcomundiv(49,7))
    
"""
------------------------------------------------------------------------------
https://github.com/lugezz/codo_a_codo_2022/blob/main/Ejercicio%20Integrador/ejercicios.py
------------------------------------------------------------------------------
# 1. Escribir una función que calcule el máximo común divisor entre dos números.
"""
def get_divisores(numero):
    resp = []
    if numero == 1:
        resp = [1]

    for i in range(2, numero + 1):
        if numero % i == 0:
            resp.append(i)
            resp += get_divisores(int(numero / i))
            break

    return resp


def orden_resultados(list_resultados):
    counts = dict()
    for i in sorted(list_resultados):
        counts[i] = counts.get(i, 0) + 1

    return counts


def maximo_comun_divisor(num1, num2):
    divisor = 1
    veces = 1

    if min(num1, num2) < 1:
        print('Ingrese 2 numeros positivos')
        return -1

    divisores1 = orden_resultados(get_divisores(num1))
    divisores2 = orden_resultados(get_divisores(num2))

    for i in divisores1:
        if i in divisores2:
            divisor = i
            veces = min(divisores1[i], divisores2[i])

    return divisor ** veces


try:
    numero1a = int(input("Ingrese el número 1: "))
    numero2a = int(input("Ingrese el número 2: "))
    respuesta = maximo_comun_divisor(numero1a, numero2a)
    if respuesta > 0:
        print(f'El Máximo Común Divisor entre {numero1a} y {numero2a} es {respuesta} ')

except Exception:
    print("Ingrese números correctos")
    
""" 
----------------------------------------------------------------------------------------------------------------
EJERCICIO 2 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""
def minimo_comun_multipo(num1, num2):
    respuesta = 1

    if min(num1, num2) < 1:
        print('Ingrese 2 numeros positivos')
        return -1

    divisores1 = orden_resultados(get_divisores(num1))
    divisores2 = orden_resultados(get_divisores(num2))
    maximo_divisor = max(list(divisores1)[-1], list(divisores2)[-1])

    for i in range(1, maximo_divisor + 1):
        respuesta *= (i ** max(divisores1.get(i, 0), divisores2.get(i, 0)))

    return respuesta


try:
    numero1b = int(input("Ingrese el número 1: "))
    numero2b = int(input("Ingrese el número 2: "))
    respuesta2 = minimo_comun_multipo(numero1b, numero2b)
    if respuesta2 > -10:
        print(f'El Mínimo Común Múltipo entre {numero1b} y {numero2b} es {respuesta2} ')

except Exception:
    print("Ingrese números correctos")


"""
----------------------------------------------
# Heber Alonso
----------------------------------------------
"""
# Escribir una función que calcule el máximo común divisor entre dos números.
numero1=int(input('Ingrese el primer numero: '))
numero2=int(input('Ingrese el segundo numero: '))
numeros_primos=[2,3,5,7,11,13,1.5]   # el 1.5 es una bandera para indicar que ninguno puede ser dividido

def buscar_divisores(num1,num2):  # Busca todos los divisores por los numeros primos
    divisores=[]
    bandera=0 # indicacion de guarda de dato divisor
    
    while num1!=1 or num2!=1:   # Ejecutar hasta que los numeros no se puedan dividir mas
        for divisor in numeros_primos:
            

            if num1%divisor==0:      
                num1=int(num1/divisor) # nuevo valor de num1
                bandera=1 # activo bandera para que s eguarde el divisor
    
                
            
            if num2%divisor==0:
                num2=int(num2/divisor) # nuevo valor de num2
                bandera=1 # activo bandera para que s eguarde el divisor        
                

            if bandera==1:
                bandera=0 # resetea la bandera
                divisores.append(divisor)  # se agrega a la lista de divisores del numero el divisor
                break    # finaliza el for para volver a dividir por la secuencia de primos
            

        if divisor==1.5:   # se activa la bandera que indica el numero primo final que algun numero ya no s epuede dividir mas

            if num1!=1:
                divisores.append(num1) # agrega el resto del numero1 que quedo ya que no se puede dividir 
                num1=1
                
            if num2!=1:
                divisores.append(num2)# agrega el resto del numero2 que quedo ya que no se puede dividir
                num2=1                # finaliza el ciclo while ya no acepta mas divisiones
                

        print ( "│",num1,'│',num2,'║',divisor)        
    return (divisores)

divisores=buscar_divisores(numero1,numero2)

print ('Divisores de los numeros:', divisores)


# calculo del multiplo
mcm=1  # es el maximo comun divisor de cualquier numero
for multiplo in divisores:
    mcm=mcm*multiplo

print('EL Mínimo Común Multiplo de los numeros',numero1,'y',numero2,'es:',mcm)

"""
----------------------------------------------------------------------------------------------------------------
EJERCICIO 3 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""

def orden_resultados(list_resultados):
    counts = dict()
    for i in sorted(list_resultados):
        counts[i] = counts.get(i, 0) + 1

    return counts

texto = "Es un teatro de temporada o de stagione que lo que"

texto_lista = texto.split()
texto_diccionario = orden_resultados(texto_lista)

"""
----------------------------------------------------------------------------------------------------------------
EJERCICIO 4 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""
def get_mas_repetido(mi_diccionario):
    resultado = ("", 0)
    for k, v in mi_diccionario.items():
        if v > resultado[1]:
            resultado = (k, v)

    return resultado


print("Ejercicio 4", get_mas_repetido(texto_diccionario))

"""
----------------------------------------------------------------------------------------------------------------
EJERCICIO 5 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""
es_entero = False


def get_int(numero):
    global es_entero
    respuesta = 0
    try:
        respuesta = int(numero)
        es_entero = True

    except ValueError:
        print("Ingreso incorrecto, intente nuevamente")

    return respuesta


while not es_entero:
    ingreso = input('Ingrese un número: ')
    valor = get_int(ingreso)


print("Ejercicio 5: Ingresaste el valor", valor)



from collections import Counter

def cadena_to_dict(string :str):
    """Convierte cadena a Diccionario


    Args:
        string (str): Cadena que ingresa el usuario

    Returns:
        dict: diccionario con key = a palabras unicas del string y value con la frecuencia 
    """

    lista = string.split(" ")
    dict_keys = Counter(lista).keys()
    dict_values = Counter(lista).values() 
       
    return dict(zip(dict_keys,dict_values))
    
    



def dict_to_tuple(a:dict):
    
    
    return sorted(result.items(), key=lambda x: x[1],reverse=True)[0]


if __name__== '__main__':
        
    result = cadena_to_dict("HOLA COMO ESTAS HOLA COMO COMO ESTAS ESTAS ESTAS")
    print(dict_to_tuple(result))
    

# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# Solución recursiva
def get_int():
    try:
        ingreso = input('Ingrese un numero: ')
        a = int(ingreso)
    except ValueError:
        print('Parece que ha habido un error, debe ingresar un numero')
        a = get_int()
    return a
    
# get_int()




# Solución iterativa
def get_int_2():
    try:
        ingreso = input('Ingrese un numero: ')
        ingreso = int(ingreso)
    except ValueError:
        print('Parece que ha habido un error, debe ingresar un numero')
    return ingreso

condicion = True
while condicion:
    numero = get_int_2()
    if type(numero) == int:
        condicion = False
print('\nPrograma finalizado')

get_int_2()

#Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto 
# en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, 
# iterando mientras el valor no sea correcto. 
# Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    print("Ingreso el numero: ", x)

get_int()

def get_int_with_recursion():
        try:
            x = int(input("Please enter a number: "))
            print(x)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            get_int_with_recursion()

get_int_with_recursion()

"""
----------------------------------------------------------------------------------------------------------------
EJERCICIO 6 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""

class Persona:

    def __init__(self, nombre="", edad=0, DNI=""):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def DNI(self):
        return self.__DNI

    def validar_nombre(self):
        # Máximo largo 100 caracteres
        if len(self.__nombre) > 100:
            print('Nombre Incorrecto!')
            self.__nombre = ""

    def validar_edad(self):
        if self.__edad < 0:
            print('Edad Incorrecta!')
            self.__edad = 0

    def validar_DNI(self):
        # Debe tener 7 a 9 caracteres
        if len(self.__DNI) < 7 or len(self.__DNI) > 9:
            print('DNI Incorrecto!')
            if len(self.__DNI) < 7:
                self.__DNI = f'{"0" * (8 - len(self.__DNI))}{self.__DNI}'
            else:
                self.__DNI = self.__DNI[:8]

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        self.validar_nombre()

    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        self.validar_edad()

    @DNI.setter
    def DNI(self, DNI):
        self.__DNI = DNI
        self.validar_DNI()

    def mostrar(self):
        return f'Mi nombre es {self.nombre}, DNI: {self.DNI} y tengo {self.edad} años'

    def es_mayor_de_edad(self):
        return self.edad >= 18


personilla = Persona("Juan", 22, "3232")
print("Ejercicio 6:")
print(personilla.mostrar())

"""
----------------------------------------------------------------------------------------------------------------
EJERCICIO 7 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""

class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    def mostrar(self):
        print(f'Titular: {self.titular.mostrar()} | Su cantidad es {self.cantidad}')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad


cuentilla = Cuenta(personilla, 100)
cuentilla.ingresar(400)
cuentilla.retirar(10)
print("Ejercicio 7:")
cuentilla.mostrar()

"""
----------------------------------------------------------------------------------------------------------------
EJERCICIO 8 ----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
"""

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        print(f'Cuenta Joven: Su cantidad es {self.cantidad} - Su bonificación es {self.bonificacion}%')

    def es_valido_titular(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25

    def retirar(self, cantidad):
        if not self.es_valido_titular():
            mensaje = "estás viejito" if self.titular.edad >= 25 else "sos un niño"
            print(f'No puedes retirar, {mensaje}')

        else:
            super().retirar(cantidad)


cuentilla_joven = CuentaJoven(personilla, bonificacion=20)
cuentilla_joven.ingresar(1300)
cuentilla_joven.retirar(128)

print("Ejercicio 8:")
cuentilla_joven.mostrar()

