import time
import requests
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
    
def Telegram(msg, prints):
    msg = msg
    prints = prints
    
    telegram_auth_token = "COLE O TOKEN DA API DO SEU TELEGRAM AQUI"
    telegram_group_id = "COLE AQUI O ID DO GRUPO DO TELEGRAM"
    
    if prints == None:
          telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={msg}"
          requests.post(telegram_api_url)
    else:
        telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendPhoto?chat_id=@{telegram_group_id}&caption={msg}"
        requests.post(telegram_api_url, files={'photo': prints})

def Dashboard():
    servico = Service(ChromeDriverManager().install())
    
    navegador = webdriver.Chrome(service=servico)
    
    navegador.get('Cole aqui o link publico do seu relatório Power Bi')

    navegador.maximize_window()
    
    time.sleep(15)
    
    navegador.save_screenshot('C:\Temp\Print.png')
    
    navegador.close()
    
    msg = "Chamados Resolvidos: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    prints = open("C:\\Temp\\Print.png", 'rb')
    
    Telegram(msg, prints)
    
    
def __init__():
    Telegram("************ INÍCIO ************", None)
    Dashboard()
    Telegram("************ FIM ************", None)
    
__init__()