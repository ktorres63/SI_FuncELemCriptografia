#Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8


file = open("poema.txt")
cont = file.read()

unicode_texto = cont.encode('unicode-escape')

print(unicode_texto)
print(cont)