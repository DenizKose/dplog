import csv
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Selenium settings

service = Service('/usr/local/bin/chromedriver')
options = Options()
options.headless = False
browser = webdriver.Chrome(service=service, options=options)

# Scrapping settings

product_url = 'https://www.detmir.ru/product/index/id/'
msk = 'RU-MOW'
spb = 'RU-SPE'
city = spb  # Moscow and region - msk (default), Saint P. and region - spb


def city_name():
    if city == msk:
        name = 'Moscow and region'
    else:
        name = 'Saint Petersburg and region'
    return name


file_name = f'Lego ({city_name()}).csv'

# Create csv file

with open(f'{file_name}', mode='w', encoding='utf-8') as csv_file:
    file = csv.writer(csv_file, delimiter=',')
    file.writerow(['id', 'title', 'price', 'promo_price', 'url'])


def link(lim, off):
    url = f'https://api.detmir.ru/v2/products?filter=categories[].alias:lego;promo:false;withregion:{city}&expand' \
          f'=meta.facet.ages.adults,meta.facet.gender.adults&meta=*&limit={lim}&offset={off}&sort=popularity:desc '
    return url


step = 0
i = 0
more = True
while more:
    browser.get(link(30, step))
    json_data = browser.find_element(By.XPATH, '/html/body/pre')
    result = json.loads(json_data.text)
    with open(f'{file_name}', mode='a', encoding='utf-8') as csv_file:
        file = csv.writer(csv_file, delimiter=',')
        for product in result['items']:
            i += 1
            print(str(i) + ' ' + str(product['id']))
            product_id = product['id']
            title = product['title']
            price = product['price']['price']
            product_link = product_url + product['id']
            try:
                old_price = product['old_price']['price']
            except TypeError:
                old_price = price
                price = ''
            file.writerow([product_id, title, old_price, price, product_link])
    if len(result['items']) == 0:
        more = False
        browser.close()
    step += 30
    time.sleep(2)

