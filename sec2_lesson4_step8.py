from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # ожидание цены и клик по кнопке 
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 
    browser.find_element(By.ID, "book").click()
    
    # находим x и решаем уравнение
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    
    # вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)
    
    # Нажать на кнопку submit
    browser.find_element(By.ID, "solve").click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()