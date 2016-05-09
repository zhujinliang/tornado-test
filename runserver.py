# -*- coding: utf-8 -*-

from tornado import ioloop
from tornado.options import define
from tornado.options import options
from tornado.options import parse_command_line
from urls import application

define('port', default=8888, type=int, help='Run on the given port!')

if __name__ == '__main__':
    parse_command_line()
    application.listen(options.port)
    print 'Tornado web server is runing on 127.0.0.1:%s' % options.port
    ioloop.IOLoop.instance().start()