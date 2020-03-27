import pandas as pd
import io
import requests
import json
import sys
import os
import datetime

from country_codes import country_code

url_confirmed="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url_deaths="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
url_recovered ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

def populate(json, df, dftype):

    json[dftype] = {}
    json[dftype]['locations'] = []
    
    tmp_latest_confirmed = int(df.sum(axis=0)[-1])

    for index, row in df.iterrows():

        tmp_element = {}
        
        tmp_province = str(row['Province/State'])
        tmp_country_name = row['Country/Region']

        tmp_country_code = country_code(tmp_country_name)
        tmp_country_latest = row[-1]

        tmp_country_position = {}
        tmp_country_position['latitude'] = row['Lat']
        tmp_country_position['longitude'] = row['Long']

        tmp_country_history = {}

        for i in range (4,df.shape[1]):
            tmp_country_history[list(df.columns.values)[i]] = row[i]

        tmp_element['coordinates'] = tmp_country_position
        tmp_element['country'] = tmp_country_name
        tmp_element['country_code'] = tmp_country_code
        tmp_element['history'] = tmp_country_history
        tmp_element['latest'] = tmp_country_latest
        tmp_element['province'] = tmp_province
        json[dftype]['locations'].append(tmp_element)

    json[dftype]['latest'] = tmp_latest_confirmed

    return json

def update():

    # Initialise the json object
    json_data_final = {}

    # Get content using http request
    try:
        confirmed_=requests.get(url_confirmed).content
    except requests.exceptions.RequestException as e:
        print("Fatal error on confirmed cases request")
        raise SystemExit(e)

    try:
        deaths_=requests.get(url_deaths).content
    except requests.exceptions.RequestException as e:
        print("Fatal error on deaths cases request")
        raise SystemExit(e)

    try:
        recovered_=requests.get(url_recovered).content
    except requests.exceptions.RequestException as e:
        print("Fatal error on recovered cases request")
        raise SystemExit(e)


    # Confirmed cases
    df_confirmed=pd.read_csv(io.StringIO(confirmed_.decode('utf-8')))
    json_data_final = populate(json_data_final,df_confirmed,"confirmed")

    # Deaths cases
    df_deaths=pd.read_csv(io.StringIO(deaths_.decode('utf-8')))
    json_data_final = populate(json_data_final,df_deaths,"deaths")

    # Recovered cases
    df_recovered=pd.read_csv(io.StringIO(recovered_.decode('utf-8')))
    json_data_final = populate(json_data_final,df_recovered,"recovered")

    # Latest cases
    json_data_final['latest'] = {}
    json_data_final['latest']['confirmed'] = json_data_final['confirmed']['latest']
    json_data_final['latest']['deaths'] = json_data_final['deaths']['latest']
    json_data_final['latest']['recovered'] = json_data_final['recovered']['latest']

    # Update datetime
    json_data_final['updatedAt'] = str(datetime.datetime.utcnow())

    with open('data.json', 'w') as f:
        json.dump(json_data_final, f)
        sys.stdout.flush()
        print("Data Updated !")

    return 0