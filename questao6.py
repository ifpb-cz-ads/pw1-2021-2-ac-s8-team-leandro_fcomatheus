def soma(L):
	total=0
	x= len(L)
	for indice in range(0,x):
	    total = total + L[indice]
	return total


L = [10, 10, 10, 10]
resultado = soma(L)
print(resultado)