from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryList = (By.CSS_SELECTOR, "input#country")
    NationName = (By.LINK_TEXT, "India")
    TermsConditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    TermsConditions_Click = (By.CSS_SELECTOR, "[type='submit']")
    TextMatch = (By.CSS_SELECTOR, "[class*='alert-success']")

    def country_Names_List(self):
        return self.driver.find_element(*ConfirmPage.countryList)

    # def CountryNames(self):
    #     # self.driver.find_element(By.LINK_TEXT, "India").click()
    #     return self.driver.find_element(*ConfirmPage.NationName)

    def Terms_And_Conditions(self):
        return self.driver.find_element(*ConfirmPage.TermsConditions)

    def TermsConditionsClick(self):
        return self.driver.find_element(*ConfirmPage.TermsConditions_Click)

    def SuccessTextMatch(self):
        return self.driver.find_element(*ConfirmPage.TextMatch)
