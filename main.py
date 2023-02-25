# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# aqui começa o bot
class bot_instagram:
    def __init__(self):
        serv = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=serv)
    
    # seleciona qual perfil entrar
    def entrar(self, link):
        self.driver.get(link)

    # seleciona o link das fotos do perfil
    def pegar_link(self):
        links = self.driver.find_elements(by='tag name', value='a')
        lista = []
        for link in links:
            href = link.get_attribute('href')
            if href.startswith('https://www.instagram.com/p/'):
                lista.append(href)
        return lista

    # comenta nas fotos
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
# acessa a página principal do instagram
bot.entrar('https://www.instagram.com/')
# espera 15s para você realizar o login
time.sleep(15)
# acessa o perfil
bot.entrar('https://www.instagram.com/forbesbr/')
time.sleep(2)
fotos = bot.pegar_link()
print(fotos)

for foto in fotos:
    bot.entrar(foto)
    bot.driver.execute_script('return document.readyState')
    time.sleep(4)
    # comenta nas fotas
    bot.comentar('comentário teste')
    time.sleep(2)
