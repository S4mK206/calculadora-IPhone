from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from os import path


class MeuApp(QMainWindow):

    num1 = 0
    num2 = 0
    numResult = 0
    op = None

    def __init__(self):
        super().__init__()
        loadUi(self.localPath('interfaceCalculadora.ui'), self)

        self.btn0.clicked.connect(lambda: self.btnClicado(self.btn0))
        self.btn1.clicked.connect(lambda: self.btnClicado(self.btn1))
        self.btn2.clicked.connect(lambda: self.btnClicado(self.btn2))
        self.btn3.clicked.connect(lambda: self.btnClicado(self.btn3))
        self.btn4.clicked.connect(lambda: self.btnClicado(self.btn4))
        self.btn5.clicked.connect(lambda: self.btnClicado(self.btn5))
        self.btn6.clicked.connect(lambda: self.btnClicado(self.btn6))
        self.btn7.clicked.connect(lambda: self.btnClicado(self.btn7))
        self.btn8.clicked.connect(lambda: self.btnClicado(self.btn8))
        self.btn9.clicked.connect(lambda: self.btnClicado(self.btn9))
        
        # operacoes
        self.btnAdicao.clicked.connect(lambda: self.definirOperacao(self.adicao))
        self.btnSubtracao.clicked.connect(lambda: self.definirOperacao(self.subtrair))
        self.btnMultiplicacao.clicked.connect(lambda: self.definirOperacao(self.multi))
        self.btnDivisao.clicked.connect(lambda: self.definirOperacao(self.divisao))
        self.btnPorcentagem.clicked.connect(self.porcentagem)

        self.btnVirgula.clicked.connect(lambda: self.btnClicado(self.btnVirgula))
        self.btnPositivoNegativo.clicked.connect(self.sinal)
        self.btnIgual.clicked.connect(self.mostraResultado)
        self.btnClear.clicked.connect(self.limparDisplay)

    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',') #transforma tudo que for int em str e mostra no display
        self.outputLabel.setText(value)

    def pegarDisplay(self):
        value = str(self.outputLabel.text())
        value = value.replace(',', '.')
        try:
            value = int(value)
        except:
            value = float(value)
        return value

    def virgula(self):
        if not '.' in str(self.pegarDisplay()):
            self.mostrarDisplay(str(self.pegarDisplay()) + '.')

    def btnClicado(self, btn):
        ultimoValor = str( self.pegarDisplay() )
        #Digitando virgula
        if btn.text() == ',':
            if isinstance(self.pegarDisplay(), float):
                return
        #Digitando numeros
        else:
            # Se for numero inteiros
            if isinstance(self.pegarDisplay(), int):
                if self.pegarDisplay() == 0:
                    ultimoValor = ''
            # Se for numero float
            else:
                if self.outputLabel.text()[-1] == ",":
                    ultimoValor = self.outputLabel.text()
        self.mostrarDisplay(ultimoValor + btn.text())

    def adicao(self):
        return self.num1 + self.num2
    
    def subtrair(self):
        return self.num1 - self.num2
    
    def multi(self):
        return self.num1 * self.num2
    
    def divisao(self):
        return self.num1 / self.num2
    
    def sinal(self):
        texto_atual = (self.pegarDisplay())
        texto_atual*=-1
        self.mostrarDisplay(str(texto_atual))

    def porcentagem(self):
        percento = self.pegarDisplay() / 100
        if self.op == self.adicao or self.subtrair:
            percento = self.num1 * percento
        self.mostrarDisplay(percento)

    def limparDisplay(self):
        self.num1 = 0
        self.num2 = 0
        self.numResult = 0
        self.op = None
        self.mostrarDisplay(0)

    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)

    def resultado(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op()
        else:
            print("não tem operação")

    def mostraResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()

            self.numResult = self.op()
            self.mostrarDisplay(self.numResult)

    def localPath(relativePath):
        return f'{path.dirname(path.realpath(__file__))}\\{relativePath}'

if __name__ == '__main__':
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()