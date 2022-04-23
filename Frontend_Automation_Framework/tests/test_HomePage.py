import time
import pytest
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from TestData import HomePageData
from TestData.HomePageData import *
from pageObjects import *
from pageObjects.ChekoutPage import ChekoutPage
from pageObjects.ConfirmPage import ConfirmPage
from selenium import webdriver

from pageObjects.Homepage import HomePage
from tests.conftest import *
from pageObjects.Homepage import *
from utilities.BaseClass import *
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)

        homepage.getName().send_keys(getData["FirstName"])
        print("It's printing")
        print("A new test Print")
        print("A new test Print")
        print("A new test Print")
        print("A new test Print")
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
        # driver.find_element(By.NAME, 'email').sen d_keys("jrahulkumar6191@yahoo.com")
        # driver.find_element(By.NAME,"name").send_keys("Rahul")
        homepage.getEmail().send_keys(getData["Email"])
        homepage.Pass().send_keys(getData["Password"])
        homepage.CheckBoXClick().click()
        self.SelectOptionByText(homepage.getGender(), "Male")

        homepage.SubmitButton().click()
        out = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.testHomePageData)
    def getData(self, request):
        return request.param
