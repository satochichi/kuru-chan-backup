
class Paging:
    domain = "https://kuru-chan.com"

    def __init__(self, pagePath, maxPageCount, maxContentCount) -> None:
        self.pagePath = pagePath
        self.maxPageCount = maxPageCount
        self.maxContentCount = maxContentCount

    def getPageLinks(self):
        pageLinks = []
        for i in range(self.maxPageCount):
            pageLinks.append({
                "pageIndex": i,
                "href": self.domain + "/" + self.pagePath + str(i + 1)
            })
        return pageLinks
    
    def getMaxContentCount(self):
        return self.maxContentCount
