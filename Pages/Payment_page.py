import time

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when(parsers.cfparse("User select other upi '{Upi_id}'"))
def payment_method(driver, Upi_id):
    time.sleep(10)
    method = driver.find_element(By.XPATH, "//span[text()='Other UPI Apps' and @class='a-color-base a-text-bold']")
    method.click()
    put = driver.find_element(By.XPATH, "//span[text()='Other UPI Apps' and @class='a-color-base a-text-bold']//ancestor::div[3]/div[3]//input[@type='text']")
    put.send_keys(Upi_id)
    sub = driver.find_element(By.XPATH, '//input[@name="ppw-widgetEvent:ValidateUpiIdEvent"]')
    sub.click()
    time.sleep(10)
