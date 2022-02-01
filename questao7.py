def validarString(palavra,minimo,maximo):
    tamanhoString = len(palavra)
    if(tamanhoString<=maximo and tamanhoString>=minimo):
        return True
    else:
        return False
        

palavra = str(input("informe uma palavra:"))
minimo = int(input("informe o mínimo de caracteres:"))
maximo = int(input("informe o maximo de caracteres:"))
resultado = validarString(palavra,minimo,maximo)
print(resultado)