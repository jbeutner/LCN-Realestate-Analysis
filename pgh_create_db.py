from sqlalchemy import create_engine
import requests
import json
import pandas as pd

#Sold homes data
sold_df = pd.read_excel('lcn_realestate_analysis/lincoln_sold_df.xlsx')
engine = create_engine('postgresql://postgres:password@localhost:5432/lcn_db')
sold_df.to_sql('sold', engine, if_exists='replace', method='multi', index=False)

#Census data
census_df = pd.read_excel('lcn_realestate_analysis/lincoln_census_df.xlsx')
engine = create_engine('postgresql://postgres:password@localhost:5432/lcn_db')
census_df.to_sql('census', engine, if_exists='replace', method='multi', index=False)

#Tract crosswalk
tract_crosswalk = pd.read_excel('lcn_realestate_analysis/lincoln_tract_crosswalk.xlsx')
engine = create_engine('postgresql://postgres:password@localhost:5432/lcn_db')
tract_crosswalk.to_sql('tract_crosswalk', engine, if_exists='replace', method='multi', index=False)
