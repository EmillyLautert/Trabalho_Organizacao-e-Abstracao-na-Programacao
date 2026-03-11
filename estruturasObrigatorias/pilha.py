class Operacoes:
    def __init__(self):
        self.pilha = []

    def empilhar(self, operacao):
        self.pilha.append(operacao)

    def desempilhar(self):
        if len(self.pilha) > 0:
            return self.pilha.pop()

    def vazia(self):
        return len(self.pilha) == 0