import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_function():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://stage.alnafi.com/auth/sign-in')
    driver.maximize_window()


def teardown_function():
    driver.quit()


def my_cred():
    return [
        ('abdeali@gmail.com', 'abdeali@123'),
        ('ali@gmail.com', 'ali@123'),
        ('abd@gmail.com', 'abd@123')
    ]


@pytest.mark.parametrize("username,password", my_cred())
def test_login(username, password):
    print("My pytest login")
    driver.find_element(By.ID, 'Username/ Email').send_keys(username)
    time.sleep(0.7)
    driver.find_element(By.ID, 'Password').send_keys(password)
    time.sleep(0.7)
    allure.attach(driver.get_full_page_screenshot_as_png(), name="myalnafi_sc", attachment_type=AttachmentType.PNG)
