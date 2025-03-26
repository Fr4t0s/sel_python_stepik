from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Нажать на кнопку
    browser.find_element(By.CLASS_NAME, "trollface.btn").click()
    
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    
    browser.switch_to.window(new_window)
    
    # находим x и решаем уравнение
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    
    # вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)
    
    # Нажать на кнопку submit
    browser.find_element(By.CLASS_NAME, "btn").click()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()