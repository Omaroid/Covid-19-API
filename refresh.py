import pandas as pd
import io
import requests
from country_codes import country_code
import json
import math
import sys

url_confirmed="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
url_deaths="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
url_recovered="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"

s=requests.get(url_confirmed).content
df_confirmed=pd.read_csv(io.StringIO(s.decode('utf-8')))

s=requests.get(url_deaths).content
df_deaths=pd.read_csv(io.StringIO(s.decode('utf-8')))

s=requests.get(url_recovered).content
df_recovered=pd.read_csv(io.StringIO(s.decode('utf-8')))

json_data_final = {}
json_data_list = []

json_data_final['confirmed'] = {}
json_data_final['confirmed']['locations'] = []
json_data_final['deaths'] = {}
json_data_final['deaths']['locations'] = []
json_data_final['recovered'] = {}
json_data_final['recovered']['locations'] = []

# Confirmed

tmp_latest_confirmed = int(df_confirmed.sum(axis=0)[-1])

for index, row in df_confirmed.iterrows():

    tmp_element = {}
    
    tmp_province = str(row['Province/State'])
    tmp_country_name = row['Country/Region']
    tmp_country_code = country_code(row['Country/Region'])
    tmp_country_latest = row[-1]

    tmp_country_position = {}
    tmp_country_position['latitude'] = row['Lat']
    tmp_country_position['longitude'] = row['Long']

    tmp_country_history = {}
    for i in range (4,df_confirmed.shape[1]):
        tmp_country_history[list(df_confirmed.columns.values)[i]] = row[i]
    
    tmp_element['coordinates'] = tmp_country_position
    tmp_element['country'] = tmp_country_name
    tmp_element['country_code'] = tmp_country_code
    tmp_element['history'] = tmp_country_history
    tmp_element['latest'] = tmp_country_latest
    tmp_element['province'] = tmp_province
    json_data_final['confirmed']['locations'].append(tmp_element)

json_data_final['confirmed']['latest'] = tmp_latest_confirmed

# Deaths

tmp_latest_deaths = int(df_deaths.sum(axis=0)[-1])

for index, row in df_deaths.iterrows():

    tmp_element = {}
    
    tmp_province = str(row['Province/State'])
    tmp_country_name = row['Country/Region']
    tmp_country_code = country_code(row['Country/Region'])
    tmp_country_latest = row[-1]

    tmp_country_position = {}
    tmp_country_position['latitude'] = row['Lat']
    tmp_country_position['longitude'] = row['Long']

    tmp_country_history = {}
    for i in range (4,df_deaths.shape[1]):
        tmp_country_history[list(df_deaths.columns.values)[i]] = row[i]
    
    tmp_element['coordinates'] = tmp_country_position
    tmp_element['country'] = tmp_country_name
    tmp_element['country_code'] = tmp_country_code
    tmp_element['history'] = tmp_country_history
    tmp_element['latest'] = tmp_country_latest
    tmp_element['province'] = tmp_province
    json_data_final['deaths']['locations'].append(tmp_element)

json_data_final['deaths']['latest'] = tmp_latest_deaths

# Recovered

tmp_latest_recovered = int(df_recovered.sum(axis=0)[-1])

for index, row in df_recovered.iterrows():

    tmp_element = {}
    
    tmp_province = str(row['Province/State'])
    tmp_country_name = row['Country/Region']
    tmp_country_code = country_code(row['Country/Region'])
    tmp_country_latest = row[-1]

    tmp_country_position = {}
    tmp_country_position['latitude'] = row['Lat']
    tmp_country_position['longitude'] = row['Long']

    tmp_country_history = {}
    for i in range (4,df_recovered.shape[1]):
        tmp_country_history[list(df_recovered.columns.values)[i]] = row[i]
    
    tmp_element['coordinates'] = tmp_country_position
    tmp_element['country'] = tmp_country_name
    tmp_element['country_code'] = tmp_country_code
    tmp_element['history'] = tmp_country_history
    tmp_element['latest'] = tmp_country_latest
    tmp_element['province'] = tmp_province
    json_data_final['recovered']['locations'].append(tmp_element)

json_data_final['recovered']['latest'] = tmp_latest_recovered

# Latest

json_data_final['latest'] = {}

json_data_final['latest']['confirmed'] = tmp_latest_confirmed
json_data_final['latest']['deaths'] = tmp_latest_deaths
json_data_final['latest']['recovered'] = tmp_latest_recovered

with open('data.json', 'w') as f:
    json.dump(json_data_final, f)
    sys.stdout.flush()
    print("Data Updated !")
