# Automação de Cadastro de Produtos (RPA)

Script de automação de tela (RPA) em Python que cadastra produtos automaticamente em um sistema web, lendo os dados de uma planilha CSV.

## Como funciona

O script abre o navegador, faz login no sistema, e para cada produto da planilha `produtos.csv`, preenche automaticamente os campos (código, marca, tipo, categoria, preço unitário, custo, observação) usando simulação de teclado e mouse.

## Tecnologias utilizadas

- Python
- PyAutoGUI (automação de teclado/mouse)
- Pandas (leitura da planilha)
- python-dotenv (variáveis de ambiente)

## Como rodar o projeto

### 1. Clonar o repositório
\`\`\`bash
git clone https://github.com/VictorEduardoOliveira/Automacao-com-Python.git
cd Automacao-com-Python
\`\`\`

### 2. Instalar as dependências
\`\`\`bash
pip install pyautogui pandas python-dotenv
\`\`\`

### 3. Configurar as credenciais
Crie um arquivo `.env` na raiz do projeto com:
\`\`\`
LOGIN_EMAIL=seuemail@gmail.com
LOGIN_SENHA=suasenha
\`\`\`

> O login nunca fica exposto no código — é carregado via variável de ambiente com `python-dotenv`.

### 4. Rodar o script
\`\`\`bash
python Automacao.py
\`\`\`

> ⚠️ O PyAutoGUI controla o mouse e teclado de verdade. Não mexa no computador enquanto o script estiver rodando.

## Autor

Victor Eduardo Oliveira
[LinkedIn](https://www.linkedin.com/in/victor-eduardo75/) | [GitHub](https://github.com/VictorEduardoOliveira)
