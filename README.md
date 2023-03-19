# Bot em Python para o Instagram
Bot desenvolvido com Python através do framework Selenium 4 para comentar e dar like em postagens do Instagram.

### Requisitos
- Selenium a partir da versão 4<br>
*Foi testado até a versão 4.8.2 do Selenium.*
- Webdriver manager instalado

## Como usar?

1. Instalar o Selenium  
- Abra o Prompt e digite este comando:
```
pip install selenium
```

2. Instalar o webdriver-manager
- Ainda no Prompt, digite o seguinte comando:
```
pip install webdriver-manager
```

3. Faça um Git Clone para usar o código do bot na sua máquina.
4. Se você usa o Chrome como navegador, basta rodar o código do bot na sua IDE.<br>
As linhas seguintes de código são responsáveis por importar o Webdriver para usar no Chrome:
```Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
```
Se você usa outro navegador, recomendo que use este repositório e procure o nome do seu navegador para instalar corretamente o Webdriver:
https://github.com/SergeyPirogov/webdriver_manager#install-manager

## Instruções para mudar o perfil e comentário
1. Na linha 54 do arquivo main você pode editar o perfil que deseja acessar, basta trocar o link:
```python
bot.entrar('https://www.instagram.com/forbesbr/')
```
2. Na linha 66 você pode mudar o comentário:
```python
bot.comentar('comentário teste')
```


