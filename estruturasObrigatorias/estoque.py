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