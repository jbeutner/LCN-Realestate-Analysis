import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

def fetch():

    #Headers will vary depending on browser/computer/OS
    headers = {
        'accept': '',
        'accept-encoding': '',
        'accept-language': '',
        'cache-control': '',
        'cookie': '',
        'sec-ch-ua': '',
        'sec-ch-ua-mobile': '',
        'sec-ch-ua-platform': '',
        'sec-fetch-dest': '',
        'sec-fetch-mode': '',
        'sec-fetch-site': '',
        'sec-fetch-user': '',
        'upgrade-insecure-requests': '',
        'user-agent': ''
        }

    listings = []

    #Insert list of zip codes to search here
    zip_code_list = ['68336','68430','68502','68503','68504','68505','68506','68507','68508',
                     '68510','68512','68514','68516','68517','68520','68521','68522','68523',
                     '68524','68526','68528','68531']

    #Insert base URL here
    url = 'https://www.zillow.com/lincoln-ne-'

    #Iterates over list of zip codes in zip code list
    for zip_code in zip_code_list:

        #Iterates over the maximum number of pages returned by a search on the site being scraped
        for p in range(1,11):
            soup = BeautifulSoup(requests.get(url+zip_code+'/sold/'+str(p)+'_p', headers=headers).content,'html.parser')
            data = json.loads(soup.select_one('script[data-zrr-shared-data-key]').contents[0].strip('!<>-'))

            for result in data['cat1']['searchResults']['listResults']:
                listings.append(result)

            time.sleep(5)
            sold_df = pd.DataFrame(listings)
            sold_df = sold_df[['id','unformattedPrice','addressZipcode','beds','baths','area','latLong']]

    #Create latitude and longitude columns
    sold_df['latLong'] = sold_df['latLong'].apply(str)
    sold_df[['latitude','longitude']] = sold_df['latLong'].str.split(',',expand=True)
    sold_df['latitude'] = sold_df['latitude'].str.strip("{'latitude': ")
    sold_df['longitude'] = sold_df['longitude'].str.strip("'longitude': ")
    sold_df['longitude'] = sold_df['longitude'].str.strip("}")
    sold_df.drop(columns=['latLong'],inplace=True)

    #Change column names
    sold_df.columns = ['id','sold_price','zipcode','beds','baths','area','latitude','longitude']

    #Export to excel
    sold_df.to_excel('lincoln_sold.xlsx')

    return sold_df
fetch()
