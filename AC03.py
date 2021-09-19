import abc
from unittest import TestCase, main

class Calculadora (object):

    def Calculando(self, valor1, valor2, operador):
        operacao_fabrica = OperacaoFabrica()
        operacao = operacao_fabrica.escolha(operador)
        if(operacao == None):
            return 0 
        else:
            resultado = operacao.executando(valor1, valor2)
            return resultado

class OperacaoFabrica(object):
    def escolha(self, operador):
        if(operador == 'divisao'):
            return Divisao()
        elif(operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
       

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executando(self, valor1, valor2):
        pass

class Divisao(Operacao):
    def executando(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Soma(Operacao):
    def executando(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executando(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado


class Teste(TestCase):
    
    def testando_divisao(self):
        calc = Calculadora()
        self.assertEqual(calc.Calculando(200,2, 'divisao'), 100)

    def testando_soma(self):
        calc1 = Calculadora()
        self.assertEqual(calc1.Calculando(250,100, 'soma'), 350)
    
    def testando_subtracao(self):
        calc2 = Calculadora()
        self.assertEqual(calc2.Calculando(20,10, 'subtracao'), 10)


calcular = Calculadora()
x = calcular.Calculando(10,5, 'soma')
print(x)

if __name__ == '__main__':
    main()