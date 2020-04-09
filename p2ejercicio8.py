def esPrimo (num):
	if(num ==1):
		return(False)
	elif(num== 2):
		return(True)
	else:
		for x in range(2,num):
			if num%x == 0:
				return(False)
	return(True)

string= input('ingrese un string, contaremos los caracteres')

tupla=set(tuple(string))
diccionario={}
for letra in tupla:
	diccionario[letra]= string.count(letra)


print(diccionario)



for keys in diccionario.keys():
	if(esPrimo(diccionario[keys])):
		print("la letra {} aparece un numero primo de veces".format(keys))
		
	
