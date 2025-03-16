from playwright.async_api import Playwright, async_playwright

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from tools.utils import json_to_csv,defineDates
import asyncio
import inspect
import os
import pandas as pd
from website import sources
from tools.utils import getDates

async def run(playwright: Playwright) -> None:
    then = datetime.now()

    start_date = datetime.now() - relativedelta(years=3)

    classes = [obj for _, obj in inspect.getmembers(sources, predicate=inspect.isclass) if obj.__module__ == "website.sources"]
    for classe in classes:
        filename = f"{classe.__name__}_{start_date.strftime('%Y')}.csv"
        print(filename)
        if getDates(start_date,filename) != False:
            date_stop, date_start, current_file = getDates(start_date,filename)
        else:
            print(classe.__name__+' Error with the starting date!')
        print(date_start,date_stop)
        classe = classe(date_stop,date_start)
        page = await classe.scrapBlog(playwright)
        if type(current_file) == type(pd.DataFrame()):
            current_file = current_file.drop('year', axis=1)
            for article in classe.articles:
                art = pd.DataFrame([article])
                current_file = pd.concat([current_file,art],ignore_index=True)
            current_file.drop_duplicates()
            current_file.to_csv('test_'+filename, sep='§', index=False)
        else:
            if len(classe.articles) != 0:
                print(classe.articles)
                json_to_csv(classe.articles, filename)
    await page.context.close()

    now = datetime.now()
    print("Processing time: "+str(now - then)+" seconds")

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright.chromium)

asyncio.run(main())
