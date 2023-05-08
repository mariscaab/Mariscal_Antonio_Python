#Cuestionario
nombre = str(input("¿Cual es tu nombre?"))
genero= str(input("¿Genero? M O F:"))
grupo_1 = "A"
grupo_2 = "B"


if (genero == "f" and nombre.casefold() < "m") or (genero.casefold() == "m" and nombre.casefold() > "n"):
    print("Tu grupo es", grupo_1)
else: 
    (genero.casefold() == "f" and nombre.casefold()  > "n") or (genero.casefold() == "m" and nombre.casefold() < "m")
    print("Tu grupo es", grupo_2)







