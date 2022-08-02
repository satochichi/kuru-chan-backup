
from copyreg import constructor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Class.Capture import Capture
from Class.Paging import Paging
from Class.ContentListClass import ContentListClass
from Class.ContentGalleryListTag import ContentGalleryListTag
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

maxPageCount =22
maxContentCount = 24
paging = Paging("blog/category/gallery/page/", maxPageCount, maxContentCount)
pageLinks = paging.getPageLinks()
capture = Capture("gallery", driver)
contentListTag = ContentGalleryListTag(driver)
print(pageLinks)

# 各ページのコンテンツリストを作成
pageContents = []
for pageLink in pageLinks : 
    contentList = ContentListClass(
        pageLink["pageIndex"], 
        pageLink["href"], 
        contentListTag,
        driver
    )
    print(pageLink["href"])
    pageContents.append(contentList.getContents())


# 全コンテンツへアクセスし、キャプチャを取る
for contents in pageContents : 
    for i,content in enumerate(contents) :
        driver.get(content['href'])
        time.sleep(1)
        title = str(paging.getMaxContentCount() * content['pageIndex'] + i) + "_" + content['title']
        capture.saveCapture(title)
        print(i)

driver.quit()