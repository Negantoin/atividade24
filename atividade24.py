# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um número: "))
tabuada = (1,2,3,4,5,6,7,8,9,10)
for numeros in tabuada:
    print(numero * numeros)