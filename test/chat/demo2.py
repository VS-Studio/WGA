#! /usr/bin/env python
# encoding:utf-8

import tornado.web
import tornado.ioloop

import tornado.websocket

class SocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()

    @staticmethod
    def send_to_all(message):
        for c in SocketHandler.clients:
            c.write_message(message)

    def open(self):
        self.write_message('Welcome to WebSocket')
        SocketHandler.send_to_all(str(id(self)) + ' has joined')
        SocketHandler.clients.add(self)

    def on_close(self):
        SocketHandler.clients.remove(self)
        SocketHandler.send_to_all(str(id(self)) + ' has left')


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('chat.html')
        
        

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
        ('/soc', SocketHandler),
    ])
    app.listen(8982)
    tornado.ioloop.IOLoop.instance().start()
