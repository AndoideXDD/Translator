from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time






conjuntoSignos = ("tú","como","estar")

conjuntoTraducidoIngles = ("")

for n in conjuntoSignos:
    if n == "hola":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "hi " 

    if n == "bueno":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "good "

    if n == "dia":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "day "

    if n == "estar" :

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "are "

    if n == "bien":

        #Possible fallo en palabra con múltiple signuficado
        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "ok "

    if n == "tú":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "you "

    if n == "estoy":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "am "

    if n == "yo":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "I "

    if n == "gracias":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "thanks "

    if n == "jugar":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "play "

    if n == "futbol":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "futbol "

    if n == "como":

        conjuntoTraducidoIngles = conjuntoTraducidoIngles + "how "





driver = webdriver.Chrome()

driver.get("https://translate.google.com/?hl=es%22")
try:
    time.sleep(10)

    elem = driver.find_element(By.TAG_NAME, 'textarea')
    elem.clear()
    elem.send_keys(conjuntoTraducidoIngles)
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.close()


except: 
    pass

print(conjuntoTraducidoIngles)