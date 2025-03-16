from playwright.async_api import Page,Playwright

from abc import ABC,abstractmethod
from datetime import datetime
import json

from tools.utils import get_first_locator_with_retries

class website(ABC):
    @abstractmethod
    def __init__(self, url: str, offset: tuple, balise: tuple, locator: str, corp: str, imgUrl: str):
        self.url = url
        self.offset = offset
        self.balise = balise
        self.locator = locator
        self.corp = corp
        self.imgUrl = imgUrl
        self.actors = []
        self.articles = []
        self.ids = []
        self.cookies = []
        
    @abstractmethod
    async def getPageInit(self, playwright: Playwright) -> Page:
        browser = await playwright.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(self.url)
        return page
    
    @abstractmethod
    async def getArticles(self, page: Page) -> bool:
        continuer = True
        k = -1
        articles = await page.locator(self.locator).all()
        for li in articles:
            k += 1
            li = (await li.inner_html(timeout=120000)).split('"')
            if k in self.ids:
                continue
            self.ids.append(k)
            date = ""
            href,title,date = "","",""
            for i in range(len(li)-1):
                if self.balise[0] in li[i]:
                    href = self.clearHrefField(li[i+self.offset[0]])
                if self.balise[1] in li[i]:
                    title = self.clearTitleField(li[i+self.offset[1]])
                if self.balise[2] in li[i]:
                    date = self.clearDateField(str(li[i+self.offset[2]]))
                    if date == datetime(2025,1,1):
                        print(li)
                if href != "" and title != "" and date != "":
                    break
            
            if self.date_start >= date and date >= self.date_stop:
                corp = await self.navigateArticle(page,href)
                print(date)
                article = {
                    "title":title,
                    "date":date.strftime("%d/%m/%Y"),
                    "href":href,
                    "corp":corp
                }
                if article not in self.articles:
                    self.articles.append(article)
            elif date >= self.date_start:
                continue
            else:
                continuer = False
                break
        return page,continuer
    
    async def navigateArticle(self, page: Page, href: str) -> str:
        new_context = page.context
        new_page = await new_context.new_page()
        await new_page.goto(href,timeout=120000)
        locators = await get_first_locator_with_retries(new_page, self.corp)
        if type(locators) == str:
            await new_page.close()
            return ""
        text = await locators.all_inner_texts()
        string = ""
        for el in text:
            string += el
        await new_page.close()
        return string