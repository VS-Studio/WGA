#! /usr/bin/env python
# encoding:utf-8


from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    
    print response.headers
    print response.reason
    
    body = response.body
    #print body
    return body



synchronous_fetch("http://www.baidu.com")