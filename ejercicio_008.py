import pandas as pandas

def aprobados(calificacion):
    calificacion = pandas.Series(calificacion)
    return calificacion[calificacion >= 5].sort_values(ascending=False)

calificacion = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(aprobados(calificacion))