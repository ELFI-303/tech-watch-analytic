from playwright.async_api import Playwright,Page
from dateutil.parser import parse

from datetime import datetime
from time import sleep
from tools.config import azureTechBlogs
from website.website import website

class azureBlog(website):
    def __init__(self, date_stop: datetime, date_start: datetime):
        self.date_stop, self.date_start = date_stop, date_start
        super().__init__("https://azure.microsoft.com/en-us/blog/?sort-by=newest-oldest&date=any&s=",
                        (2,3,-2),
                        ('search-result-card','search-result-card','min read'),
                        '.msx-card__body',
                        '.single-layout__content',
                        "https://roverba.com/wp-content/uploads/2024/02/logo-Microsoft-Azure.jpg")
    
    async def getPageInit(self, playwright):
        return await super().getPageInit(playwright)
    
    async def getArticles(self, page):
        return await super().getArticles(page)
    
    async def scrapBlog(self, playwright: Playwright) -> Page:
        page = await super().getPageInit(playwright)
        await self.getScrollPage(page)
        #Initiate the page
        return page
    
    async def getScrollPage(self, page: Page) -> Page:
        while ((await self.getArticles(page))[1]):
            await page.get_by_role("button", name="Load more").click()
            sleep(1)
        return page
    
    def clearHrefField(self, field: str) -> str:
        #Clear
        return field
    
    def clearTitleField(self, field: str) -> str:
        #Clear
        return field.replace(">\n\t\t\t\t\t<span>","").replace("</span>&nbsp;<span class=","").replace("&nbsp;"," ").replace("&amp;", "&").replace(",","").replace("\n","").replace(";"," ")
    
    def clearDateField(self, field: str) -> datetime:
        #Clear
        field = field.replace("\n","").replace("\t","").replace(" ","").replace("</li><liclass=","").replace(">","")
        if len(field.split(",")) == 1:
            field = field[3:]+" "+field[:3]+" "+str(datetime.now().year)
        else:
            field = field.split(",")
            field = field[0][3:]+" "+field[0][:3]+" "+str(field[1])
        return parse(field)

class azureTechBlog(website):
    def __init__(self, date_stop: datetime, date_start: datetime):
        self.date_stop, self.date_start = date_stop, date_start
        super().__init__("",
                        (10,2,2),
                        ('MessageViewCard_lia-message-img-wrap___G72a','MessageViewCard_lia-subject-wrap__glXCU','messageTime'),
                        '.MessageViewCard_lia-card-wrap__iy_tA',
                        '.styles_clearfix__xFEoC',
                        "https://cours-informatique-gratuit.fr/wp-content/uploads/2014/05/microsoft.png")
        
    async def getPageInit(self, playwright):
        return await super().getPageInit(playwright)
    
    async def getArticles(self, page):
        return await super().getArticles(page)
    
    async def scrapBlog(self, playwright: Playwright) -> Page:
        browser = await playwright.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        """for url in azureTechBlogs:
            self.ids = []
            print(url.split('/category/')[1])
            await page.goto(url)
            await self.getScrollPage(page)"""
        return page
    
    async def getScrollPage(self, page: Page) -> Page:
        while ((await self.getArticles(page))[1]):
            try:
                await page.get_by_test_id("PanelItemList.MessageListForNodeByRecentActivityWidget").get_by_test_id("PanelItemList.Footer").click(timeout=120000)
            except:
                with open('output.txt','w',encoding='utf-8') as file:
                    file.write(await page.locator('body').inner_html())
                break
            sleep(1)
        return page
    
    def clearHrefField(self, field: str) -> str:
        #Clear
        return 'https://techcommunity.microsoft.com'+field
    
    def clearTitleField(self, field: str) -> str:
        #Clear
        return field
    
    def clearDateField(self, field: str) -> datetime:
        #Clear
        field = field.split(' at ')[0].replace(',','')
        return parse(field)
