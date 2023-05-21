fruta_precio = {'platano':1.35, 'manzana':0.8, 'pera':0.85, 'naranja':0.7}
fruta_buscada = input('¿Que fruta buscas? ')
kilos = float(input('¿Cuantos kilos necesitas? '))
if fruta_buscada in fruta_precio:
    print('El precio de',kilos,'kg','de', fruta_buscada, 'es', fruta_precio[fruta_buscada]*kilos, 'pesos' )
else: 
    print("Lo siento, la fruta", fruta_buscada, "no está disponible.")