import time

from pytest_bdd import given, then, when
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@given("User create driver", target_fixture="driver")
def create_driver():
    service = Service(executable_path=ChromeDriverManager().install())
    # service = Service(executable_path="/home/hasan/Downloads/chromedriver")
    driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(executable_path="")
    # driver.maximize_window()
    return driver


@given("User open url")
def open_url(driver):
    driver.get("https://www.amazon.in/")


@when("switch to window")
def switch_to_next_tab(driver):
    parent_window = driver.current_window_handle
    print(driver.current_window_handle)
    child_windows = driver.window_handles
    for child in child_windows:
        if parent_window == child:
            pass
        else:
            driver.switch_to.window(child)
            break

time.sleep(5)
@then("User close driver")
def close_driver(driver):
    driver.quit()
