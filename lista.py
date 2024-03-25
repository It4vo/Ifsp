# Criando uma lista vazia
lista = []

# Adicionando itens à lista
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

# Imprimindo a lista
print("Lista original:", lista)

# Removendo um item da lista
item_removido = lista.pop(2)  # Remove o item na posição 2
print("Item removido:", item_removido)
print("Lista após a remoção:", lista)

# Invertendo a lista
lista.reverse()
print("Lista invertida:", lista)

# Imprimindo a lista de trás para frente
print("Lista de trás para frente:", lista[::-1])

# Obtendo o comprimento da lista
print("Comprimento da lista:", len(lista))

# Ordenando a lista
lista.sort()
print("Lista ordenada:", lista)

lista.insert(0, 10)  # Insere o número 10 na primeira posição da lista
print("Lista após inserção:", lista)

lista.remove(2)  # Remove o número 2 da lista, se presente
print("print lista apos a remoçao:", lista)


vezes = lista.count(4)  # Retorna quantas vezes o número 4 aparece na lista
print("o numero 4 apareceu",vezes,"vez")

lista.extend([5, 6, 7])  # Adiciona os números 5, 6 e 7 ao final da lista

lista_copia = lista.copy()  # Cria uma cópia da lista original
print("Lista copia:", lista_copia)

lista.clear()  # Remove todos os itens da lista, deixando-a vazia
print("lista linpa:", lista)

