
from copyreg import constructor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Class.Capture import Capture
from Class.Paging import Paging
from Class.ContentListClass import ContentListClass
from Class.ContentStaffChannelListTag import ContentStaffChannelListTag
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

capture = Capture("staffChannel", driver)
contentListTag = ContentStaffChannelListTag(driver)

pageLinks = [
    {"href":"https://kuru-chan.com/staff-channel/2017/01/","pageIndex":0},
    {"href":"https://kuru-chan.com/staff-channel/2016/04/","pageIndex":1},
    {"href":"https://kuru-chan.com/staff-channel/2015/06/","pageIndex":2},
    {"href":"https://kuru-chan.com/staff-channel/2014/06/","pageIndex":3},
    {"href":"https://kuru-chan.com/staff-channel/2014/05/","pageIndex":4},
    {"href":"https://kuru-chan.com/staff-channel/2014/02/","pageIndex":5},
    {"href":"https://kuru-chan.com/staff-channel/2013/10/","pageIndex":6},
    {"href":"https://kuru-chan.com/staff-channel/2013/09/","pageIndex":7},
    {"href":"https://kuru-chan.com/staff-channel/2013/08/","pageIndex":8},
    {"href":"https://kuru-chan.com/staff-channel/2013/07/","pageIndex":9},
    {"href":"https://kuru-chan.com/staff-channel/2013/06/","pageIndex":10},
    {"href":"https://kuru-chan.com/staff-channel/2013/05/","pageIndex":11},
    {"href":"https://kuru-chan.com/staff-channel/2013/04/","pageIndex":12},
    {"href":"https://kuru-chan.com/staff-channel/2013/03/","pageIndex":13},
    {"href":"https://kuru-chan.com/staff-channel/2012/01/","pageIndex":14}
]

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
count = 0
for contents in pageContents : 
    for i,content in enumerate(contents) :
        driver.get(content['href'])
        time.sleep(1)
        title = str(count) + "_" + content['title']
        capture.saveCapture(title)
        count+=1

driver.quit()