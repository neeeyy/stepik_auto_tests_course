import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    print(text)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    button.click()

    input_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control"))
    )
    num = browser.find_element(By.ID, "input_value").text
    num = int(num)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    result = calc(num)
    input = browser.find_element(By.CLASS_NAME, "form-control")
    input.send_keys(result)

    but1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    but1.click()


    alert = browser.switch_to.alert.text
    alert = alert.split(': ')[-1]
    print(alert)

    browser = webdriver.Chrome()
    browser.get("https://stepik.org/")
    browser.add_cookie({
        "name": "sessionid",
        "value": "hkwev63fsu382dxz0s5h7ccrqgvzgk6n",
        "domain": "stepik.org"
    })
    browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')

    inp = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area.ember-view"))
    )
    inp.send_keys(alert)
    but1 = browser.find_element(By.CLASS_NAME, "submit-submission")
    time.sleep(66)
    but1.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()