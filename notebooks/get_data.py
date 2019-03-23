import requests
import json
# import matplotlib.pyplot as plt
import pandas as pd
import xmltodict
# import gmaps
from pprint import pprint
#importing keys
# from api_keys import zillow_key
# from api_keys import gkey
import time

df = pd.read_csv('County_Adds.csv')
df = df[['zip', 'address', 'lat', 'lng', 'County']]
df['taxAssessment'] = ''
df['lot sq/ft'] = ''
df['finished sq/ft'] = ''
df['price low'] = ''
df['price high'] = ''
df['zestimate'] = ''

url = "https://www.zillow.com/webservice/GetDeepSearchResults.htm?"
params = {
    'zws-id': 'X1-ZWz181cgn4m5fv_9myga',
    'address': '3235 AVENUE G, PATTISON, TX 77466',
    'citystatezip':'77466'
}
start = time.time()
for i in range(100):
    
    params['address'] = df.iloc[i, 1]
    params['citystatezip'] = df.iloc[i, 0]
    
    response = requests.get(url, params)
    response_result = xmltodict.parse(response.text)
    
    #checks if response is a 200 type or not
    if response.status_code != 200:
        print('response error')
        continue
    try:
        print(f"{i}, {df.iloc[i, 1]}")
        df.iat[i, 5] = response_result[('SearchResults:searchresults')][('response')][('results')][('result')][('taxAssessment')]
        df.iat[i, 6] = response_result[('SearchResults:searchresults')][('response')][('results')][('result')][('lotSizeSqFt')]
        df.iat[i, 7] = response_result[('SearchResults:searchresults')][('response')][('results')][('result')][('finishedSqFt')]
        df.iat[i, 8] = response_result[('SearchResults:searchresults')][('response')][('results')][('result')][('zestimate')][('amount')][('#text')]
        df.iat[i, 9] = response_result[('SearchResults:searchresults')][('response')][('results')][('result')][('zestimate')][('valuationRange')][('low')][('#text')]
        df.iat[i, 10] = response_result[('SearchResults:searchresults')][('response')][('results')][('result')][('zestimate')][('valuationRange')][('high')][('#text')]
    except KeyError:
        print('KeyError')
        
    except:
        print("Unexpected error:")

end = time.time()
print(end-start)
# print(df.head())