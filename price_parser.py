import urllib
from bs4 import BeautifulSoup
import re
import requests


# from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException

# 4820001313581  рафаелло
# 4820001313581 кетчуп
# 4820000455732  львівське пиво
# 4820017000055 моршинська
# 4820073561774 грін дей
# 4820045701665 молоко

def tmp_geting_data(product_bar_code='4820045701665'):
    fozzyUrl = 'https://fozzy.zakaz.ua/ru/?q=0'
    novusUrl = 'https://novus.zakaz.ua/ru/?q=0'
    furshetUrl = 'https://efurshet.com/search?q='

    product_name = ''

    tmp_list = []
    shops = {"Novus": novusUrl, 'Fozzy': fozzyUrl, "Furshet": furshetUrl}

    for shop_name, shop_url in shops.items():
        tmp_dict = {}
        if shop_name == "Novus" or shop_name == "Fozzy":
            try:
                response = urllib.request.urlopen(shop_url + str(product_bar_code))
                soup = BeautifulSoup(response, "html.parser")
                div_product = soup.find('button', class_='btn btn-mini product-add-to-cart-button')
                span_product_price = div_product.find('span', class_='one-product-price')
                span_product_grivna_price = span_product_price.find('span', class_='grivna price').string
                span_product_kopeiki_price = span_product_price.find('span', class_='kopeiki').string
                product_price = span_product_grivna_price + '.' + span_product_kopeiki_price
                tmp_dict['name'] = shop_name
                tmp_dict['price'] = product_price
                if product_price == 'немає в наявності':
                    product_name = 'Продукт не знайдено'
                else:
                    product_name = soup.find('div', class_='one-product-name').string
            except:
                tmp_dict['name'] = shop_name
                tmp_dict['price'] = 'немає в наявності'
            # except NoSuchElementException:
            #     pass
        # print(tmp_list)
        if shop_name =="Furshet":
            try:
                response = urllib.request.urlopen(shop_url + str(product_bar_code))
                soup = BeautifulSoup(response, 'html.parser')
                product_price = soup.find('span', class_='sal').text
                tmp_dict['name'] = shop_name
                tmp_dict['price'] = product_price[:-4]
            except:
                tmp_dict['name'] = shop_name
                tmp_dict['price'] = 'немає в наявності'
        tmp_list.append(tmp_dict)

    context = {
        'product_name': product_name,
        'price_list': tmp_list
    }
    return(context)

# if __name__ == '__main__':
# print("ddqwd")
# ttt = tmp_geting_data('4820017000024')
# print(ttt)