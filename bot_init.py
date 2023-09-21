from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
import time

def run_bot():
    while True:
        options = Options()
        options.headless = True
        connected = False
        while not connected:
            try:
                driver = webdriver.Firefox(options=options)
                connected = True
            except:
                time.sleep(5) 
                
        driver.get("http://app:5005/champion_emote_unpleased_leverage")
        driver.add_cookie({'name': 'cookie','value': 'bobbed-scorebook-tricycle-thickness'})
        time.sleep(1)
        driver.refresh()
        # Обработка алертов
        try:
            while True:
                alert = Alert(driver)
                alert.accept()
        except:
            pass
        time.sleep(60)
        driver.quit()
