import scrapy
from bs4 import BeautifulSoup

# scrapy runspider httpScrapy.py


class SXLJSpider(scrapy.Spider):
    name = "sxljSpider"
    start_urls = ["https://sx.lianjia.com/ershoufang/keqiaoqu/"]

    def parse(self, response):
        print(f"start: {'-'*60}")
        print(f"url: {response.url}")
        print(f"code: {response.status}")
        pages = response.css(".page-box.fr")
        print(pages.get())
        pagedata = pages.css("div:first-child")
        print(pagedata.get())
        page = pagedata.css("div::attr(page-data)")
        d = page.get()
        print(type(d), dict(d))
        print(f"start: {'*'*60}")
        return True
