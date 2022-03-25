import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from webdriver_manager import driver

@when(parsers.cfparse("User enter mobile number '{number}' and password '{password}'"))
def login_details(driver, number, password):
  time.sleep(10)
  var = driver.find_element(By.XPATH, '//a[@id="nav-link-accountList"]')
  var.click()
  var1 = driver.find_element(By.XPATH, '//input[@class="a-input-text a-span12 auth-autofocus auth-required-field"]')
  var1.send_keys(number)
  next = driver.find_element(By.XPATH,  '//input[@class="a-button-input"]')
  next.click()
  var2 = driver.find_element(By.XPATH, '//input[@class="a-input-text a-span12 auth-autofocus auth-required-field"]')
  var2.send_keys(password)
  next = driver.find_element(By.XPATH, '//input[@class="a-button-input"]')
  next.click()
  time.sleep(5)