#Volver a preprocesar el archivo cambiando cada carácter según UNICODE-8
file = open("poema.txt")
cont = file.read()
nPoem = []

unicode_texto = cont.encode('unicode-escape')

print('Con bibliotecaa:\n',unicode_texto)
print("---------------------------")

print('Sin biblioteca: ')
nPoem.append(' b\'')

for letra in cont:
    if letra == '\n' :
        nPoem.append('\\\\n')
    elif letra =='á' :
        nPoem.append('\\\\xe1')
    elif letra =='é':
        nPoem.append('\\\\xe9')
    elif letra =='í':
        nPoem.append('\\\\xed')
    elif letra =='ó':
        nPoem.append('\\\\xf3')
    elif letra =='ú' :
        nPoem.append('\\\\xfa')
    elif letra =='¡' :
        nPoem.append('\\\\xa1')
    elif letra =='¿':
        nPoem.append('\\\\xbf')
    elif letra =='ñ':
        nPoem.append('\\\\xf1')
    else:
        nPoem.append(letra)

nPoem.append('\'')
NuevoPoema = ''.join(nPoem)
print(NuevoPoema)