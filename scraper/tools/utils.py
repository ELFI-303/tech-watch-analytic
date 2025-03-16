from markdown import markdown
from ttp import ttp
from playwright.async_api import Page
from pandas import DataFrame,to_datetime,read_csv
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

import re
import os
import asyncio

from tools.config import categories

if not os.path.exists("results"):
    os.makedirs("results")

def remove_emojis(input_string: str) -> str:
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
        "\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed Characters
        "\U0001F926-\U0001F937"  # Supplemental Symbols
        "\U00010000-\U0010FFFF"  # Supplementary Private Use Area
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', input_string)

def word_match(resume: str) -> list:
    matched_categories = []
    for category, keywords in categories.items():
        if any(keyword.lower() in (resume.lower()) for keyword in keywords):
            matched_categories.append(category)
    return matched_categories

def json_to_csv(json: dict, filename: str) -> None:
    tab = DataFrame.from_dict(json)
    tab['title'] = tab['title'].replace('"',"'")
    tab['title'] = '"'+tab['title']+'"'
    tab['corp'] = tab['corp'].replace('"',"'")
    tab['corp'] = '"'+tab['corp']+'"'
    tab.to_csv('results/test_'+filename, sep='§', index=False)

async def get_first_locator_with_retries(page: Page, selector, max_retries=5, delay=5):
    for attempt in range(max_retries):
        try:
            locators = await page.locator(selector).all()
            if locators:
                return locators[0]
            else:
                raise
        except:
            if attempt < max_retries - 1:
                await asyncio.sleep(delay)
            else:
                return page.url

def get_info() -> tuple:
    return os.environ.get('x_info_scrap').split(":")

def monthRange(date: datetime):
    date = (date - timedelta(days=(date.day-1)) 
            - timedelta(hours=(date.hour)) 
            - timedelta(minutes=(date.minute)) 
            - timedelta(seconds=(date.second))
            - timedelta(microseconds=(date.microsecond)))
    return date,(date + relativedelta(months=1) - timedelta(microseconds=1))

def progress_bar(progress, total):
    length = 50
    multiplier = 100/length
    percent = length * (progress / float(total))
    bar = '▓' * int(percent) + '▒' * (length - int(percent))
    print(f"\r{bar} Processing websites: {percent*multiplier:.2f}%", end="\r")

def defineDates(name: str, date_start: datetime, date_stop: datetime):
    array = []
    for filename in os.listdir('test'):
        if name in filename:
            array.append(filename)
    for file in array:
        separated = file.split('_')
        date1 = parse(separated[1])
        date2 = parse(separated[2].replace('.csv',''))
        if date_start >= date1 and date1 >= date_stop:
            date_start = date1
        elif date_start >= date2 and date2 >= date_stop:
            date_stop = date2
    return date_start,date_stop

def getDates(start_date: datetime, filename: str):
    current_file = None
    for file in os.listdir('test'):
        if file == filename:
            print('yeah')
            current_file = read_csv('test/'+file, sep='§', engine='python')
    if type(current_file) == type(DataFrame()):
        first_date = to_datetime(current_file['date'],dayfirst=True).max()
        last_date = to_datetime(current_file['date'],dayfirst=True).min()
        if start_date >= first_date:
            print('a')
            stop_date = first_date + relativedelta(days=1)
        elif last_date >= start_date:
            print('b')
            start_date = last_date - relativedelta(days=1)
            stop_date = datetime(start_date.year,1,1)
        else:
            return False
    else:
        print('c')
        current_file = False
        start_date = datetime(start_date.year,12,31)
        stop_date = datetime(start_date.year,1,1)
    return stop_date,start_date,current_file