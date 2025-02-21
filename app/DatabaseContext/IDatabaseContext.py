from abc import ABC, abstractmethod

class IDatabaseContext(ABC):
    @abstractmethod
    def GetNewsById(self, news_id):
        pass

    @abstractmethod
    def GetNewsByUrl(self, url):
        pass

    @abstractmethod
    def SaveNews(self, news_object):
        pass
