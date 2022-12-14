number_times=0
matriz= []
transposta=[]
lista=[]

def organizar_matriz(matriz):
    global number_times 
    number_times=0
    for j in matriz:
        quicksort(j)
        number_times+=1

def quicksort(linha, ini=0, fim=None):
    fim = fim if fim is not None else len(linha)
    if ini < fim:
        pp = particao(linha, ini, fim)
        quicksort(linha, ini, pp)
        quicksort(linha, pp + 1, fim)
    return linha

def particao(linha, ini, fim):
    global mode , lista, number_times
    pivo = linha[fim - 1]
    for i in range(ini, fim):
        if linha[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            linha[i], linha[ini - 1] = linha[ini - 1], linha[i]
            if i!=ini-1 and number_times==0: lista.append(f"{mode} {ini} {i+1} ")
    return ini - 1
    
def transpor(mtx1,mtx2):
    for i in range(len(mtx1[0])):
        coluna=[]
        for j in range(len(mtx1)):
            coluna.append(mtx1[j][i])
        mtx2.append(coluna)

while True:
    try:
        tamanho = str(input('Digite a quantidade de linhas e colunas: ')).split()
        if len(tamanho)==2:
            linha = int(tamanho[0])
            coluna = int(tamanho[1])
            if 1 <= linha <= 200 and 1 <= coluna <= 200:break
        print('Valor inválido. Tente novamente.\n')
    except ValueError: print('Valor inválido. Tente novamente.\n')

while True:
    try:
        for l in range(linha):
            matriz.append([])
            while True:
                try:
                    valor = str(input(f'Como estão organizadas as fileiras da linha {l+1}º: ')).split()
                    
                    if len(valor)==coluna:break
                    else:print('Valor inválido. Tente novamente.\n')
                except ValueError: print('Valor inválido. Tente novamente.\n')
            for c in valor:
                c = int(c)
                matriz[l].append(c)
        break
    except ValueError: print('Valor inválido. Tente novamente.\n')

mode="C"
organizar_matriz(matriz)
transpor(matriz,transposta)

mode="L"
organizar_matriz(transposta)

print(len(lista))


for i in lista:
    print(i)

input('\n[ENTER<--]')
    
