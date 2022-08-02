from abc import ABCMeta, abstractmethod

class ContentListTag(metaclass=ABCMeta):
    @abstractmethod
    def getContentListTags(self):
        pass