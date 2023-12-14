# Classe elevador

class Elevador(object):

    # Método construtor
    def __init__(self, andarAtual, portaAberta, peso):
        self.andarAtual = andarAtual
        self.portaAberta = portaAberta
        self.peso = peso

    # Encapsulamento
    def setAndarAtual(self, andarAtual):
        self.andarAtual = andarAtual

    def getAndarAtual(self):
        return self.andarAtual

    def setPortaAberta(self, portaAberta):
        self.portaAberta = portaAberta

    def getPortaAberta(self):
        return self.portaAberta

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def __str__(self):
        return(
            '\n Andar Atual.....................' + str(self.getAndarAtual()) +
            str('\n Peso............................{:.2f}').format(self.getPeso()) +
            '\n Porta Aberta....................' + str(self.getPortaAberta())
        )

    # Métodos
    def subir(self, andarDesejado):
        if self.fecharPorta():
            while andarDesejado > self.getAndarAtual():
                self.andarAtual+=1
                print(f'{self.andarAtual}º andar...')
        else:
            print('Excesso de peso!')

    def descer(self, andarDesejado):
        if self.fecharPorta():
            while andarDesejado < self.getAndarAtual():
                self.andarAtual-=1
                print(f'{self.getAndarAtual()}º andar... ')
        else:
            print('Excesso de peso!')

    def fecharPorta(self):
        if self.getPeso() < 750:
            self.setPortaAberta(False)
        return not self.getPortaAberta()
