from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from whois.items import WhoisPage

class IanaSpider(BaseSpider):
    name = "iana"
    allowed_domains = ["http://www.iana.org/"]
    start_urls = [
      "http://www.iana.org/domains/root/db",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//a[contains(@href, "/domains/root/db/")]')
        items = []
        for row in links:
            item = WhoisPage()
            #item['domain'] = row.select("text()").extract()

            item['url'] = "".join(["http://www.iana.org/", ] + row.select("@href").extract())
            items.append(item)
        return items

