
class Capture:

    def __init__(self, directory,driver ) -> None:
        self.directory = directory
        self.driver = driver

    def saveCapture(self , title):
        # 縦と横のサイズを取得してキャプチャを取得する
        page_width = self.driver.execute_script('return document.body.scrollWidth')
        page_height = self.driver.execute_script('return document.body.scrollHeight')
        self.driver.set_window_size(page_width, page_height)

        filename = title + ".png"

        # キャプチャの取得
        self.driver.save_screenshot("./capture/" + self.directory + "/" + filename)
