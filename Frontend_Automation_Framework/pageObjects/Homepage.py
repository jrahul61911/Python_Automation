from selenium.webdriver.common.by import By

from pageObjects.ChekoutPage import ChekoutPage
from tests.conftest import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, 'email')
    checkBox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    gender = (By.ID, "exampleFormControlSelect1")
    password = (By.ID,"exampleInputPassword1")

    def ShopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutpage = ChekoutPage(self.driver)
        return checkOutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def CheckBoXClick(self):
        return self.driver.find_element(*HomePage.checkBox)

    def SubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def Pass(self):
        return self.driver.find_element(*HomePage.password)