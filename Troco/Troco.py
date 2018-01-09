print("\n### TROCO ###")

compra = float(input("\nValor Compra: "))                             #definição das variáveis
dinheiro = float(input("\nValor Dinheiro: "))
quantidade = 0
troco = dinheiro - compra

print("\nTroco R$ ", troco)

moedasDisponiveis = [100, 50, 10, 5, 1, 0.5, 0.1, 0.05, 0.01]       #definindo vetor
moedasUtilizadas = {}

for i in range(len(moedasDisponiveis)):                             #condição quantidade de moedas
    numMoedas = troco // moedasDisponiveis[i]                      
    troco -= numMoedas * moedasDisponiveis[i]
    quantidade += numMoedas
    if numMoedas > 0:
        moedasUtilizadas[moedasDisponiveis[i]] = numMoedas         #condição número de moedas utilizadas

print("\nQuantidade Moedas:", quantidade)                             #imprime a quantidade de moedas
print("Moedas Utilizadas:")                                         #imprime as moedas utilizadas
for moeda, quantidade in moedasUtilizadas.items():
    print("Moeda de", moeda, "->", quantidade)

input("\nPressione enter para sair!")                             
