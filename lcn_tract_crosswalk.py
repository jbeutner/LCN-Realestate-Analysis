import pandas as pd
import censusgeocode as cg
from random import uniform
from concurrent.futures import ThreadPoolExecutor
from tqdm.notebook import tqdm

#Import sold dataframe to obtain list of latitudes and longitudes
sold_df = pd.read_excel('lincoln_sold_2.xlsx')

#Change id to id_ (id is a reserved word in Python)
sold_df.columns = sold_df.columns.str.replace('id', 'id_')

#Create locations object containing id, latitude, and longitude
locations = sold_df[['id_','latitude','longitude']]

#Function to retrieve Census data and turn into dictionary
def geocode(row):
    index, id_, lat, lng = row
    try:
        census = cg.coordinates(lng, lat)['2020 Census Blocks'][0]

        data = dict(tract=census['TRACT'],
                   lat=lat,
                   lng=lng,
                   id_=id_)

    except Exception as e:
        data = dict(lat=lat,
                    lng=lng)

    return data

with ThreadPoolExecutor() as tpe:
     data = list(tqdm(tpe.map(geocode, locations.itertuples()), total=len(locations)))
tract_df = pd.DataFrame.from_records(data)

#export to to_excel
tract_df.to_excel('tract_df.xlsx')
