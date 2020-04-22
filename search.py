import requests
import csv
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import timedelta

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

#Definisco i dati pr la ricerca
ricerca="'paura' covid coronavirus"
startDate = date(2020, 4, 2)
endDate = date(2020, 4, 2) #5520

#coversione per la query di ricerca
deltaDate=endDate-startDate

print("--------------------\nQuery: " + ricerca)
print("From: " + startDate.strftime("%d/%m/%Y")+" to: "+endDate.strftime("%d/%m/%Y")+"\n--------------------")
print(deltaDate.days)
 
for i in range(deltaDate.days+1):
    
    #moduli query di ricerca
    qHeader="https://www.google.com/search?q="
    qText=ricerca.replace("'","%22").replace(" ","+")
    qTimestamp="&safe=active&sxsrf=ALeKk02GfGyt6J2O2C16qAgaIQHUaTO2tw%3A1587473771795"
    qSource="&source=lnt"
    qTimeSpan="&tbs=cdr%3A1%2C%2C"
    qStartDate="cd_min%3A"+ startDate.strftime("%d/%m/%Y").replace("/","%2F")+"%2C"
    qEndDate="cd_max%3A"+ startDate.strftime("%d/%m/%Y").replace("/","%2F")
    qNews="&tbm=nws"

    #query finale
    URL=qHeader+qText+qTimestamp+qSource+qTimeSpan+qStartDate+qEndDate+qNews
    #print(URL)
    result = requests.get(URL, headers=headers)    
    soup = BeautifulSoup(result.content, 'html.parser')
    total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False)
    results_num = ''.join([num for num in total_results_text if num.isdigit()])
    print(startDate.strftime("%d/%m/%Y")+ " " +results_num)
    
    startDate+=timedelta(1)

