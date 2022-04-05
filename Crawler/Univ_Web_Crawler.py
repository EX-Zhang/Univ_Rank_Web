from Crawler import Crawler

class Univ_Web_Crawler(Crawler):

    def __init__(self,url,**paras):

       Crawler.__init__(self,url,paras)

       self.__Websites = []

       self.getWebsites()

    def getWebsites(self):

        if self._Soup == None:
            return

        results = []

        ps = self._Soup.find_all('p',attrs = {'align':'center'})

        for p in ps:

            results.extend(self._Data_from_Soup(p.children))

        for result in results:

            if result.name == 'a' and str.isdigit(result.string) and int(result.string) in range(1,13):

                self.__Websites.append(result.attrs['href'])

    def getData(self):
        return self.__Websites

    def printData(self):
        for website in self.__Websites:
            print(website)
