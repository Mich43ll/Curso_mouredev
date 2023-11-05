### Exceptions ###

NUMBER_ONE = 5
NUMBER_THREE= "1"

try:
    print(NUMBER_ONE + NUMBER_THREE)
except Exception: #Se ejecuta cuando sucede un error en el try
    print("Se ha producido un error")
finally: #Se ejecuta siempre
    print("La ejecucion continua")

try:
    print(NUMBER_ONE + NUMBER_THREE)
except TypeError as e:
    print("Se produjo un error")
    print(e)

    