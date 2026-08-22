# 🐍 Automação com Python

Script de automação de tela (RPA) que usa **PyAutoGUI** e **Pandas** para cadastrar produtos automaticamente em um sistema web, lendo os dados diretamente de uma planilha CSV.

## 📋 Sobre o projeto

Em vez de digitar manualmente dezenas (ou centenas) de produtos em um sistema de cadastro, este script:

1. Abre o navegador Chrome;
2. Acessa o sistema web e realiza o login automaticamente;
3. Lê a base de produtos de um arquivo `produtos.csv`;
4. Preenche o formulário de cadastro linha a linha, campo a campo, simulando cliques e digitação real do usuário.

É um projeto de estudo focado em **automação de processos repetitivos (RPA)** com Python.

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — controle de mouse e teclado
- [Pandas](https://pandas.pydata.org/) — leitura e manipulação do CSV

## 📁 Estrutura do projeto

```
Automacao-com-Python/
├── Automacao.py     # Script principal da automação
├── produtos.csv      # Base de dados dos produtos a serem cadastrados
└── README.md
```

## ⚙️ Como executar

### Pré-requisitos

- Python 3 instalado
- Google Chrome instalado

### Instalação

```bash
pip install pyautogui pandas
```
