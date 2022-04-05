
import abc

import requests
from bs4 import BeautifulSoup
import bs4

class Crawler(metaclass = abc.ABCMeta):

    def __init__(self,URL,paras):

        self._URL = URL

        self._HTML = None

        self._Soup = None

        self._HTML = self.getHTML(self.__setHeaders(paras))

        self._Soup = self.getSoup(self.__setParser(paras))

    def getHTML(self,headers):

        if self._HTML != None:
            return self._HTML
        
        try:
            request = requests.get(self._URL,timeout=headers['timeout'],headers=headers['header'])
            
            request.raise_for_status()
            
            request.encoding = request.apparent_encoding
            
            return request
            
        except:
            return None

    def getSoup(self,parser):

        if self._HTML == None:
            return None

        if self._Soup != None:
            return self._Soup

        return BeautifulSoup(self._HTML.text,parser)

    def _Data_from_Soup(self,datas):

        results = []

        for data in datas:

            if isinstance(data,bs4.element.Tag):

                results.append(data)

        return results

    def __setHeaders(self,paras):
        headers = {'header':{'user-agent': 'Chrome'},'timeout':30}

        if 'header' in paras:
            headers['header'] = paras['header']

        if 'timeout' in paras:
            headers['timeout'] = paras['timeout']

        return headers

    def __setParser(self,paras):
        if 'parser' not in paras:
            return "html.parser"
        return paras['parser']

    @abc.abstractmethod
    def getData(self): pass

    @abc.abstractmethod
    def printData(self): pass
