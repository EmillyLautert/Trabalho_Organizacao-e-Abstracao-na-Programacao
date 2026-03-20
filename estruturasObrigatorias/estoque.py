from classesMinimas import Cliente
from classesMinimas import Produto
from classesMinimas import Venda
from listaEncadeada import ListaEncadeada
from pilha import Pilha
from fila import Fila
from persistenciaAutomatica import (carregarClientes, salvarClientes, carregarProdutos, salvarProdutos, carregarVendas, salvarVendas)

class SistemaEstoque:
    def __init__(self):
        self.listaClientes = ListaEncadeada()
        self.listaProdutos = ListaEncadeada()
        self.filaVendas = Fila()
        self.historicoOperacoes = Pilha()

        carregarClientes(self.listaClientes)
        carregarProdutos(self.listaProdutos)
        carregarVendas(self.filaVendas, self.listaClientes, self.listaProdutos)

    def cadastrarCliente(self):
        print("\n===== CADASTRAR CLIENTE =====")
        idCliente = input("Digite o ID do cliente: ").strip()
        nomeCliente = input("Digite o nome do cliente: ").strip()

        if idCliente == "" or nomeCliente == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        if self.listaClientes.buscarClientePorId(idCliente) is not None:
            print("Erro: o ID do cliente já existe.")
            return

        if self.listaClientes.buscarClientePorNome(nomeCliente) is not None:
            print("Erro: o nome do cliente já existe.")
            return

        cliente = Cliente(idCliente, nomeCliente)
        self.listaClientes.inserirFim(cliente)
        salvarClientes(self.listaClientes)

        self.historicoOperacoes.push(("cadastroCliente", cliente.idCliente))
        print("Cliente cadastrado com sucesso.")

    def listarClientes(self):
        print("\n===== LISTA DE CLIENTES =====")
        clientes = self.listaClientes.listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(cliente)
            
    def cadastrarProduto(self):
        print("\n===== CADASTRAR PRODUTO =====")
        idProduto = input("Digite o ID do produto: ").strip()
        nomeProduto = input("Digite o nome do produto: ").strip()

        if idProduto == "" or nomeProduto == "":
            print("Erro: ID e nome são obrigatórios.")
            return

        if self.listaProdutos.buscarProdutoPorId(idProduto) is not None:
            print("Erro: o ID do produto já existe.")
            return

        if self.listaProdutos.buscarProdutoPorNome(nomeProduto) is not None:
            print("Erro: o nome do produto já existe.")
            return

        try:
            quantidadeEstoque = int(input("Digite a quantidade em estoque: "))
            precoProduto = float(input("Digite o preço do produto: "))
        except:
            print("Erro: quantidade e preço devem ser numéricos.")
            return

        if quantidadeEstoque < 0:
            print("Erro: a quantidade não pode ser negativa.")
            return

        if precoProduto <= 0:
            print("Erro: o preço deve ser maior que zero.")
            return

        produto = Produto(idProduto, nomeProduto, quantidadeEstoque, precoProduto)
        self.listaProdutos.inserirFim(produto)
        salvarProdutos(self.listaProdutos)

        self.historicoOperacoes.push(("cadastroProduto", produto.idProduto))
        print("Produto cadastrado com sucesso.")

    def listarProdutos(self):
        print("\n===== LISTA DE PRODUTOS =====")
        produtos = self.listaProdutos.listar()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        for produto in produtos:
            print(produto)

    def pesquisarProduto(self):
        print("\n===== PESQUISAR PRODUTO =====")
        opcao = input("Pesquisar por 1-ID ou 2-Nome? ").strip()

        if opcao == "1":
            idProduto = input("Digite o ID do produto: ").strip()
            produto = self.listaProdutos.buscarProdutoPorId(idProduto)
        elif opcao == "2":
            nomeProduto = input("Digite o nome do produto: ").strip()
            produto = self.listaProdutos.buscarProdutoPorNome(nomeProduto)
        else:
            print("Opção inválida.")
            return

        if produto is None:
            print("Produto não encontrado.")
        else:
            print(produto)