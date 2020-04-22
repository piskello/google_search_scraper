import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
URL     = "https://www.google.com/search?safe=active&biw=1680&bih=916&tbs=cdr%3A1%2Ccd_min%3A3%2F3%2F2020%2Ccd_max%3A3%2F3%2F2020&tbm=nws&sxsrf=ALeKk02j1D7vNjvChlA8BfEzi4ZeOFBphQ%3A1587542275898&ei=A_mfXu62Nsfh6ASyzq2ADQ&q=%22paura%22+covid+corona&oq=%22paura%22+covid+corona&gs_l=psy-ab.3...5571.9804.0.10402.20.20.0.0.0.0.197.1961.2j15.17.0....0...1c.1.64.psy-ab..3.4.440...0i19k1.0.8IS8rDhGIXM"
result = requests.get(URL, headers=headers)    

soup = BeautifulSoup(result.content, 'html.parser')

total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False) # this will give you the outer text which is like 'About 1,410,000,000 results'
results_num = ''.join([num for num in total_results_text if num.isdigit()]) # now will clean it up and remove all the characters that are not a number .
print(results_num)

