def palindromo(lista):
    # Caso base 1: lista vazio ou 1 elemento: é palíndromo
    if len(lista) <= 1:
        return True
    
    # Caso base 2: primeiro e último elementos diferentes: não é palíndromo
    if lista[0] != lista[-1]:
        return False
    
    # Chamada recursiva: remove o primeiro e o último e verifica o resto
    return palindromo(lista[1:-1])

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

arrays = [array1, array2, array3, array4]

for arr in arrays:
    resultado = "É palíndromo" if palindromo(arr) else "Não é palíndromo"
    print(f"{arr} -> {resultado}")