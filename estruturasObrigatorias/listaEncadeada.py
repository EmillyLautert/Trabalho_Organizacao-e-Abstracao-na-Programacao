class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, dado):

        novo = No(dado)

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio

            while atual.proximo:
                atual = atual.proximo

            atual.proximo = novo

    def listar(self):

        atual = self.inicio

        while atual:
            print(atual.dado)
            atual = atual.proximo