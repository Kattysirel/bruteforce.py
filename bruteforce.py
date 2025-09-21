import time

def combinaciones(alfabeto, longitud):
    if longitud == 1:
        for caracter in alfabeto:
            yield caracter
    else:
        for caracter in alfabeto:
            for sub_combinacion in combinaciones(alfabeto, longitud - 1):
                yield caracter + sub_combinacion



minus = "abcdefghijklmnopqrstuvwxyz"
mayus= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"

alfabeto = minus + mayus + numeros + simbolos



contrasena = "123!*"
longitud_maxima = 4

print(f"La contraseña es: '{contrasena}'")


tiempo_inicio = time.time()
intentos = 0
contra_encontrada = False




for longitud in range(1, longitud_maxima + 1):
    
    print(f" prueba de longitud {longitud} ")
    
    
    for intento_actual in combinaciones(alfabeto, longitud):
        intentos = intentos + 1
                

        if intento_actual == contrasena:
            contra_encontrada = True
            break
    
    if contra_encontrada:
        break
    
    
  
tiempo_fin = time.time()
duracion = tiempo_fin - tiempo_inicio


if contra_encontrada:
    print(f"\nLa contraseña encontrada es: {contrasena}")
    print(f"Intentos totales realizados: {intentos}")
    print(f"Tiempo de busqueda fue: {duracion} segundos")
    print(f"\n ")
    
    
else:
    print(f"\nNo se encontró la contraseña")
    print(f"Se realizaron {intentos} intentos en total.")
    print(f"El tiempo de busqueda fue: {duracion} segundos")
print(f"\n ")