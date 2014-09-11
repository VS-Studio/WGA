#! /usr/bin/env python
# encoding:utf-8

import tornado.web
import tornado.ioloop

import tornado.websocket

class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message('Welcome to WebSocket')


class Index(tornado.web.RequestHandler):
    def get(self):
        self.write('''
<html>
<head>
<script>
var ws = new WebSocket('ws://10.1.72.154:8982/soc');
ws.onmessage = function(event) {
    document.getElementById('message').innerHTML = event.data;
};
</script>
</head>
<body>
<p id='message'></p>
        ''')
        
        

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/', Index),
        ('/soc', SocketHandler),
    ])
    app.listen(8982)
    tornado.ioloop.IOLoop.instance().start()
