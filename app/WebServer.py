#!/usr/bin/env python
#encoding=utf-8

import Base
import torndb;

class Home(Base.Handler):
    def get(self):
        self.write("Welcome WGA v1.0\n");
        
class Test(Base.Handler):
    def get(self):
        self.write("TEST\n");
       
        
class Comment(Base.Handler):
    def get(self, info):
        
        info = self.pathInfo(info);
        
        if(len(info) < 2):
            raise self.error(400,"input value invalid");
        
        db = info[0];
        table = info[1];
        
        #db=torndb.Connection('127.0.0.1','liujf_db', 'root','root','root');
        
        self.write("\n " + info);
        
        
        
    def pathInfo(self, url):
        '''
        截取2位， 第一位为DB，第二位为Table
        '''
        return url.split('/');
        
    
        
class Query(Base.Handler):
    def get(self):
        print "callback: " + self.get_argument("_code_",'404');
        



        
        
        
        