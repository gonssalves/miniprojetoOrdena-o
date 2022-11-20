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