def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None




l = [10, 20, 30, 40]
print(pesquise(l, 25))
print(pesquise(l, 30))