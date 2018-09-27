import os 
from urllib.request import urlretrieve
import pandas as pd

URL1 ='https://data.seattle.gov/api/views/mdbt-9ykn/rows.csv?accessType=DOWNLOAD'
URL = 'https://data.seattle.gov/api/views/3xqu-vnum/rows.csv?accessType=DOWNLOAD'
FREMONT_URL='https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# URL3 51W data line 

"""Download and cache the fremont data 

Parameters
----------
filename : string (optional)
    location to save the data 
url : string (optional)
    web location of the data
force_download : bool (optional)
    if True, force redownload of data 

Returns
-------
data : pandas.DataFrame
    The Fremont bridge Data
    
"""    
def get_fremont_data(filename="fremonts.csv",url=FREMONT_URL,force_download=False):
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
        
    data = pd.read_csv(filename,index_col='Date',parse_dates=True)
    data.columns =['West','East']
    data['Total'] = data['West']+data['East']
    return data