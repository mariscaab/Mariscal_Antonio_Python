def area_circulo(radio):
    pi = 3.1415
    return 2*pi*radio**2

def volumen(radio, altura):
    return area_circulo(radio)*altura

print(volumen(5,2))