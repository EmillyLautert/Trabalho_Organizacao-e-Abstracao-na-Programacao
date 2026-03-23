# Trabalho Avaliativo - Estrutura de Dados com Python

- Instituição: Atitus Educação
- Curso: Ciência da Computação
- Disciplina: Organização e Abstração na Programação
- Estudantes: Camila Campos (RA: 1118454); Emilly Santos (RA: 1138184); Gabriela Ampese (RA: 1138006); Maria Moro (RA: 1138252) e Mathias Stadtlober (RA: 1116251)

## Descrição

O sistema consiste em uma aplicação desenvolvida em Python para gerenciamento de clientes, produtos e vendas. As informações do sistema são organizadas por meio das classes Cliente, Produto e Venda, responsáveis por representar as principais entidades utilizadas na aplicação.

Para garantir a persistência das informações, foram estruturados arquivos de armazenamento em formato CSV, denominados clientes.csv, produtos.csv e vendas.csv. Esses arquivos permitem o registro e manutenção dos dados do sistema.

## Estruturas de Dados Utilizadas

O sistema utiliza três estruturas de dados fundamentais estudadas na disciplina:

- Lista Encadeada
A lista encadeada é utilizada para armazenar os clientes e produtos.
Cada elemento da lista é representado por um nodo, que contém um valor e uma referência para o próximo elemento.
Essa estrutura permite:
Inserção dinâmica de novos elementos;
Percorrer os dados sequencialmente;
Realizar buscas por ID ou nome.

- Fila
A fila é utilizada para armazenar as vendas realizadas.
Ela segue o princípio FIFO (First In, First Out), ou seja, o primeiro elemento inserido é o primeiro a ser processado.
No sistema:
Cada nova venda é adicionada ao final da fila;
A ordem das vendas é preservada.

- Pilha (Stack)
A pilha é utilizada para armazenar o histórico de operações, permitindo desfazer ações realizadas pelo usuário.
Ela segue o princípio LIFO (Last In, First Out), ou seja:
A última operação realizada é a primeira a ser desfeita
Essa estrutura é utilizada para:
Desfazer cadastro de clientes;
Desfazer cadastro de produtos;
Desfazer vendas.

- Persistência Automática em Arquivos
O sistema realiza a persistência dos dados por meio de arquivos no formato CSV:
clientes.csv
produtos.csv
vendas.csv
Funcionamento:
Ao iniciar o sistema, os dados são carregados automaticamente dos arquivos;
Sempre que ocorre uma alteração (cadastro ou venda), os dados são salvos automaticamente;
Caso os arquivos não existam, o sistema os cria automaticamente;
Essa abordagem garante que os dados não sejam perdidos ao encerrar o programa.

## Instruções de Execução do Projeto

Para executar o sistema, siga os passos abaixo:
1. Certifique-se de ter o Python instalado no computador;
2. Abra o terminal ou prompt de comando;
3. Navegue até a pasta do projeto;
4. Execute o main.py;
5. O sistema será iniciado e exibirá um menu interativo no terminal.

## Observações

O sistema não permite cadastros com IDs ou nomes duplicados;
Os dados são mantidos automaticamente entre execuções;
O sistema funciona inteiramente via terminal.