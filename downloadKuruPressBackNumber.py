import os
import urllib.parse
from copyreg import constructor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Class.Capture import Capture
from Class.ContentListClass import ContentListClass
from Class.ContentKuruPressDownloadTag import ContentKuruPressDownloadTag
import time

downloadDir = '/Users/satoshiaoki/works/kurukuru/kuru-chan-backup/download'
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": downloadDir,
    "plugins.always_open_pdf_externally": True
})
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

capture = Capture("kuruPress", driver)
contentListTag = ContentKuruPressDownloadTag(driver)

pageLinks = [
    {"href":"https://kuru-chan.com/kuru2press/2014/08/04/%e3%83%90%e3%83%83%e3%82%af%e3%83%8a%e3%83%b3%e3%83%90%e3%83%bc16/","pageIndex":0},
    # {"href":"https://kuru-chan.com/kuru2press/2014/08/","pageIndex":0},
    # {"href":"https://kuru-chan.com/kuru2press/2014/01/","pageIndex":1},
    # {"href":"https://kuru-chan.com/kuru2press/2013/12/","pageIndex":2},
    # {"href":"https://kuru-chan.com/kuru2press/2013/06/","pageIndex":3},
    # {"href":"https://kuru-chan.com/kuru2press/2013/05/","pageIndex":4},
    # {"href":"https://kuru-chan.com/kuru2press/2012/05/","pageIndex":5}
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

print('pageContents',pageContents)

# 全コンテンツへアクセスし、キャプチャを取る
count = 0
for contents in pageContents : 
    for i,content in enumerate(contents) :
        driver.get(content['href'])
        time.sleep(2)
        oldname = urllib.parse.unquote(os.path.basename(content['href']))
        newfilename = str(count) + "_" + content['title'] + '.pdf'
        os.rename(downloadDir + '/' + oldname, downloadDir + '/' + newfilename)
        count+=1

driver.quit()