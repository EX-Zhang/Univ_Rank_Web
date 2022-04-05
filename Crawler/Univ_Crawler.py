from Crawler import Crawler
from Univ import Univ

class Univ_Crawler(Crawler):

    def __init__(self,url,**paras):

        self.__Univs = []

        Crawler.__init__(self,url,paras)

        self.get_Univ_Info()

    def get_Univ_Info(self):

        if self._Soup == None:
            return

        results = self._Data_from_Soup(self._Soup.find('tbody').findChildren('tr'))
        
        for result in results:

            self.__Univs.append(Univ(result('td')))

    def getData(self):
        return self.__Univs
    
    def printData(self):
        print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "综合得分"))

        for univ in self.__Univs:
            
            print(univ.Get_Univ_String())

