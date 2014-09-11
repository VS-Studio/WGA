#!/usr/bin/env python
#encoding=utf-8

import tornado.ioloop
import tornado.web
import tornado.httpserver
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

#导入包
from app import WebServer



#定义应用
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", WebServer.Home),
            (r"/_t", WebServer.Test),
            (r"/_q", WebServer.Query),
            (r"/_c/(.*)", WebServer.Comment),
        ];
        settings = dict(
            debug=True
        );
        tornado.web.Application.__init__(self, handlers, **settings);



#初始化
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application());
    http_server.listen(8982);
    #tornado.ioloop.PeriodicCallback(Schedules.Schedules().start, 1000).start()
    tornado.ioloop.IOLoop.instance().start();
    
    
    