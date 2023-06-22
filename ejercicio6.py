#Obtener la información que el método Kasiski requiere para implementar un ataque, para ello deberá
#recorrer el texto preprocesado y hallar los trigramas en el mismo (sucesión de tres letras seguidas que se
#repiten) y las distancias (número de caracteres entre dos trigramas iguales consecutivos)


file = open("POEMA_PRE.txt")
trig = []

cont = file.read()
PoemList = list(cont)

i = 0
# generamos los trigramas
while(i< len(PoemList)):
    if (len(PoemList[i:i+3])==3):
        trig.append(PoemList[i:i+3])
    i+=1

print(trig)

#contamos la repeticion de los trigramas generados
for t in trig:
    print("Trigrama: ",t,"\trepeticiones: ",trig.count(t))
