# -*- coding: utf-8 -*-
import requests
import os
from dotimg.settings import IMAGES_STORE

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PixelimgPipeline(object):
    def process_item(self, item, spider):
        r = requests.get(item['Pic_url'])
        duan = item['Pic_url'].split("/")
        print(item['Artist']+ "-" +duan[-1])
        # save = duan[-2] + "-" + duan[-1] + ".gif"

        # print(save)
        # isExists=os.path.exists(IMAGES_STORE+save)

        # if not isExists:
        #     gif = open(IMAGES_STORE+"/"+save, 'wb')
        #     gif.write(r.content)
        # else:
        #     gif = open(IMAGES_STORE+"/"+save, 'wb')
        #     gif.write(r.content)
        # return item



# class MyImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield scrapy.Request(image_url)

#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item


