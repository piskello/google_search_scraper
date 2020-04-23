import requests
import csv
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import timedelta
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

#Definisco i dati pr la ricerca
ricerca="+paura +coronavirus"
startDate = date(2020, 2, 1)
endDate = date(2020, 4, 22)

#coversione per la query di ricerca
deltaDate=endDate-startDate

print("--------------------\nQuery: " + ricerca)
print("From: " + startDate.strftime("%d/%m/%Y")+" to: "+endDate.strftime("%d/%m/%Y")+"\n--------------------")

for i in range(deltaDate.days+1):
    #compongo query di ricerca
  
    qHeader="https://www.google.com/search?q="
    qText=ricerca.replace("'","%22").replace("+","%2B").replace(" ","+")
    qTimestamp="&safe=active&sxsrf=ALeKk02GfGyt6J2O2C16qAgaIQHUaTO2tw%3A1587473771795"
    qSource="&source=lnt&start=10"
    qTimeSpan="&tbs=cdr%3A1%2C"
    qStartDate="%2Ccd_min%3A"+startDate.strftime("%m/%d/%Y").replace("/","%2F")
    qEndDate="%2Ccd_max%3A"+ startDate.strftime("%m/%d/%Y").replace("/","%2F")
    qNews="&tbm=nws"
    #query finale
    URL=qHeader+qText+qTimestamp+qSource+qTimeSpan+qStartDate+qEndDate+qNews
    result = requests.get(URL, headers=headers)    
    soup = BeautifulSoup(result.content, 'html.parser')
    total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False) 
    results_num = ''.join([num for num in total_results_text if num.isdigit()])
    print(startDate.strftime("%d/%m/%Y")+ " " +results_num)
#    print (result.content)
    print(URL)
    time.sleep(30)
    startDate+=timedelta(1)
    
