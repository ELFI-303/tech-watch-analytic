from playwright.async_api import Playwright,Page
from dateutil.parser import parse

from datetime import datetime,timedelta
import re
from time import sleep

from tools.utils import get_first_locator_with_retries
from tools.config import googleIgnore
from website.website import website
from website.azure import *

class aws(website):
    def __init__(self, date_stop: datetime, date_start: datetime):
        self.date_stop, self.date_start = date_stop, date_start
        super().__init__("https://aws.amazon.com/blogs/?awsf.blog-master-category=category%23migration%7Ccategory%23aws-well-architected%7Ccategory%23aws-cloud-financial-management%7Ccategory%23storage%7Ccategory%23management-tools&awsf.blog-master-learning-levels=*all&awsf.blog-master-industry=*all&awsf.blog-master-analytics-products=*all&awsf.blog-master-artificial-intelligence=*all&awsf.blog-master-aws-cloud-financial-management=*all&awsf.blog-master-blockchain=*all&awsf.blog-master-business-applications=*all&awsf.blog-master-compute=*all&awsf.blog-master-customer-enablement=*all&awsf.blog-master-customer-engagement=*all&awsf.blog-master-database=*all&awsf.blog-master-developer-tools=*all&awsf.blog-master-devops=*all&awsf.blog-master-end-user-computing=*all&awsf.blog-master-mobile=*all&awsf.blog-master-iot=*all&awsf.blog-master-management-governance=*all&awsf.blog-master-media-services=*all&awsf.blog-master-migration-transfer=*all&awsf.blog-master-migration-solutions=*all&awsf.blog-master-networking-content-delivery=*all&awsf.blog-master-programming-language=*all&awsf.blog-master-sector=*all&awsf.blog-master-security=*all&awsf.blog-master-storage=*all",
                        (1,0,-1),
                        ('href','<b>','m-card-description'),
                        '.m-list-card',
                        '.blog-post-content',
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1200px-Amazon_Web_Services_Logo.svg.png")
    
    async def getPageInit(self, playwright):
        return await super().getPageInit(playwright)
    
    async def getArticles(self, page):
        return await super().getArticles(page)
    
    async def scrapBlog(self, playwright: Playwright) -> Page:
        page = await super().getPageInit(playwright)
        await self.getScrollPage(page)
        await page.close()
        #Initiate the page
        return page
    
    async def getScrollPage(self, page: Page) -> Page:
        while ((await self.getArticles(page))[1]):
            await page.locator(".m-directories-more-container").click(timeout=120000)
            sleep(1)
        return page
    
    def clearHrefField(self, field: str) -> str:
        #Clear
        return field
    
    def clearTitleField(self, field: str) -> str:
        #Clear
        return (field.replace(",","").replace("\n","").replace(";"," ").split("<b>")[1]).replace("&amp;", "&").split("</b>")[0]
    
    def clearDateField(self, field: str) -> datetime:
        #Clear
        try:
            date1 = (field.split("\n")[2]).replace(" ","").split("/")
            field = datetime(int(date1[2]),int(date1[0]),int(date1[1]))
        except:
            date2 = (field.split("\n")[1]).replace(" ","").split("/")
            field = datetime(int(date2[2]),int(date2[0]),int(date2[1]))
        return field

class azure:
    def __init__(self, date_stop: datetime, date_start: datetime):
        self.date_stop =date_stop
        self.date_start = date_start
        self.articles = []

    async def scrapBlog(self,playwright: Playwright) -> Page:
        browser = await playwright.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        """azBlog = azureBlog(self.date_stop,self.date_start)
        azTechBlog = azureTechBlog(self.date_stop,self.date_start)
        page1 = await azBlog.scrapBlog(playwright)
        self.articles += azBlog.articles
        await page1.close()
        page2 = await azTechBlog.scrapBlog(playwright)
        self.articles += azTechBlog.articles
        await page2.close()"""
        return page
    
class google(website):
    def __init__(self, date_stop: datetime, date_start: datetime):
        self.date_stop, self.date_start, self.init = date_stop, date_start, True
        super().__init__("https://cloud.google.com/blog/?hl=en",
                        (1,1,1),
                        ('href','Qwf2Db-MnozTc qPW6X nRhiJb-DbgRPb-R6PoUb-ma6Yeb Qwf2Db-MnozTc-OWXEXe-MnozTc-II5mzb','dEogG'),
                        '.u2M0Kb',
                        '.dQQu7c',
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png")
    
    async def getPageInit(self, playwright):
        return await super().getPageInit(playwright)
    
    async def getArticles(self, page: Page) -> bool:
        continuer = True
        k = -1
        articles_cards = await page.locator(self.locator).all()
        if self.init:
            print(len(articles_cards))
            li = articles_cards.pop()
            li = (await li.inner_html(timeout=120000)).split('"')
            href,date = "",""
            for i in range(len(li)-1):
                if self.balise[0] in li[i]:
                    href = self.clearHrefField(li[i+self.offset[0]])
                    new_context = page.context
                    new_page = await new_context.new_page()
                    await new_page.goto(href,timeout=1200000)
                    locators = await get_first_locator_with_retries(new_page, ".dEogG")
                    if type(locators) == str:
                        date = self.date_start - timedelta(days=1)
                    else:
                        date_loc = await locators.inner_html(timeout=120000)
                        date_loc = re.sub(r'[^a-zA-Z0-9 ]', '', date_loc)
                        date = parse(date_loc)
                    print('>'+date.strftime('%d/%m/%Y'))
                    locators = await get_first_locator_with_retries(new_page, self.corp)
                    if type(locators) == str:
                        print(href)
                        print(date)
                        await new_page.close()
                if href != "" and date != "":
                    break
            if self.date_start >= date and date >= self.date_stop:
                return page,continuer
            elif date <= self.date_stop:
                self.init = False
                return await self.getArticles(page)
            else:
                for u in range(len(articles_cards)-1):
                    self.ids.append(u)
                    self.ids = list(dict.fromkeys(self.ids))
                return page,continuer
        else:
            for li in articles_cards:
                k += 1
                if k in self.ids:
                    continue
                li = (await li.inner_html(timeout=120000)).split('"')
                href,title,date = "","",""
                for i in range(len(li)-1):
                    if self.balise[0] in li[i]:
                        href = self.clearHrefField(li[i+self.offset[0]])
                        new_context = page.context
                        new_page = await new_context.new_page()
                        await new_page.goto(href,timeout=1200000)
                        locators = await get_first_locator_with_retries(new_page, ".dEogG")
                        if type(locators) == str:
                            date = self.date_start - timedelta(days=1)
                        else:
                            date_loc = await locators.inner_html(timeout=120000)
                            date_loc = re.sub(r'[^a-zA-Z0-9 ]', '', date_loc)
                            date = parse(date_loc)
                        locators = await get_first_locator_with_retries(new_page, self.corp)
                        if type(locators) == str:
                            print(href)
                            print(date)
                            await new_page.close()
                        else:
                            text = await locators.all_inner_texts()
                            corp = ""
                            for el in text:
                                corp += el
                            await new_page.close()
                    if self.balise[1] in li[i]:
                        title = self.clearTitleField(li[i+self.offset[1]])
                    if href != "" and title != "" and date != "":
                        break
                if href.split('/')[5] in googleIgnore:
                    continue
                if self.date_start >= date and date >= self.date_stop:
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
    
    async def scrapBlog(self, playwright: Playwright) -> Page:
        page = await super().getPageInit(playwright)
        #await self.getScrollPage(page)
        #await page.close()
        #Initiate the page
        return page
    
    async def getScrollPage(self, page: Page) -> Page:
        length = 10
        while ((await self.getArticles(page))[1]):
            for i in range(9):
                length += 10
                await page.get_by_role("button", name="Load more stories").click()
                while(len(await page.locator(self.locator).all()) != length):
                    sleep(1)
        return page
    
    def clearHrefField(self, field: str) -> str:
        #Clear
        return field
    
    def clearTitleField(self, field: str) -> str:
        """
        ">Calling all devs: Code the future of baseball with Google Cloud and MLB</h5><p class="
        """
        #Clear
        return field.replace("</h5><p class=","").replace(">","")
    
    async def clearDateField(self, field: str) -> datetime:
        #Clear
        """
        "December19,2024"
        replace(" ","").replace("\n","")
        """
        field = field.replace("</div></div></section><divclass=","").replace(">","")
        field = re.sub(r"(\w+)(\d{1,2}),(\d{4})", r"\1 \2 \3", field)
        return parse(field)