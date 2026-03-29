from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--incognito")  #pagina incógnito para evitar

    driver = webdriver.Chrome(options=options)
    return driver