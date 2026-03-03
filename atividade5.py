'''

#QUESTAO 1

x = 5
y = 9

if x > 10:
    if y > 5:
        print("A")
    else:
        print("B")
elif x == 10:
    print("C")
else:
    print("D")

print("FIM")

#PERGUNTA 1: IMPRIME A
#PERGUNTA 2: IMPRIME C
#PERGUNTA 3: IMPRIME D
#PERGUNTA 4: EXISTEM 3 CAMINHOS A DEPENDER DO VALOR DE X

'''
'''
#QUESTAO 2

lado_a = float(input("Digite o o valor do lado 1: "))
lado_b = float(input("Digite o o valor do lado 2: "))
lado_c = float(input("Digite o o valor do lado 3: "))

if(lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b+lado_c > lado_a):
    if(lado_a == lado_b and lado_b == lado_c and lado_c == lado_a):
        print("Triangulo equilatero!!!")
    elif (lado_a != lado_b and lado_a != lado_c and lado_b != lado_c):
        print("Triangulo escaleno")
    else:
        print("Triangulo Isósceles")
else:
    print("Não é um triangulo")

'''

#QUESTAO 3.1

valor_pedido = float(input("Digite o valor do pedido: "))
frete = 9.99

if (valor_pedido < 20.0):
    print (frete)
elif (valor_pedido >= 20.0 and valor_pedido < 50.0):
    frete = 5.99
    print(frete)
elif(valor_pedido >= 50.0):
    frete = 0
    print(frete)

