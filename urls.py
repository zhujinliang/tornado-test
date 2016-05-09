# -*- coding: utf-8 -*-

from tornado.web import Application

from handlers import MainHandler
from handlers import HelloHandler
from handlers import StoryHandler
from settings import settings


urls = [
    (r'/', MainHandler),
    (r'/hello', HelloHandler),
    (r'/story/(\d+)', StoryHandler),
]

application = Application(urls, **settings)