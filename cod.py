import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

# Abrir navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# Entrar no site da empresa
pyautogui.write("https://site-empresa.com")
pyautogui.press("enter")
time.sleep(2)

# Login no site
pyautogui.press("tab")
pyautogui.write("E-mail") # Usuario/Email
pyautogui.press("tab")
pyautogui.write("Senha") # Usuario/Email
pyautogui.press("enter") # Login
time.sleep(2)

# Preenche o formulario para cada produto
produtos = pandas.read_csv("produtos.csv")

for l in produtos.index:
    for c in produtos.columns:
        pyautogui.press("tab")

        if str(produtos.loc[l, c]) != "nan":
            pyautogui.write(str(produtos.loc[l, c]))  

    pyautogui.press("enter")

    pyautogui.press("f5")
    time.sleep(2)