sequencia_tribonacci = [0, 0, 1]
    
    for i in range(3, n + 1):
        proximo_termo = sequencia_tribonacci[i - 1] + sequencia_tribonacci[i - 2] + sequencia_tribonacci[i - 3]
        sequencia_tribonacci.append(proximo_termo)
        
    return sequencia_tribonacci[n::-1]