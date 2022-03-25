
from pytest_bdd import when
from selenium.webdriver.common.by import By

@when("User click add cart")
def cart(driver):
    do = driver.find_element(By.XPATH, '//a[@class="nav-a nav-a-2 nav-progressive-attribute"]')
    do.click()

@when("User click proceed to buy")
def buy(driver):
    do1 = driver.find_element(By.XPATH, '//input[@name="proceedToRetailCheckout"]')
    do1.click()