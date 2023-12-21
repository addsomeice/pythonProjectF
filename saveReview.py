#!/usr/bin/env python3
from flask import Flask, jsonify
from flask import render_template
from flask import request
import math
import json
from azure.cosmos import CosmosClient
import redis
import time

DB_CONN_STR =  "AccountEndpoint=https://tutorial-uta-cse6332.documents.azure.com:443/;" \
               "AccountKey=fSDt8pk5P1EH0NlvfiolgZF332ILOkKhMdLY6iMS2yjVqdpWx4XtnVgBoJBCBaHA8PIHnAbFY4N9ACDbMdwaEw==;"
db_client = CosmosClient.from_connection_string(conn_str=DB_CONN_STR)
database = db_client.get_database_client("tutorial")
# city_name = 'Parma'
# container = database.get_container_client("us_cities")
# query_review = "SELECT * FROM c WHERE c.city = @city_name"
# params = [dict(name="@city_name", value=city_name)]
# reviews = list(container_reviews.query_items(query_review, parameters=params , enable_cross_partition_query=True))
# print(reviews)
# for review in reviews:
#     # print(reviews['score'])
#     score = int(review['score'])
#     print(score)

import math
import json
import redis


# 建立与 Redis 的连接
redis_passwd = "dH83jFtaYDZA7socl4hld3cGCgMu81TCrAzCaMSKXMs="
redis_host = "LiushuaiRedis.redis.cache.windows.net"
cache = redis.StrictRedis(
    host=redis_host, port=6380,
    db=0, password=redis_passwd,
    ssl=True,
)

# if cache.ping():
#     print("pong")
# key_to_delete = "SELECT c.score,c.city,c.review FROM c"
# cache.delete(key_to_delete)

# def purge_cache():
#     for key in cache.keys():
#          cache.delete(key.decode())
# purge_cache()
# print("true")

# # 从数据库中获取城市数据
container = database.get_container_client("us_cities")
query_review = "SELECT c.score,c.city,c.review FROM c"
#container_reviews = database.get_container_client("reviews")
#
# # 第一步查询：获取城市属性
query = "SELECT c.city, c.lat, c.lng, c.state, c.population FROM c"
#resultRe = container_reviews.query_items(query_review, enable_cross_partition_query=True)
result=container.query_items(query, enable_cross_partition_query=True)
cities = list(result)
#reviews = list(resultRe)
# #
print(cities)
# #
redis_key = 'cities'
#encoded_review = json.dumps(reviews)
encoded_review = json.dumps(cities)
cache.set(redis_key, encoded_review)



