#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
from bs4 import BeautifulSoup
url = "https://www.tradingview.com/markets/currencies/ideas/?sort=recent"
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.content,"html.parser")
result = soup.find_all("div",attrs={"class" : "tv-feed__item tv-feed-layout__card-item"})
x=1
for item in result:
    print(x , " :")

    Symbol = item.find("a",attrs={"tv-widget-idea__symbol apply-overflow-tooltip"})
    print("Sympol : ", Symbol.text)
       
    timeframe = item.find_all("span",attrs={"tv-widget-idea__timeframe"})
    timeframe2 = str(timeframe)
    result_time = re.findall(r"\w*</span>]$",timeframe2)
    result_time=re.sub("</span>]","",str(result_time))
    print("TimeFrame : " ,result_time)    
    
    order = item.find_all("div",attrs={"tv-widget-idea__info-row"})
    order2 = str(item)

    Order_Buy = re.findall(r"Long",order2)
    Order_Sell = re.findall(r"Short",order2)
    #print(Order_Sell)
    for item2 in Order_Buy:
        print("Order_Type : ", item2)
        break
        
    for item2 in Order_Sell:
        print("Order_Type : ", item2)
        break                
        
    print("----------------")
    x=x+1


# In[ ]:




