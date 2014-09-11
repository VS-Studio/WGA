#! /usr/bin/env python
# encoding:utf-8

import tornado
import tornado.httpclient

class Handler(tornado.web.RequestHandler):
    
    def error(self, code, msg):
        raise tornado.web.HTTPError(code, msg);

    def json_encode(self,obj):
        return tornado.escape.json_encode(obj);
    
    def json_decode(self,obj):
        return tornado.escape.json_decode(obj);
    
    def echo_json(self,obj):
        self.write(self.json_encode(obj));
        
    def file_get_content(self,url):
        client = tornado.httpclient.HTTPClient();
        return client.fetch(url).body;
    
    def file_get_content_asyn(self,url,callback):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(url, callback=callback)