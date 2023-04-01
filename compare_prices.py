import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    html1 = requests.get(product_laughs).content
    
    soup1 = BeautifulSoup(html1, 'html.parser')
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    class_name = "price"
    price_text = soup1.find_all(class_=class_name)
    mylist = []
    for element in price_text:
        price = element.text
        mylist.append(float(price.replace('Rs.', '')))
    price_laughs = mylist[1]
    product_name_laughs = soup1.find('h1').text

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    response = requests.get(product_glomark)
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', {'type': 'application/ld+json'})
    inline_script_data = script_tag.string.strip()
    data_dict = json.loads(inline_script_data)
    price_glomark = float(data_dict['offers'][0]['price'])
    product_name_glomark = soup.find('h1').text
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')