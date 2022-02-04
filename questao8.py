
def encontrarString(string, lista):
    for indice in range(len(lista)):
        if lista[indice] == string:
            return True
    return False   
    
    
    
string = "hero"
lista = [10,12,"hero",10]
achou = encontrarString(string,lista)
print(achou)