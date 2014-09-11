#! /usr/bin/env python
# encoding:utf-8


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8804, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,
                "http://api.video.ucweb.com/interface/compact.php?coms=[{%22com%22:%22com_video_search%22,%22param%22:%22{\%22count\%22:10,\%22q\%22:\%22Kick\%22}%22}]")
        body = json.loads(response.body)
        result_count = len(body[0]['data'][0]['video_list'])
        now = datetime.datetime.utcnow()
        
        print response;
        
        raw_oldest_tweet_at = body[0]['data'][0]['video_list'][4]['update_time']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%Y-%m-%d %H:%M:%S")
        seconds_diff = time.mktime(now.timetuple()) - \
                time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (query, tweets_per_second))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()