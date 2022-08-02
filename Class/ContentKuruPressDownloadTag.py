
from selenium.webdriver.common.by import By
from Class.ContentListTag import ContentListTag

class ContentKuruPressDownloadTag(ContentListTag):
    def __init__(self, driver) :
        self.driver = driver

    def getContentListTags(self):
        self.driver.implicitly_wait(20)
        return self.driver.find_elements(by=By.CSS_SELECTOR, value="#content > article > div.entry-content > table > tbody > tr:not(:first-child) > td")