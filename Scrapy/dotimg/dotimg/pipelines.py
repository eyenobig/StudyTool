# -*- coding: utf-8 -*-
import requests
import os
from dotimg.settings import IMAGES_STORE

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DotimgPipeline(object):
    def process_item(self, item, spider):
        r = requests.get(item['Pic_url'])
        duan = item['Pic_url'].split("/")
        save = duan[-2] + "-" + duan[-1] + ".gif"

        # print(save)
        isExists=os.path.exists(IMAGES_STORE+save)

        if not isExists:
            gif = open(IMAGES_STORE+"/"+save, 'wb')
            gif.write(r.content)
        else:
            gif = open(IMAGES_STORE+"/"+save, 'wb')
            gif.write(r.content)
        return item
