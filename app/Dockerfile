FROM python:latest
RUN pip install scrapy-redis -i https://pypi.douban.com/simple/
ADD jm /jm
WORKDIR /jm
CMD scrapy crawl jmfang
