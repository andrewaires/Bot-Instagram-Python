# Importa a versão mais recente do Selenium para usar com Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class bot_instagram:
    def __init__(self):
        serv = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=serv)
    
    # Seleciona qual perfil entrar
    def entrar(self, link):
        self.driver.get(link)

    # Seleciona o link das fotos do perfil
    def pegar_link(self):
        links = self.driver.find_elements(by='tag name', value='a')
        lista = []
        for link in links:
            href = link.get_attribute('href')
            if href.startswith('https://www.instagram.com/p/'):
                lista.append(href)
        return lista

    # Like nas fotos 
    def curtida(self, url):
        like = self.driver.find_elements(by=By.CLASS_NAME, value='_abl-')
        like[1].click()
    
    # Comenta nas fotos
    def comentar(self, comentario):
        textarea = self.driver.find_element(by='css selector', value='textarea[aria-label="Adicione um comentário..."]')
        time.sleep(1)
        textarea.click()
        time.sleep(1)
        textarea = self.driver.find_element(by='css selector', value='textarea[aria-label="Adicione um comentário..."]')
        time.sleep(1)
        textarea.clear()
        time.sleep(1)
        textarea.send_keys(comentario + Keys.ENTER)
        time.sleep(1)
        

bot = bot_instagram()
# Acessa a página principal do instagram
bot.entrar('https://www.instagram.com/')
# Espera 18s para você realizar o login
time.sleep(18)
# Acessa o perfil
bot.entrar('https://www.instagram.com/forbesbr/')
time.sleep(2)
fotos = bot.pegar_link()

for foto in fotos:
    bot.entrar(foto)
    bot.driver.execute_script('return document.readyState')
    time.sleep(4)
    # Curti a foto
    bot.curtida(foto)
    time.sleep(2)
    # Comenta nas fotas
    bot.comentar('comentário teste')
    time.sleep(2)
