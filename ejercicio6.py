#Obtener la información que el método Kasiski requiere para implementar un ataque, para ello deberá
#recorrer el texto preprocesado y hallar los trigramas en el mismo (sucesión de tres letras seguidas que se
#repiten) y las distancias (número de caracteres entre dos trigramas iguales consecutivos)


file = open("POEMA_PRE.txt")
trig = []

cont = file.read()
# generamos los trigramas
i = 0
while(i< len(cont)):
    if (len(cont[i:i+3])==3):
        trig.append(cont[i:i+3])
    i+=1

#print(trig)
#contamos la repeticion de los trigramas generados
trigRep = {}
for t in trig:
    trigRep[t]= trig.count(t)

for cTrig in trigRep:
    print("Trigrama: ",cTrig,"\trepeticiones: ",trigRep[cTrig])


##distancia entre 2 trigramas

"""
val='COF'
cont = 0
for i in range(len(trig)):
   
    if val == trig[i]:
        break
    else:
        cont+=1


print(val,": ",cont)"""