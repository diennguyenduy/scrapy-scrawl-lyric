# -*- coding: utf-8 -*-

# Scrapy settings for nhaccuatui project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
ITEM_PIPELINES = {
    'scrapy_mysql_pipeline.MySQLPipeline':300,
}

BOT_NAME = 'nhaccuatui'

SPIDER_MODULES = ['nhaccuatui.spiders']
NEWSPIDER_MODULE = 'nhaccuatui.spiders'

MYSQL_HOST = 'localhost'
MYSQL_DB = 'scrapy'
MYSQL_TABLE = 'Songs'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '12345678'
MYSQL_PORT = 3306
