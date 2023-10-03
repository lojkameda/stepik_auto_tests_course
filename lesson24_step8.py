from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text

def calc (y):
    return math.log(math.fabs(12*math.sin(y)))

try:
    browser.get(link)
    # price_value = browser.find_element(By.ID, "price")
    a = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x_value = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(calc(x_value))
    browser.find_element(By.ID, "solve").click()



finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    print("ok")
    # browser.quit()
