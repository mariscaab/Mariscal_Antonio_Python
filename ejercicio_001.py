Nombre = str(input("¿Cuál es tu nombre?"))
Apellido = str(input("¿Cuál es tu primer apellido?"))
Segundo_Apellido = str(input("¿Cual es tu segundo apellido?"))
Año = int(input("¿En que año naciste?"))
Nacimiento = str(input("¿En qué mes y día naciste mm-dd?"))
año_actual = 2023


print(f"Este es tu nombre completo en mayusculas:", Nombre.upper() + " " + Apellido.upper() +  " " + Segundo_Apellido.upper())
print(f"Este es tu nombre completo en minusculas:", Nombre.lower() + " " + Apellido.lower() + " " + Segundo_Apellido.lower())
print(f"Esta es tu fecha de nacimiento dd-mm-aaaa:" + Nacimiento)
print(f"Esta es tu edad:", año_actual - Año)
nombrecompleto = (input("Tu nombre completo tiene: "))
vocales = "aeiouAEIOU"
j = 0
for NOMBRES in nombrecompleto:
    if  NOMBRES in vocales:
        j = j + 1
print(f"Tu nombre completo tiene {j} vocales:")
print('Tu nombre completo tiene', len(Nombre + Apellido + Segundo_Apellido), 'letras')
print(f"Tu edad en 10 años sera", {año_actual - Año + 10})