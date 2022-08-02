
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ContentListClass : 
    driver :webdriver

    def __init__(self, pageIndex, pageUrl, contentListTag, driver) :
        self.pageIndex = pageIndex
        self.pageUrl = pageUrl
        self.contentListTag = contentListTag
        self.driver = driver

        self.contents = []

    def getContents(self):
        if len(self.contents) == 0 :
            self.createContentList()
        
        return self.contents

    def createContentList(self):
         # 該当ページへ遷移
        self.driver.get(self.pageUrl)
        time.sleep(1)

        for listTag in self.getContentListTags() :
            self.driver.implicitly_wait(20)
            aTag = listTag.find_element(by=By.TAG_NAME, value="a")
            self.contents.append({
                "href":aTag.get_attribute('href'),
                "title":aTag.text,
                "pageIndex": self.pageIndex
            })

    def getContentListTags(self) :
        return self.contentListTag.getContentListTags()
    
    