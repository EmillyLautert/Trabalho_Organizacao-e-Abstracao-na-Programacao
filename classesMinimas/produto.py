class Produto:
    def __init__(self, idProduto, nomeProduto, quantidadeEstoque, precoProduto):
        self.idProduto = idProduto
        self.nomeProduto = nomeProduto
        self.quantidadeEstoque = quantidadeEstoque
        self.precoProduto = precoProduto

    def __str__(self):
        return f"ID: {self.idProduto}, Nome: {self.nomeProduto}, Quantidade em Estoque: {self.quantidadeEstoque}, Preço: R${self.precoProduto}"