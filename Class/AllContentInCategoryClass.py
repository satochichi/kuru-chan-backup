
from selenium import webdriver
from selenium.webdriver.common.by import By
from Class.ContentListClass import ContentListClass
import time

class AllContentInCategoryClass : 
    driver :webdriver

    def __init__(self, pageLink, contentListTag, capture, driver) :
        self.pageLink = pageLink
        self.contentListTag = contentListTag
        self.capture = capture
        self.driver = driver
        self.pageContents = []

    def accessPageAndGetContent(self):
        for pageLink in self.pageLinks : 
            contentList = ContentListClass(
                pageLink["pageIndex"], 
                pageLink["href"], 
                self.contentListTag,
                self.driver
            )
            print(pageLink["href"])
            self.pageContents.append(contentList.getContents())

    def capture(self):
         for contents in self.pageContents:
            for i, content in enumerate(contents):
                self.driver.get(content['href'])
                time.sleep(1)
                title = str(self.paging.getMaxContentCount() *
                            content['pageIndex'] + i) + "_" + content['title']
                self.capture.saveCapture(title)
                print(i)


    
    