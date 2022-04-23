import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from tests.test_HomePage import *
from tests.conftest import *


@pytest.mark.usefixture("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        l = logging.getLogger(__name__)
        filehandler = logging.FileHandler('C:\\Users\\rkumar\\PycharmProjects\\Frontend_Automation_Framework\\utilities\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        l.addHandler(filehandler)
        l.setLevel(logging.DEBUG)
        l.debug("A debug statement is executed")
        l.info("Information Statement")
        l.warning("Something is in warning mode")
        l.error("Test failed")
        return l

    def VerifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
