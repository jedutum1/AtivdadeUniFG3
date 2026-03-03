
#QUESTAO 1
'''
a = 8
b = 3

print(a+b*2)
print((a+b)*2)
print(a//b)
print(a%b)
print(a**2/b)
print(a==8)
print(a>b)
print(a!=b)
print(b%2==0)
print(a/b)
'''
'''
#QUESTAO 2

nome = input("Qual seu nome?")
peso = float(input("Qual seu peso em kg?"))
altura = float(input("Qual sua altura em m?"))

imc = peso/(altura**2)

print(f"\n === Resultado para {nome} ===")
print(f"Peso: {peso} kg")
print(f"altura {altura} m")
print (f"IMC : {imc:.2f}")
print(f"Classificação virá na próxima aula")

'''
#QUESTAO 03
'''
nome = input("nome do funcionario: ")
salario = float(input("Digite o salario: "))
desconto = float(input("Digite percentual de desconto do INSS: "))

desconto_INSS = salario * (desconto/100)
salario_liquido = salario - desconto_INSS

print("==============================\n      Holerite do Mês \n==============================")
print(f"Funcionario:       {nome}")
print(f"Salario Bruto:     {salario:,.2f}".replace(',', 'x').replace('.',',').replace('x', '.'))
print(f"Desconto do INSS:  {desconto_INSS:,.2f}".replace(',', 'x').replace('.',',').replace('x', '.'))
print(f"Salario liquido:   {salario_liquido:,.2f}".replace(',', 'x').replace('.',',').replace('x', '.'))

'''

