# bruteforce.py
Cómo ejecutar el programa?
Para la ejecución correcta del programa se deben seguir los siguientes pasos:
1.-Tener la aplicación de Python instalada en el sistema.
2.-Guardar el archivo catalogado como "bruteforce.py" en el directorio del proyecto.
3.-Ejecutar el archivo desde la terminal o en la línea de comandos.

Ejemplos de salida.
El programa puede generar las siguientes salidas acorde a la contraseña ingresada:
La contraseña es: 'Ab2'
 prueba de longitud 1 
 prueba de longitud 2 
 prueba de longitud 3 

La contraseña encontrada es: Ab2
Intentos totales realizados: 209319
Tiempo de busqueda fue: 0.04895591735839844 segundos

La contraseña es: 'J12*'
 prueba de longitud 1
 prueba de longitud 2
 prueba de longitud 3
 prueba de longitud 4 

La contraseña encontrada es: J12*
Intentos totales realizados: 24956078
Tiempo de busqueda fue: 7.565248966217041 segundos

La contraseña es: '123!*'
 prueba de longitud 1
 prueba de longitud 2
 prueba de longitud 3
 prueba de longitud 4 

No se encontró la contraseña
Se realizaron 60658840 intentos en total.
El tiempo de busqueda fue: 17.57936954498291 segundos

Reflexión
¿Qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?
El factor mas relevente en este caso es el tiempo de búsqueda ya que crece en gran medida, lo que puede derivar en la tradanza del programa para encontrar la contraseña, adicionalmente la computadora quedaria congelada (matariamos a la compu).
Si realizamos los respectivos calculos en combinaciones seria un total de 88 caracteres posibles,lo que es aproximadamente 3.596 billones.
