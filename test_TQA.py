import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep



class HelloWorld(unittest.TestCase):
    driver: WebDriver = webdriver.Chrome(executable_path="chromedriver.exe")
    @classmethod
    def SetUp(cls):
        driver = cls.driver
        driver.implicitly_wait(10)


    def test1_hello_world(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(2)
        usuario = driver.find_element(By.ID, "user-name")
        usuario.send_keys("standard_user")
        sleep(2)
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        sleep(2)
        button = driver.find_element(By.ID, "login-button")
        button.click()

    def test2_login_true(self):
        driver = self.driver
        input_user = driver.find_element(By.ID, self.input_user)
        input_user.send_keys("standard_user")
        input_user.submit()
        input_password = driver.find_element(By.ID, self.input_password)
        input_password.send_keys("secret_sauce")
        button = driver.find_element(By.ID, self.button)
        button.click()
        init_page = driver.find_element(By.XPATH, self.xpath_page_init).is_displayer()
        self.asserttrue(init_page, "Not view page init")

print("Login correcto")


if __name__ == '__main__':
    print_hi('PyCharm')

