
from copyreg import constructor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Class.Capture import Capture
from Class.ContentListClass import ContentListClass
from Class.ContentStaffChannelListTag import ContentStaffChannelListTag
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

capture = Capture("kuruPress", driver)
contentListTag = ContentStaffChannelListTag(driver)

pageLinks = [
    {"href":"https://kuru-chan.com/kuru2press/2021/04/","pageIndex":0},
    {"href":"https://kuru-chan.com/kuru2press/2021/03/","pageIndex":1}
    # {"href":"https://kuru-chan.com/kuru2press/2021/02/","pageIndex":2},
    # {"href":"https://kuru-chan.com/kuru2press/2020/12/","pageIndex":3},
    # {"href":"https://kuru-chan.com/kuru2press/2020/11/","pageIndex":4},
    # {"href":"https://kuru-chan.com/kuru2press/2020/10/","pageIndex":5},
    # {"href":"https://kuru-chan.com/kuru2press/2020/09/","pageIndex":6},
    # {"href":"https://kuru-chan.com/kuru2press/2020/08/","pageIndex":7},
    # {"href":"https://kuru-chan.com/kuru2press/2020/07/","pageIndex":8},
    # {"href":"https://kuru-chan.com/kuru2press/2020/06/","pageIndex":9},
    # {"href":"https://kuru-chan.com/kuru2press/2020/04/","pageIndex":10},
    # {"href":"https://kuru-chan.com/kuru2press/2020/03/","pageIndex":11},
    # {"href":"https://kuru-chan.com/kuru2press/2020/02/","pageIndex":12},
    # {"href":"https://kuru-chan.com/kuru2press/2020/01/","pageIndex":13},
    # {"href":"https://kuru-chan.com/kuru2press/2019/11/","pageIndex":14},
    # {"href":"https://kuru-chan.com/kuru2press/2019/10/","pageIndex":15},
    # {"href":"https://kuru-chan.com/kuru2press/2019/08/","pageIndex":16},
    # {"href":"https://kuru-chan.com/kuru2press/2019/07/","pageIndex":17},
    # {"href":"https://kuru-chan.com/kuru2press/2019/06/","pageIndex":18},
    # {"href":"https://kuru-chan.com/kuru2press/2019/05/","pageIndex":19},
    # {"href":"https://kuru-chan.com/kuru2press/2019/04/","pageIndex":20},
    # {"href":"https://kuru-chan.com/kuru2press/2019/03/","pageIndex":21},
    # {"href":"https://kuru-chan.com/kuru2press/2019/02/","pageIndex":22},
    # {"href":"https://kuru-chan.com/kuru2press/2019/01/","pageIndex":23},
    # {"href":"https://kuru-chan.com/kuru2press/2018/12/","pageIndex":24},
    # {"href":"https://kuru-chan.com/kuru2press/2018/11/","pageIndex":25},
    # {"href":"https://kuru-chan.com/kuru2press/2018/10/","pageIndex":26},
    # {"href":"https://kuru-chan.com/kuru2press/2018/08/","pageIndex":27},
    # {"href":"https://kuru-chan.com/kuru2press/2018/07/","pageIndex":28},
    # {"href":"https://kuru-chan.com/kuru2press/2018/06/","pageIndex":29},
    # {"href":"https://kuru-chan.com/kuru2press/2018/05/","pageIndex":30},
    # {"href":"https://kuru-chan.com/kuru2press/2018/04/","pageIndex":31},
    # {"href":"https://kuru-chan.com/kuru2press/2018/03/","pageIndex":32},
    # {"href":"https://kuru-chan.com/kuru2press/2018/02/","pageIndex":33},
    # {"href":"https://kuru-chan.com/kuru2press/2018/01/","pageIndex":34},
    # {"href":"https://kuru-chan.com/kuru2press/2017/12/","pageIndex":35},
    # {"href":"https://kuru-chan.com/kuru2press/2017/11/","pageIndex":36},
    # {"href":"https://kuru-chan.com/kuru2press/2017/09/","pageIndex":37},
    # {"href":"https://kuru-chan.com/kuru2press/2017/08/","pageIndex":38},
    # {"href":"https://kuru-chan.com/kuru2press/2017/07/","pageIndex":39},
    # {"href":"https://kuru-chan.com/kuru2press/2017/06/","pageIndex":40},
    # {"href":"https://kuru-chan.com/kuru2press/2017/05/","pageIndex":41},
    # {"href":"https://kuru-chan.com/kuru2press/2017/04/","pageIndex":42},
    # {"href":"https://kuru-chan.com/kuru2press/2017/03/","pageIndex":43},
    # {"href":"https://kuru-chan.com/kuru2press/2016/12/","pageIndex":44},
    # {"href":"https://kuru-chan.com/kuru2press/2016/11/","pageIndex":45},
    # {"href":"https://kuru-chan.com/kuru2press/2016/10/","pageIndex":46},
    # {"href":"https://kuru-chan.com/kuru2press/2016/09/","pageIndex":47},
    # {"href":"https://kuru-chan.com/kuru2press/2016/08/","pageIndex":48},
    # {"href":"https://kuru-chan.com/kuru2press/2016/07/","pageIndex":49},
    # {"href":"https://kuru-chan.com/kuru2press/2016/06/","pageIndex":50},
    # {"href":"https://kuru-chan.com/kuru2press/2016/05/","pageIndex":51},
    # {"href":"https://kuru-chan.com/kuru2press/2016/04/","pageIndex":52},
    # {"href":"https://kuru-chan.com/kuru2press/2016/03/","pageIndex":53},
    # {"href":"https://kuru-chan.com/kuru2press/2016/02/","pageIndex":54},
    # {"href":"https://kuru-chan.com/kuru2press/2015/12/","pageIndex":55},
    # {"href":"https://kuru-chan.com/kuru2press/2015/11/","pageIndex":56},
    # {"href":"https://kuru-chan.com/kuru2press/2015/10/","pageIndex":57},
    # {"href":"https://kuru-chan.com/kuru2press/2015/08/","pageIndex":58},
    # {"href":"https://kuru-chan.com/kuru2press/2015/07/","pageIndex":59},
    # {"href":"https://kuru-chan.com/kuru2press/2015/06/","pageIndex":60},
    # {"href":"https://kuru-chan.com/kuru2press/2015/05/","pageIndex":61},
    # {"href":"https://kuru-chan.com/kuru2press/2015/04/","pageIndex":62},
    # {"href":"https://kuru-chan.com/kuru2press/2015/03/","pageIndex":63},
    # {"href":"https://kuru-chan.com/kuru2press/2015/02/","pageIndex":64},
    # {"href":"https://kuru-chan.com/kuru2press/2015/01/","pageIndex":65},
    # {"href":"https://kuru-chan.com/kuru2press/2014/12/","pageIndex":66},
    # {"href":"https://kuru-chan.com/kuru2press/2014/11/","pageIndex":67},
    # {"href":"https://kuru-chan.com/kuru2press/2014/10/","pageIndex":68},
    # {"href":"https://kuru-chan.com/kuru2press/2014/09/","pageIndex":69},
    # {"href":"https://kuru-chan.com/kuru2press/2014/08/","pageIndex":70},
    # {"href":"https://kuru-chan.com/kuru2press/2014/01/","pageIndex":71},
    # {"href":"https://kuru-chan.com/kuru2press/2013/12/","pageIndex":72},
    # {"href":"https://kuru-chan.com/kuru2press/2013/06/","pageIndex":73},
    # {"href":"https://kuru-chan.com/kuru2press/2013/05/","pageIndex":74},
    # {"href":"https://kuru-chan.com/kuru2press/2012/05/","pageIndex":75}
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