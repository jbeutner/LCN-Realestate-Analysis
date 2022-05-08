from sqlalchemy import create_engine
import requests
import json
import pandas as pd

#Sold homes data
sold_df = pd.read_excel('pgh_realestate_analysis/sold_df.xlsx')
engine = create_engine('postgresql://postgres:*****@localhost:5432/pgh_realestate')
sold_df.to_sql('sold', engine, if_exists='replace', method='multi', index=False)

#Census data
census_df = pd.read_excel('pgh_realestate_analysis/census_df.xlsx')
engine = create_engine('postgresql://postgres:*****@localhost:5432/pgh_realestate')
census_df.to_sql('census', engine, if_exists='replace', method='multi', index=False)

#Tract crosswalk
tract_crosswalk = pd.read_excel('pgh_realestate_analysis/tract_crosswalk.xlsx')
engine = create_engine('postgresql://postgres:*****@localhost:5432/pgh_realestate')
tract_crosswalk.to_sql('tract_crosswalk', engine, if_exists='replace', method='multi', index=False)
