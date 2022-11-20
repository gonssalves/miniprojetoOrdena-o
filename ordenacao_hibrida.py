import timeit


def selectionSort(uma_lista):
    for posicao_verificada in range(len(uma_lista)-1,0,-1):
        posicao_maior = 0
        for posicao in range(1,posicao_verificada+1):
            if uma_lista[posicao]>uma_lista[posicao_maior]:
                posicao_maior = posicao
                
        temp = uma_lista[posicao_verificada]
        uma_lista[posicao_verificada] = uma_lista[posicao_maior]
        uma_lista[posicao_maior] = temp
        

def mergeSort(uma_lista):    
    if len(uma_lista) > 1:
        meio = len(uma_lista)//2
        esquerda = uma_lista[:meio]
        direita = uma_lista[meio:]
     
        mergeSort(esquerda)
        mergeSort(direita)

        i=0; j=0; k=0
    
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k]=esquerda[i]
                i=i+1
            else:
                uma_lista[k]=direita[j]
                j=j+1
            k=k+1
                
            while i < len(esquerda):
                uma_lista[k]=esquerda[i]
                i=i+1
                k=k+1
                
            while j < len(direita):
                uma_lista[k]=direita[j]
                j=j+1
                k=k+1
                
        
def hibridoSort(uma_lista):
  if len(uma_lista) >= 5:
    meio = len(uma_lista)//2
    esquerda = uma_lista[:meio]
    direita = uma_lista[meio:]
    hibridoSort(esquerda)
    hibridoSort(direita)
    # merge
    i=0
    j=0
    k=0
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        uma_lista[k]=esquerda[i]
        i=i+1
      else:
        uma_lista[k]=direita[j]
        j=j+1
      k=k+1
    while i < len(esquerda):
      uma_lista[k]=esquerda[i]
      i=i+1
      k=k+1
    while j < len(direita):
      uma_lista[k]=direita[j]
      j=j+1
      k=k+1
  else:
    selectionSort(uma_lista)


def mergeModificado(uma_lista):
  if len(uma_lista) > 1:
    meio = len(uma_lista)//2
    esquerda = []
    for pos in range(meio):
      esquerda.append(uma_lista[pos])
    direita = []
    
    for pos in range(meio, len(uma_lista)):
      direita.append(uma_lista[pos])
      
    mergeModificado(esquerda)
    mergeModificado(direita)
    
    i=0;j=0;k=0
    
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        uma_lista[k]=esquerda[i]
        i=i+1
      else:
        uma_lista[k]=direita[j]
        j=j+1
      k=k+1
    while i < len(esquerda):
      uma_lista[k]=esquerda[i]
      i=i+1
      k=k+1
    while j < len(direita):
      uma_lista[k]=direita[j]
      j=j+1
      k=k+1



lista = list(range(1000, 0, -1))



def teste_sort():
    # print(f'LISTA EMBARALHADA\n{lista}\n')
    selectionSort(lista)
    # print(f'A LISTA FOI ORDENADA!')
    # print(lista,'\n\n')
    
tempo = timeit.timeit( stmt=teste_sort, number=100)

print('\n#######################################################################################')
print('TESTE FEITO UTILIZANDO O SELECTION SORT\n')
print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
print(f'Tempo de duração do teste: {tempo}')
print(f'Tempo médio de duração do teste: {tempo/100}\n')

  
lista = list(range(10000, 0, -1))
tempo = timeit.timeit( stmt=teste_sort, number=100)
print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
print(f'Tempo de duração do teste: {tempo}')
print(f'Tempo médio de duração do teste: {tempo/100}\n')


lista = list(range(100000, 0, -1))
tempo = timeit.timeit( stmt=teste_sort, number=100)
print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
print(f'Tempo de duração do teste: {tempo}')
print(f'Tempo médio de duração do teste: {tempo/100}')
print('#######################################################################################')



# lista = list(range(1000))


# def teste_merge():
  
#     # print(f'LISTA EMBARALHADA\n{lista}\n')
#     mergeSort(lista)
#     # print(f'A LISTA FOI ORDENADA!')
#     # print(lista,'\n\n')

# tempo = timeit.timeit( stmt=teste_sort, number=100)

# print('\n#######################################################################################')
# print('TESTE FEITO UTILIZANDO O MERGE SORT\n')
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}\n')

  
# lista = list(range(10000, 0, -1))
# tempo = timeit.timeit( stmt=teste_sort, number=100)
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}\n')


# lista = list(range(100000, 0, -1))
# tempo = timeit.timeit( stmt=teste_sort, number=100)
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}')
# print('#######################################################################################')



# lista = list(range(1000))


# def teste_hibrido():
#     # print(f'LISTA EMBARALHADA\n{lista}\n')
#     hibridoSort(lista)
#     # print(f'A LISTA FOI ORDENADA!')
#     # print(lista,'\n\n')

# tempo = timeit.timeit( stmt=teste_sort, number=100)

# print('\n#######################################################################################')
# print('TESTE FEITO UTILIZANDO O SELECTION E MERGE SORT\n')
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}\n')

  
# lista = list(range(10000, 0, -1))
# tempo = timeit.timeit( stmt=teste_sort, number=100)
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}\n')


# lista = list(range(100000, 0, -1))
# tempo = timeit.timeit( stmt=teste_sort, number=100)
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}')
# print('#######################################################################################')



# lista = list(range(1000))


# def teste_modificado():
#     # print(f'LISTA EMBARALHADA\n{lista}\n')
#     mergeModificado(lista)
#     # print(f'A LISTA FOI ORDENADA!')
#     # print(lista,'\n\n')

# tempo = timeit.timeit( stmt=teste_sort, number=100)

# print('\n#######################################################################################')
# print('TESTE FEITO UTILIZANDO MERGE SORT SEM SLICE\n')
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}\n')

  
# lista = list(range(10000, 0, -1))
# tempo = timeit.timeit( stmt=teste_sort, number=100)
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}\n')


# lista = list(range(100000, 0, -1))
# tempo = timeit.timeit( stmt=teste_sort, number=100)
# print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
# print(f'Tempo de duração do teste: {tempo}')
# print(f'Tempo médio de duração do teste: {tempo/100}')
# print('#######################################################################################')