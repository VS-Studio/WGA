#! /usr/bin/env python
# encoding:utf-8


from tornado import ioloop
from tornado import iostream
import socket
import errno
import functools

def handle_connection(client, address): 
  #buf = client.recv(1024)
  #print buf
  
  client.send("HTTP/1.1 200 OK\r\n\r\n")
  client.send("Hello, World")
  client.close()

def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error, e:
            if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return
        connection.setblocking(0)
        handle_connection(connection, address)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)
sock.bind(("10.1.72.154", 8982))
sock.listen(128)

io_loop = ioloop.IOLoop.instance()
callback = functools.partial(connection_ready, sock)
io_loop.add_handler(sock.fileno(), callback, io_loop.READ)
io_loop.start()