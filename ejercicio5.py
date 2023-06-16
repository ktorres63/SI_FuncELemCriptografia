#Abra el archivo generado e implementar una función que calcule una tabla de frecuencias para cada letra de
#la ’A’ a ’Z’. La función deberá definirse como frecuencias(archivo) y deberá devolver un diccionario cuyos
#índices son las letras analizadas y cuyos valores son las frecuencias de las mismas en el texto (número de
#veces que aparecen). Reconozca en el resultado obtenido los cinco caracteres de mayor frecuencia

def frecuencias(archivo):

    cont = list(archivo.upper())
    freq = {}

    for letra in range(ord('A'), ord('Z')+1):
        # Convertir el código ASCII de la letra a carácter
        letra = chr(letra)

        # Contar la frecuencia de la letra en la oración
        frecuencia = cont.count(letra)

        # Almacenar la frecuencia en el diccionario
        freq[letra] = frecuencia
    return freq


file2 = open("POEMA_PRE.txt")
cont = file2.read()

tabla_frec = frecuencias(cont)


# Imprimir la tabla de frecuencias
for letra, frecuencia in tabla_frec.items():
    print(f"Letra '{letra}': {frecuencia} veces")

file2.close()