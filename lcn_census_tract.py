import requests
import pandas as pd

url = "https://api.census.gov/data/2020/acs/acs5?get=NAME,B01001_001E,B06011_001E,B06009_005E&for=tract:*&in=state:31&key={0}"\
    .format('API KEY')

response = requests.request("GET", url)

#Function to create pandas dataframe
def json_to_dataframe(response):
    """
    Convert response to dataframe
    """
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])

census_df = json_to_dataframe(response)

census_df.to_excel('census_df.xlsx')
