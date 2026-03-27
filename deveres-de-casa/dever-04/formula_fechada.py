import math

# Função recursiva
def F_recursivo(n):
    # Caso base
    if n == 1:
        return 2
    
    # Chamada recursiva
    return 2 * F_recursivo(n - 1) + n**2


# Fórmula fechada
def F_formula(n):
    # Fórmula obtida matematicamente
    return (n**2 + 2*n + 2) * (2**(n-1)) - (n**2 + 2*n + 2)


while(True):
    try:
        n = int(input("Digite um valor de n (não muito grande): "))
        # Cálculo recursivo
        resultado_recursivo = F_recursivo(n)
        # Cálculo pela fórmula
        resultado_formula = F_formula(n)
        break
    except RecursionError:
        print("Número muito grande")

print(f"\nResultado recursivo: F({n}) = {resultado_recursivo}")
print(f"Resultado pela fórmula fechada: F({n}) = {resultado_formula}")