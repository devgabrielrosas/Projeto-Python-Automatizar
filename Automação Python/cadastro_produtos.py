# Projeto para automatizar cadastro hipotético de produtos em um formulário
# Baseado na Jornada Python da Hashtag Programação

# 1º Entrar no sistema de cadastro
import pyautogui
pyautogui.PAUSE = 0.9

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

from time import sleep

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press("enter")
sleep(3)

# 2º Logar a conta hipotética
pyautogui.press("tab")
pyautogui.write("emailhipotetico@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhahipotetica")
pyautogui.hotkey("tab", "enter")
sleep(3)

# 3º Cadastrar os produtos
import pandas
produtos = pandas.read_csv("produtos.csv")

for linha in produtos.index:
    
    str(produtos.loc[linha, "codigo"])
    pyautogui.click(401,258)
    pyautogui.write(str(produtos.loc[linha, "codigo"]))

    str(produtos.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "marca"]))

    str(produtos.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "tipo"]))

    str(produtos.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "categoria"]))

    str(produtos.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "preco_unitario"]))

    str(produtos.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(str(produtos.loc[linha, "custo"]))

    obs = str(produtos.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(str(produtos.loc[linha, "obs"]))

    pyautogui.hotkey("tab", "enter")
    pyautogui.scroll(1000)