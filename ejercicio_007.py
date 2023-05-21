def length_words(sentence):
    palabras = sentence.split()
    longitud = map(len, palabras)
    return dict(zip(palabras, longitud))

print(length_words('Hola Mundo'))