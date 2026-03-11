class Vendas:
    def __init__(self):
        self.fila = []

    def enfileirar(self, venda):
        self.fila.append(venda)

    def desenfileirar(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)

    def listar(self):
        return self.fila