
class PageLink:
    domain = "https://kuru-chan.com"

    def __init__(self, pagePath, pageCount) -> None:
        self.pagePath = pagePath
        self.pageCount = pageCount

    def getPageLinks(self):
        pageLinks = []
        for i in range(self.pageCount):
            pageLinks.append({
                "pageIndex": i,
                "href": self.domain + "/" + self.pagePath + str(i + 1)
            })
        return pageLinks
