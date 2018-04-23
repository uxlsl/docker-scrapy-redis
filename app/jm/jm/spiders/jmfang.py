# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider


class JmfangSpider(RedisSpider):
    name = 'jmfang'
    allowed_domains = ['esf.jm.fang.com']

    def parse(self, response):
        pass
