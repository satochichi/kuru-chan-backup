from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def saveCapture(title):
    #縦と横のサイズを取得してキャプチャを取得する   
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')        
    driver.set_window_size(page_width, page_height)

    filename = title + ".png"

    #キャプチャの取得
    driver.save_screenshot(filename)

    print(filename)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# driver.get("https://kuru-chan.com/0565hjazz/2021/04/18/383/")
# title = "4_4/25東久留米JAZZフェスティバル開催間近です！【東久留米からジャズを 実行委員会】"

# driver.get("https://kuru-chan.com/what/")
# title = "東久留米ってどんなまち？"

# driver.get("https://kuru-chan.com/guideline/")
# title = "はじめての方へ"

# driver.get("https://kuru-chan.com/terms/")
# title = "利用規約"

# driver.get("https://kuru-chan.com/privacy/")
# title = "個人情報保護方針"

driver.get("https://kuru-chan.com/0565hjazz/2021/04/18/383/")
title = "4/25東久留米JAZZフェスティバル開催間近です！"

time.sleep(3)
saveCapture(title)