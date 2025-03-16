from pandas import concat,read_csv,DataFrame
import pandas as pd
import datetime as dt
from dateutil.parser import parse
from urllib.parse import urlparse
import os
import sys
import csv
maxInt = sys.maxsize
from tools.config import googleIgnore

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def split_years(dt):
    dt['year'] = pd.to_datetime(dt['date'], dayfirst=True).dt.year
    return [dt[dt['year'] == y] for y in dt['year'].unique()]

folder = 'results/'
test = 'test/'

aws2024 = read_csv(folder+'awsBlog_26-12-2023_26-12-2024.csv', sep='§', engine='python')
aws2023 = read_csv(folder+'awsBlog_26-12-2022_26-12-2023.csv', sep='§', engine='python')

google2023 = read_csv(folder+'googleBlog_24-12-2022_24-12-2023.csv', sep='§', engine='python')
google2024 = read_csv(folder+'googleBlog_24-12-2023_24-12-2024.csv', sep='§', engine='python')

google = concat([google2023,google2024],ignore_index=True)
aws = concat([aws2024,aws2023],ignore_index=True)

azure = DataFrame()
for file in os.listdir(folder):
    if 'azure' in file and 'HPC' not in file and 'AI' not in file:
        new_file = read_csv(folder+file, sep='§', engine='python')
        azure = concat([azure,new_file],ignore_index=True)

for index, element in google.iterrows():
    for blog in googleIgnore:
        if blog in element['href']:
            google = google.drop([index])

google = split_years(google)
aws = split_years(aws)
azure = split_years(azure)

for year in google:
    y = year.iloc[0]['year']
    year.to_csv(test+'google_'+str(y)+'.csv', sep='§',index=False)
for year in aws:
    y = year.iloc[0]['year']
    year.to_csv(test+'aws_'+str(y)+'.csv', sep='§',index=False)
for year in azure:
    y = year.iloc[0]['year']
    year.to_csv(test+'azure_'+str(y)+'.csv', sep='§',index=False)

