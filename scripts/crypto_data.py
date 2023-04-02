import http.client
import json
import csv
import urllib3
import os
import pandas as pd
import numpy as np
import datetime
import time as t
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


SIZE=1
PAGE=3

#___________________________________________________GET SLUGS BY MARKETCAP DESCENDING_____________________________________

def getAllSlugs():

    # initialize slugs array

    slugs = []


    for page in range(0, PAGE):
        t.sleep(0.51)

        #size= option anywhere between 1 and 100

        http = urllib3.PoolManager()
        url = 'https://data.block.cc/api/v3/symbols?size=' + str(SIZE) + '&page=' + str(page)
        resp = http.request('GET', url, headers={
            'X-api-key': API_KEY
        })
                
        print(resp.status)

        jason = resp.data.decode('utf-8')

        data = json.loads(jason)

        for slug in data:

            slugs.append(slug['slug'])

    return slugs



#___________________________________________________GET SINGLE COIN TIMESTAMP AND PRICE_____________________________________


def getCoinData(slug_id: str, start: str, end: str, interval: str):


    http = urllib3.PoolManager()
    url = 'https://data.block.cc/api/v3/price/history' +'?slug=' + slug_id + '&start=' + start + '&end=' + end + '&interval=' + interval
    resp = http.request('GET', url, headers={
        'X-api-key': API_KEY
    })
            
    # print(resp.status)

    jason = resp.data.decode('utf-8')

    data = json.loads(jason)

    # pull time convert 13-bit unix timestamp to year-month-date
    
    time = [ datetime.datetime.utcfromtimestamp(time['T']/1000).strftime("%Y-%m-%d") for time in data ]

    # pull price (USD) 


    price = [ price['u'] for price in data ]


    return time, price

#___________________________________________________GET MANY COINS PUSHED INTO A DF_____________________________________

def many_coins(coins: list):

    # 13 bit unix time stamp for different years

    # #2019
    # year_2019_start = '1546232400000'
    # year_2019_end = '1577682000000'
    
    # #2020
    # year_2020_start = '1577768400000'
    # year_2020_end = '1609304400000'

    # #2021
    # year_2021_start = '1609390800000'
    # year_2021_end = '1640840400000'

    # #2022
    # year_2022_start = '1640926800000'
    # year_2022_end = '1672376400000'

    # #2023
    # year_2023_start = '1672462800000'
    # year_2023_end = '1703912400000'

    # interval
    potential_intervals = ['5m','15m','30m','1h','2h','6h','12h','1d','2d']


    combined_start = ['1546232400000', '1577768400000', '1609390800000', '1640926800000', '1672462800000']

    combined_end = ['1577682000000', '1609304400000', '1640840400000', '1672376400000', '1703912400000']




     # initialize dataframe with bitcoin

    df = pd.DataFrame()

    coin_ini = 'bitcoin'

    for i in range(len(combined_start)):
        t.sleep(0.51)
        df2 = pd.DataFrame()

        tnp = getCoinData(coin_ini, combined_start[i], combined_end[i], potential_intervals[7])

        timestamp = tnp[0]
        price = tnp[1]

        df2['timestamp'] = timestamp
        df2[coin_ini +'_price'] = price

        df = pd.concat([df, df2], ignore_index=True)



    # list of all coins being pushed into df

    coins = coins

    
    # loop through coins and append to dataframe



    for coin in coins:

        if(coin != 'bitcoin'):
            
            df3 = pd.DataFrame()

            for i in range(len(combined_start)):
                t.sleep(0.51)
                df4= pd.DataFrame()

                tnp = getCoinData(coin, combined_start[i], combined_end[i], potential_intervals[7])

                timestamp = tnp[0]
                price = tnp[1]

                df4['timestamp'] = timestamp
                df4['timestamp'] =df4['timestamp'].astype(object)
                df4[coin +'_price'] = price


                df3 = pd.concat([df3, df4], ignore_index=True)

    

            df5 = df.merge(df3, how='left', left_on='timestamp', right_on='timestamp')
            df = df5

    return df


if __name__ == "__main__":


    # get coin list -

    slugs = getAllSlugs()


#     # append new coin to the dataframe____________________________________________________
    
    

    final_df = many_coins(slugs)

    print("done")
    final_df.to_csv('crypto_data.csv', index = False)




   



    
   
