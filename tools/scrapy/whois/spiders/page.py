from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from whois.items import WhoisItem

class PageSpider(BaseSpider):
    name = 'page'
    allowed_domains = ['www.iana.org']

    start_urls = [l.strip() for l in open('items.lst').readlines()][1:]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        i = WhoisItem()
        i['idna'] = response.url.split('/')[-1].split('.')[0]
        i['domain'] = "".join("".join(hxs.select('//title/text()').extract()).split()[2:3])
        i['url'] = hxs.select('//*[@id="main_right"]/p[1]/a/@href').extract()
        if hxs.select('//*[@id="main_right"]').re(r'WHOIS Server'):
            #i['whois'] = "".join([x.extract().strip() for x in hxs.select('//*[@id="main_right"]/p[1]/text()')])
            i['whois'] = "".join(hxs.select('//*[@id="main_right"]').re(r'WHOIS Server:\</b\>(?P<whois>.+)')).strip()
        else:
            i['whois'] = ''

        return i
