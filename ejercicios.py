def num_prime(n):
  for i in range (2,n):
    if (n%i)==0:
        return False
  return True  
print(num_prime(7)) 




# -*- coding: UTF-8 -*-
 
def primo(num):
	
	cont=0;
	
	for i in range(1,num):
		if(num%i==0):
			
			cont+=1
			if cont>1:
				return False
	return True
 
lista=[1,2,3,4,5,6,7,8,9,10,11]
suma=0
for i in lista:
	if num_prime(i):
		print ("El número ",i," es primo")
	else:
		print ("El número ",i," NO es primo")
	suma+=i
 
print ("La suma de la lista es:",suma)
print ("El promedio de la lista es:",(suma/len(lista)))


"""def convertir(valor,mo,md):
    
    if mo=="c" and md=="f":
        return(valor*1.8)+32
    if mo=="f" and md=="c":
        return (valor-32)/1.8
    if mo=="c" and md=="k":
        return(valor+273.15)
    if mo=="k" and md=="c":
        return(valor-273.15)
    if mo=="f" and md=="k" :
        return(valor+459.67)/1.8
    if mo=="k" and md=="f":
        return(valor*1.8)-459.67    

def listacelcius(arr):
    mo=input("ingresa la medida de origen: ")
    md=input("ingresa el origen: ")
    for numero in arr:
        convertido=convertir(numero,mo,md)
        print(f"para{numero}{mo} se convierte a",str(convertido),(md))

arr=[10,40,36]
listacelcius(arr)  """      


     






