import scrapy
from dotimg.items import DotimgItem

class pixelimgSpider(scrapy.Spider):
    name = "dotimg"
    start_urls = [
        "http://collepic.net/new/item?pg=0",
    ]
    web_url = 'http://collepic.net'
    oldpages = start_urls
    star = 0
    def parse(self, response):
        # url = response.xpath('//*[@class="tooltip"]/strong/a/@href').extract()
        get = response.xpath('//div[@class="itemtbl"]')
        index = 0
        for box in get:
            item = DotimgItem()
            array = box.xpath("a/@href").extract()
            text = box.xpath("a/text()").extract()
            item['Title'] = text[0]
            if len(text) > 1:
                item['Artist'] = text[1]
            else:
                item['Artist'] = "佚名"
            item['Pic_url'] = self.web_url + box.xpath("a/img/@src").extract()[0]
            item['Work_url'] = array[0]
            item['Artist_url'] = array[2]

            yield item

        url = response.xpath('//div[contains(@style,"font-size: 14px; text-align: center; margin: 4px 0;")][last()]/a/@href').extract()
        next_pages = url[len(url) - 1]
        if next_pages != self.oldpages[self.star]:
            self.oldpages[self.star] = next_pages
            ## 将 「下一页」的链接传递给自身，并重新分析
            yield scrapy.Request(self.web_url + self.oldpages[self.star], callback=self.parse)


    # def push_data(Data):

        # item = PixelimgItem()
        # print(Data)
        # # //*[@id="leftblockspan"]/div[1]/div/div[50]/a[3]
        # item['Title'] = response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[1]/td[2]/text()').extract()[0]
        # item['Artist'] = response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[2]/td[2]/a/text()').extract()[0]
        # item['Posted'] = response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[3]/td[2]/text()').extract()[0]
        # item['Artist_url'] = self.web_url+response.xpath('//*[@id="leftblockspan"]/div[1]/div/table/tr[1]/td/table/tr[2]/td[2]/a/@href').extract()[0]
        # lists = response.xpath('//*[@id="mainimg"]/@src').extract()
        # i = 0
        # for x in lists:
        #     lists[i] = self.web_url + x
        #     i +=1
        # item['image_urls'] = lists

        # yield item
