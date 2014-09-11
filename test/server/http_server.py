#! /usr/bin/env python
# encoding:utf-8

#! /usr/bin/env python
#coding=utf-8
  
from tornado.tcpserver import TCPServer  
from tornado.ioloop  import IOLoop  
  
class Connection(object):  

    def __init__(self, stream, address): 
        self._stream = stream  
        self._address = address  
        self._stream.set_close_callback(self.on_close)  
        self.read_message()  
        print "A new user has entered the chat room.", address 
        
      
    def read_message(self):  
        self._stream.read_until('\n', self.send_message)  
      
    def send_message(self, data):  
        self._stream.write(data) 
          
    def on_close(self):  
        print "A user has left the chat room.", self._address

  
class ChatServer(TCPServer):  
    def handle_stream(self, stream, address): 
        print "New connection :", address, stream 
        Connection(stream, address) 
        print "connection num is:", len(Connection.clients)
  
if __name__ == '__main__':  
    print "Server start ......"  
    server = ChatServer()  
    server.listen(8982)  
    IOLoop.instance().start() 