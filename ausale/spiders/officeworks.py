from bs4 import BeautifulSoup as bs
from ausale.items import AusaleItem
from scrapy.http import Request
from scrapy.spider import Spider

class OfficeworksSpider(Spider):
  name = "officeworks"
  allowed_domain = ['www.officeworks.com.au']
  # start_urls = ['http://www.officeworks.com.au/shop/SearchDisplay?searchTerm=dolce+gusto&storeId=10151&langId=-1&pageSize=24&beginIndex=0&sType=SimpleSearch&resultCatEntryType=2&showResultsPage=true&searchSource=Q&pageView=']
  start_urls = ('http://www.officeworks.com.au/shop/SearchDisplay?searchTerm=dolce+gusto&storeId=10151',)

  def parse(self, response):
    soup = bs(response.body)
    # print(soup)
    items = soup.find_all("div", class_="span12")
    for item in items:
      title = item.find("h2")
      if title:
        title = title.get_text().strip()
      price = item.find("div",class_="price")
      if price:
        price = price.get_text()
      bulk_price = item.find("td", class_="price")
      if bulk_price:
        bulk_price = bulk_price.get_text()
      officeworks_item = AusaleItem()
      officeworks_item['title'] = title
      officeworks_item['price'] = price
      officeworks_item['bulk_price'] = bulk_price
      print(officeworks_item)
      return officeworks_item