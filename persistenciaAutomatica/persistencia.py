


#COLOQUEI O COD. A PARTIR DA LINHA 80 COMO ESTAVA NO GIT - TESTE# MATHIAS# 











































































def carregarVendas(filaVendas, listaClientes, listaProdutos):
    garantirArquivo("vendas.csv")

    try:
        with open("vendas.csv", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                partes = linha.split(",")

                if len(partes) != 5:
                    continue

                idVenda = partes[0]
                idCliente = partes[1]
                idProduto = partes[2]

                try:
                    quantidade = int(partes[3])
                except:
                    continue

                cliente = listaClientes.buscarClientePorId(idCliente)
                produto = listaProdutos.buscarProdutoPorId(idProduto)

                if cliente is not None and produto is not None:
                    venda = Venda(idVenda, cliente, produto, quantidade)
                    filaVendas.enqueue(venda)
    except:
        print("Erro ao carregar vendas.")


def salvarVendas(filaVendas):
    try:
        with open("vendas.csv", "w", encoding="utf-8") as arquivo:
            for venda in filaVendas.listar():
                arquivo.write(venda.to_csv())
    except:
        print("Erro ao salvar vendas.")