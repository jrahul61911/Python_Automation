from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class ChekoutPage:

    def __init__(self, driver):
        self.driver = driver

    #  cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.XPATH, "//button[@class='btn btn-info']")
    checkout_shop = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*ChekoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*ChekoutPage.cardFooter)

    def getcheckoutShop(self):
        return self.driver.find_element(*ChekoutPage.checkout_shop)

    def getCheckout(self):
        self.driver.find_element(*ChekoutPage.checkout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

