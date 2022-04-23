import time
import pytest
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageObjects import *
from pageObjects.ChekoutPage import ChekoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.Homepage import HomePage
from utilities.BaseClass import *
from tests.conftest import *


@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        checkOutpage = homepage.ShopItems()
        log.info("Getting all the card details")
        # checkOutpage = ChekoutPage(self.driver)
        # confirmpage = ConfirmPage(self.driver)
        checkOutpage.getCardTitles()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutpage.getCardFooter()[i].click()

        confirmpage = checkOutpage.getcheckoutShop().click()
        confirmpage = checkOutpage.getCheckout()
        log.info("Entering Country Name")
        confirmpage.country_Names_List().send_keys("India")
        self.VerifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmpage.Terms_And_Conditions().click()
        confirmpage.TermsConditionsClick().click()
        textmatch = confirmpage.SuccessTextMatch().text
        assert ("Success! Thank !" in textmatch)
