# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class WhoisPage(Item):
    url = Field()

class WhoisItem(Item):
    # define the fields for your item here like:
    # name = Field()
    domain = Field()
    idna = Field()
    whois = Field()
    url = Field()
    