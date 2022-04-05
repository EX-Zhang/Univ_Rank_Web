
class Univ:

    def __init__(self,data):

        self.__data = data

        self.__Rank = data[0].string
        self.__Name = data[1].string
        self.__Score = data[3].string

    def Get_Univ_Data(self):

        return self.__data

    def Get_Univ_String(self):

        return "{:^10}\t{:^6}\t{:^10}".format(self.__Rank,self.__Name,self.__Score)
