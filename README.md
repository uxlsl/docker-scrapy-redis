# 使用docker-compose 编排scrapy-redis 例子

## 重要点
传REDIS的环境变量 

``` app/jm/jm/scrapy_redis_settings.py

REDIS_HOST = os.getenv('REDIS_HOST')

```

## 使用
 docker-compose --project-name app-test-1 -f docker-compose.yml up

## 参考
https://hackernoon.com/docker-tutorial-getting-started-with-python-redis-and-nginx-81a9d740d091
