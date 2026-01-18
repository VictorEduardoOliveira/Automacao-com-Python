import pyautogui
import time
import pandas

#link do sistema para o teste
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "seuemail@gmail.com"
senha = "essaeasenha"

pyautogui.PAUSE = 0.5

# Abrir o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Tempo de espera para abrir o navegador
time.sleep(3)

# Entrar no site
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Logar no site
pyautogui.click(x=491, y=402)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# Importar o banco de dados 
tabela = pandas.read_csv("produtos.csv")

# Colocar todas as informações do banco de dados
for linhas in tabela.index:
    pyautogui.click(x=568, y=291)
    codigo = str(tabela.loc[linhas, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linhas, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linhas, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linhas, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco = str(tabela.loc[linhas, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    custo = str(tabela.loc[linhas, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linhas, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Voltar para o topo da pagina
    pyautogui.scroll(5000)