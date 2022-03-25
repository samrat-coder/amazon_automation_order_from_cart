import time
from select import select

from pytest_bdd import when, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when(parsers.cfparse("User select country name '{nam}'"))
def country(driver, nam):
    time.sleep(5)
    country = driver.find_element(By.XPATH, '//select[@id="address-ui-widgets-countryCode-dropdown-nativeId"]')
    number = Select(country)
    number.select_by_visible_text(nam)

@when(parsers.cfparse("User select name '{Name}'"))
def Full_Name(driver, Name):
    Full = driver.find_element(By.XPATH, '//input[@name="address-ui-widgets-enterAddressFullName"]')
    Full.send_keys(Name)


@when(parsers.cfparse("User select mobile no '{Mobile_number}'"))
def Mobile(driver, Mobile_number):
    MOb = driver.find_element(By.XPATH, '//input[@id="address-ui-widgets-enterAddressPhoneNumber"]')
    MOb.send_keys(Mobile_number)

@when(parsers.cfparse("User select pincode '{pin_number}'"))
def Pincode(driver, pin_number):
    pincode = driver.find_element(By.XPATH, '//input[@id="address-ui-widgets-enterAddressPostalCode"]')
    pincode.send_keys(pin_number)

@when(parsers.cfparse("User select Flat no '{Building_no}'"))
def House_no(driver, Building_no):
    House_no = driver.find_element(By.XPATH, '//input[@id="address-ui-widgets-enterAddressLine1"]')
    House_no.send_keys(Building_no)

@when(parsers.cfparse("User select street '{Street_name}'"))
def Area(driver, Street_name):
    Area = driver.find_element(By.XPATH, '//input[@id="address-ui-widgets-enterAddressLine2"]')
    Area.send_keys(Street_name)

@when(parsers.cfparse("User select landmark '{Landmark_name}'"))
def Landmark(driver, Landmark_name):
    Landmark = driver.find_element(By.XPATH, '//input[@id="address-ui-widgets-landmark"]')
    Landmark.send_keys(Landmark_name)

@when(parsers.cfparse("User select town '{City_name}'"))
def Town(driver, City_name):
    Town = driver.find_element(By.XPATH, '//input[@id="address-ui-widgets-enterAddressCity"]')
    Town.send_keys(City_name)


@when("User select state")
def state(driver):
    state = driver.find_element(By.XPATH, '//select[@id="address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId"]')
    number = Select(state)
    number.select_by_value('WEST BENGAL')


@when("User select address type")
def Address_type(driver):
    Address = driver.find_element(By.XPATH, "//span[@id='address-ui-widgets-addr-details-address-type-and-business-hours']")
    Address.click()
    driver.find_element(By.XPATH, "//a[@data-value='RES']").click()
    # number.select_by_visible_text(' Home (7 am – 9 pm delivery) ')


@when("User select use to address")
def Use_address(driver):
    use = driver.find_element(By.XPATH, '//input[@type="submit"]')
    use.click()