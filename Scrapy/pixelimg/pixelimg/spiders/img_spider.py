import scrapy
from pixelimg.items import PixelimgItem

class pixelimgSpider(scrapy.Spider):
    name = "pixelimg"
    start_urls = [
        "http://pixeljoint.com/pixels/new_icons.asp?ob=rating",
    ]
    web_url = 'http://pixeljoint.com'
    oldpages = start_urls
    star = 0
    def parse(self, response):
        url = response.xpath('//*[@class="tooltip"]/strong/a/@href').extract()
        for x in url:
            yield scrapy.Request(self.web_url+x, callback=self.parse_content)

        next_pages = response.xpath('//*[@id="leftblockspan"]/div[1]/div/div[50]/a[3]/@href').extract()

        # if next_pages[0] != self.oldpages[self.star]:
        #     self.oldpages[self.star] = next_pages[0]
        # #     ## 将 「下一页」的链接传递给自身，并重新分析
        #     yield scrapy.Request(self.web_url + self.oldpages[self.star], callback=self.parse)


    def parse_content(self, response):
        item = PixelimgItem()
        # //*[@id="leftblockspan"]/div[1]/div/div[50]/a[3]
        item['Title'] = response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[1]/td[2]/text()').extract()[0]
        item['Artist'] = response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[2]/td[2]/a/text()').extract()[0]
        item['Posted'] = response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[3]/td[2]/text()').extract()[0]
        item['Artist_url'] = self.web_url+response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[2]/td[2]/a/@href').extract()[0]
        item['Pic_url'] = response.xpath('//*[@id="mainimg"]/@src').extract()[0]
        # i = 0
        # for x in lists:
        #     lists[i] = self.web_url + x
        #     i +=1
        # item['image_urls'] = lists

        yield item
