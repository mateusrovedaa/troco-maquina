import math
from stringbuilder import StringBuilder


class MaquinaDeTroco:

    def __init__(self):
        self.sbNotas = StringBuilder()
        self.sbMoedas = StringBuilder()
        self.notas = [100, 50, 20, 10, 5, 2, 1]
        self.moedas = [50, 25, 10, 5, 1]
        self.valorPago = 0
        self.valorDaConta = 0
        self.troco = 0

    def __validaValor__(self, valor):
        if valor < 0:
            return False
        else:
            return True

    def __calculaNotas__(self, troco):
        vlr = int(troco)
        i = 0
        while vlr != 0:
            c = int(vlr/self.notas[i])
            if c != 0:
                if c > 1 and self.notas[i] > 1:
                    self.sbNotas.Append(str(c)+' notas de R$' +
                                        str(self.notas[i])+' reais')
                    self.sbNotas.Append("\n")
                    vlr = vlr % self.notas[i]
                elif c == 1 and self.notas[i] > 1:
                    self.sbNotas.Append(str(c)+' nota de R$' +
                                        str(self.notas[i])+' reais')
                    self.sbNotas.Append("\n")
                    vlr = vlr % self.notas[i]
                elif c > 1 and self.notas[i] == 1:
                    self.sbNotas.Append(str(c)+' notas de R$' +
                                        str(self.notas[i])+' real')
                    self.sbNotas.Append("\n")
                    vlr = vlr % self.notas[i]
                else:
                    self.sbMoedas.Append(str(c)+' moeda de R$' +
                                         str(self.notas[i])+' real')
                    self.sbMoedas.Append("\n")
                    vlr = vlr % self.notas[i]
            i += 1

    def __calculaMoedas__(self, troco):
        vlr = int(round((troco - int(troco))*100, 2))
        i = 0
        while vlr != 0:
            c = int(vlr/self.moedas[i])
            if c != 0:
                if c > 1 and self.moedas[i] > 1:
                    self.sbMoedas.Append(str(c)+' moedas de R$' +
                                         str(self.moedas[i])+' centavos')
                    self.sbMoedas.Append("\n")
                    vlr = vlr % self.moedas[i]
                elif c == 1 and self.moedas[i] > 1:
                    self.sbMoedas.Append(str(c)+' moeda de R$' +
                                         str(self.moedas[i])+' centavos')
                    self.sbMoedas.Append("\n")
                    vlr = vlr % self.moedas[i]
                elif c > 1 and self.moedas[i] == 1:
                    self.sbMoedas.Append(str(c)+' moedas de R$' +
                                         str(self.moedas[i])+' centavo')
                    self.sbMoedas.Append("\n")
                    vlr = vlr % self.moedas[i]
                else:
                    self.sbMoedas.Append(str(c)+' moeda de R$' +
                                         str(self.moedas[i])+' centavo')
                    self.sbMoedas.Append("\n")
                    vlr = vlr % self.moedas[i]
            i += 1

    def __calculaTroco__(self):
        return(math.fabs(round(self.valorPago, 2)-round(self.valorDaConta, 2)))

    def __calculaValores__(self):
        self.troco = self.__calculaTroco__()
        self.__calculaNotas__(self.troco)
        self.__calculaMoedas__(self.troco)

    def defineValores(self, valordaconta, valorpago):
        if self.__validaValor__(valordaconta) and self.__validaValor__(valorpago):
            self.valorDaConta = float(valordaconta)
            self.valorPago = float(valorpago)
            if self.valorDaConta == 0 and self.valorPago == 0:
                print("É de grátis :)")
            else:
                self.__calculaValores__()
        else:
            print("Os valores precisam ser maiores do que 0")

    def imprimeValores(self):
        if self.valorPago < self.valorDaConta:
            print('Ainda falta pagar: R$'+str(self.troco))
        elif self.valorDaConta % self.valorPago == 0:
            print('Pagamento exato ou não há valor a pagar. Não há troco.')
        else:
            print("------------- Calculando troco -------------")
            print("\n")
            print("Troco: R$", str(round(self.troco, 2)).replace(".", ","))
            print("\n")
            print("Cédulas:")
            print(self.sbNotas)
            print("Moedas:")
            print(self.sbMoedas)
