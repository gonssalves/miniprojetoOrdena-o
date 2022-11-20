import timeit
from sorts import *

if __name__ == '__main__':
  
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
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')


  lista = list(range(100000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}')
  print('#######################################################################################')


  lista = list(range(1000))

  def teste_merge():
    
      # print(f'LISTA EMBARALHADA\n{lista}\n')
      mergeSort(lista)
      # print(f'A LISTA FOI ORDENADA!')
      # print(lista,'\n\n')

  tempo = timeit.timeit( stmt=teste_sort, number=100)

  print('\n#######################################################################################')
  print('TESTE FEITO UTILIZANDO O MERGE SORT\n')
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')

    
  lista = list(range(10000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')


  lista = list(range(100000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}')
  print('#######################################################################################')



  lista = list(range(1000))


  def teste_hibrido():
      # print(f'LISTA EMBARALHADA\n{lista}\n')
      hibridoSort(lista)
      # print(f'A LISTA FOI ORDENADA!')
      # print(lista,'\n\n')

  tempo = timeit.timeit( stmt=teste_sort, number=100)

  print('\n#######################################################################################')
  print('TESTE FEITO UTILIZANDO O SELECTION E MERGE SORT\n')
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')

    
  lista = list(range(10000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')


  lista = list(range(100000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}')
  print('#######################################################################################')



  lista = list(range(1000))


  def teste_modificado():
      # print(f'LISTA EMBARALHADA\n{lista}\n')
      mergeModificado(lista)
      # print(f'A LISTA FOI ORDENADA!')
      # print(lista,'\n\n')

  tempo = timeit.timeit( stmt=teste_sort, number=100)

  print('\n#######################################################################################')
  print('TESTE FEITO UTILIZANDO MERGE SORT SEM SLICE\n')
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')

    
  lista = list(range(10000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}\n')


  lista = list(range(100000, 0, -1))
  print(f'Teste repetido {100} vezes em uma lista de {len(lista)} elementos')
  print(f'Tempo de duração do teste: {tempo}')
  print(f'Tempo médio de duração do teste: {tempo/100}')
  print('#######################################################################################')