#! /usr/bin/env python
# encoding:utf-8


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8804, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://api.video.ucweb.com/interface/compact.php?coms=[{%22com%22:%22com_video_search%22,%22param%22:%22{\%22count\%22:10,\%22q\%22:\%22Kick\%22}%22}]",
                callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        
        print body;
       
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()