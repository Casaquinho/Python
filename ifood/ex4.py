def markov(corpus, n):
    # Construir a cadeia de Markov manualmente
    cadeia = {}
    for i in range(len(corpus) - 1):
        elemento_atual = corpus[i]
        elemento_seguinte = corpus[i + 1]
        
        if elemento_atual not in cadeia:
            cadeia[elemento_atual] = {}
        
        if elemento_seguinte not in cadeia[elemento_atual]:
            cadeia[elemento_atual][elemento_seguinte] = 0
        
        cadeia[elemento_atual][elemento_seguinte] += 1

    # Função para escolher o próximo elemento com maior probabilidade (ou em ordem alfabética em caso de empate)
    def proximo_elemento(elemento):
        if elemento not in cadeia:
            return None
        elementos_possiveis = cadeia[elemento]
        
        # Encontrar o elemento com a maior contagem, e o menor lexicograficamente em caso de empate
        maior_probabilidade = max(elementos_possiveis.values())
        candidatos = [proximo_elemento for proximo_elemento in elementos_possiveis if elementos_possiveis[proximo_elemento] == maior_probabilidade]
        
        return min(candidatos)

    # Gerar a sequência de tamanho n começando com 'A'
    sequencia = ['A']
    elemento_atual = 'A'
    
    for _ in range(n - 1):
        elemento_atual = proximo_elemento(elemento_atual)
        if elemento_atual is None:
            break
        sequencia.append(elemento_atual)
    
    return ''.join(sequencia)