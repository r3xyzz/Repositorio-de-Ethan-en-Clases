'''
generador de contraseñas: 
Crea un programa que genere contraseñas aleatorias. 
La contraseña debe tener una longitud predeterminada y contener letras mayúsculas, minúsculas y números. 
'''
import random
import string

longitud = 8  #especificamos la longitud que deseamos que tenga la contraseña. En este ejemplo, se utiliza una longitud predeterminada de 8 caracteres, pero puedes ajustarlo según tus necesidades.

'''
variable llamada caracteres que contiene todas las letras mayúsculas, minúsculas y dígitos. 
Luego, utilizamos una comprensión de lista y la función random.choice() 
para seleccionar aleatoriamente caracteres de la cadena caracteres y generar la contraseña deseada.
'''
caracteres = string.ascii_letters + string.digits
contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

print("Contraseña Generada: ", contrasena)

