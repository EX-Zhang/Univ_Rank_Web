
import mysql.connector as MySQL

from Univ_Crawler import Univ_Crawler
from Univ_Web_Crawler import Univ_Web_Crawler

def main():
    
    url = 'https://www.university-list.net/paiming/dx-160001.html'

    uwc = Univ_Web_Crawler(url)

    websites = uwc.getData()

    univs = []

    for website in websites:

        uc = Univ_Crawler('https://www.university-list.net/paiming/'+website)
    
        univs.extend(uc.getData())

    db = MySQL.connect(

        host = "localhost",
        user = "Univ",
        passwd = "UnivTest",
        database = "univrank"
        
    )

    cursor = db.cursor()

    for i in range(len(univs)):

        univ = univs[i]

        univ_data = univ.Get_Univ_Data()

        sql = "insert into Univ_Rank values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        val = [str(i),]

        for data in univ_data:

            val.append(data.string)

        cursor.execute(sql,val)

    db.commit()
    
main()
