import sys

class DivisorNegativoError(Exception):
    """
        Excepción lanzada si se divide por un número negativo
    """
    pass

def mostrar_division_entera(dividendo,divisor):
    try:
        assert divisor >= 0, "Mandaron un número negativo"
        if divisor < 0:
            raise DivisorNegativoError("Mandaron un número negativo en el divisor")
            
        print('Intentando resolver la division')
        resultado = dividendo / divisor
        print(f"El resultado de la división es: {resultado}")
    except AssertionError as assert_error:
        print(assert_error)
        print('Le erraste a un dato...')
    except TypeError:
        #logica de capturar error
        print('Error, divisor o dividendo no son numericos')
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(exc_type)
        print(exc_value)
        print(exc_traceback)
    except ZeroDivisionError as DZeroException:
        print(f'Error {DZeroException}')
    except DivisorNegativoError:
        print('Error paso algo con el divisor que es negativo')
    except Exception as ex:
        print(f'Algo anda mal: {ex}')
    else:
        print('Este programa nunca falla...')
    finally:
        print('Finalizacion de la funcion')

mostrar_division_entera(2,-1)
mostrar_division_entera(4,"4")
mostrar_division_entera(4,0)
print('Continuación del programa')