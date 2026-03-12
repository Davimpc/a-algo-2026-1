import time
import sys

# aumentar o limite de chamadas recursivas. O limite padrão do python lançava um RecursionError
sys.setrecursionlimit(2000)

def fatorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)!
    return n * fatorial(n - 1)

# valores de n para teste
valores = [10, 100, 500, 1000]

print("Medição de tempo - fatorial recursivo\n")

for n in valores:
    inicio = time.perf_counter()
    resultado = fatorial(n)
    fim = time.perf_counter()
    tempo_execucao = fim - inicio

    print(f"n = {n}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos\n")

"""
Medição de tempo - fatorial recursivo

n = 10
Tempo de execução: 0.000008 segundos

n = 100
Tempo de execução: 0.000043 segundos

n = 500
Tempo de execução: 0.000317 segundos

n = 1000
Tempo de execução: 0.000610 segundos

O algoritmo recursivo de cálculo do fatorial possui complexidade assintótica O(n), pois realiza uma chamada recursiva para cada valor de n até chegar ao caso base. 
O número total de chamadas cresce linearmente com o tamanho da entrada. 
"""