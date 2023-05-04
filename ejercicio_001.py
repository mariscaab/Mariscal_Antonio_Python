#Cuestionario
nombre = str(input("¿Cuál es tu nombre:?"))
apellido = str(input("¿Cuál es tu primer apellido:?"))
segundo_apellido = str(input("¿Cual es tu segundo apellido:?"))
año_nacimiento = int(input("¿En que año naciste:?"))
nacimiento_mesdia = (input("¿En qué mes y día naciste :?(en el siguiente formato “mm-dd”)"))

#A.Nombre en mayusculas
nombre_completo = nombre + " " + apellido + " " + segundo_apellido 
print(f"Este es tu nombre completo en mayusculas:", nombre_completo.upper())

#B.Nombre en minusculas
print(f"Este es tu nombre completo en minusculas:", nombre_completo.lower())

#C. Fecha de nacimiento 
fecha = nacimiento_mesdia
print('Mes', fecha[3:5])
print('Día', fecha[:2])


#D.Esta es tu edad
año_actual = 2023
edad = año_actual - año_nacimiento
print(f"Esta es tu edad:", edad)


#E. Numero de vocales
vocales = "aeiouAEIOU"
j = 0
for valores in nombre_completo:
    if  valores in vocales:
        j = j + 1
print(f"Tu nombre completo tiene {j} vocales:")

#F.Numero de letras
longitud_nombre = len(nombre_completo)
print('Tu nombre completo tiene', longitud_nombre, 'letras')


#G.Tipo de numero
if type(edad) == int:
    print(f"¿Tu edad es un caracter de tipo numero:? True")

#H. alfanumertico 
print(f"¿Tu nombre completo es un carácter de tipo alfanumérico?:",nombre_completo.isalnum())


#I. Edad 10 años
print(f"Tu edad en 10 años sera:", edad + 10)


#J. Edad media en 20 años
print(f"La media de tu edad actual y tu edad en 20 años es:", edad / 2 + 20)



























