from classesMinimas.cliente import Cliente
from classesMinimas.produto import Produto
from classesMinimas.venda import Venda

def menu():

    while True:

        print("===== MENU ESTOQUE =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Cadastrar produto")
        print("4 - Listar produtos")
        print("5 - Pesquisar produto")
        print("6 - Realizar venda")
        print("7 - Ver fila de vendas")
        print("8 - Desfazer última operação")
        print("9 - Exibir valor total do estoque")
        print("10 - Exibir valor total de vendas")
        print("11 - Exibir clientes e valores gastos")
        print("12 - Sair")

        opcao = input("Digite o número da consulta: ")
        if opcao == "12":
            break
menu()