
'''
#QUESTAO 1

temperatura_celsius = float(input("Digite a temperatura em celsius"))
temperatura_farenheit = temperatura_celsius * 9/5 + 32
temperatura_kelvin = temperatura_celsius + 273.35

print (f"Temperatura em Farenheit: {temperatura_farenheit:.2f} F \n")
print(f"Temperatua em Kelvin {temperatura_kelvin:.2f} K \n")

'''

'''
#QUESTAO 2

distancia = float(input("Digitie a distância em km: "))
consumo_carro = float(input("Digite o consumo do carro em km/l: "))
preco_litro = float(input("Digite o preço do litro de combustível: "))

print (f"Litros Necessários: " + str(distancia/consumo_carro)+"Litros")
print (f"O Valor da viagem ficou: R$ " + str((distancia/consumo_carro)*preco_litro))
print(f"Custo por KM rodado em R$ : " + str((1.0/consumo_carro) * preco_litro))

'''

