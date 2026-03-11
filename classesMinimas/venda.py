class Venda:
    def __init__(self, idVenda, cliente, produto, quantidade, valorTotal):
        self.idVenda = idVenda
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valorTotal = valorTotal
        
    def __str__(self):
        return f"ID: {self.idVenda}, Cliente: {self.cliente.nomeCliente}, Produto: {self.produto.nomeProduto}, Quantidade: {self.quantidade}, Valor Total: R${self.valorTotal}"