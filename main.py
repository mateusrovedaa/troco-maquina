from maquinadetroco import MaquinaDeTroco

mt = MaquinaDeTroco()

print("Máquina de Troco")

valorconta = input('Digite o valor total da conta: R$').replace(",", ".")
while mt.defineValor(valorconta) is False:
    print("Digite apenas números, utilizando vírgula (,) ou ponto (.)")
    valorconta = input(
        'Digite o valor total da conta: R$').replace(",", ".")
valorcontavalidado = float(valorconta)

valorpago = input('Digite o valor pago: R$').replace(",", ".")
while mt.defineValor(valorpago) is False:
    print("Digite apenas números, utilizando vírgula (,) ou ponto (.)")
    valorpago = input('Digite o valor pago: R$').replace(",", ".")
valorpagovalidado = float(valorpago)

mt.defineValoresCalculo(valorcontavalidado, valorpagovalidado)
mt.imprimeValores()
