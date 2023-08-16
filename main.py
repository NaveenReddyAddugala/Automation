from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://automated.pythonanywhere.com/')
d=driver.find_element(By.XPATH,'/html/body/div[1]/div/h1[1]')
print(d.text)