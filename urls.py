# -*- coding: utf-8 -*-

import tornado.web
from handlers.test import MainHandler
from handlers.test import HelloHandler
from handlers.test import StoryHandler
from handlers.shopping_cart import ShoppingCart
from handlers.shopping_cart import CartDetailHandler
from handlers.shopping_cart import CartHandler
from handlers.shopping_cart import StatusHandler
from settings import settings


urls = [
    (r'/', MainHandler),
    (r'/hello', HelloHandler),
    (r'/story/(\d+)', StoryHandler),
    (r'/cart', CartHandler),
    (r'/cart/detail', CartDetailHandler),
    (r'/cart/status', StatusHandler),
]

# application = tornado.web.Application(urls, **settings)


class Application(tornado.web.Application):
    def __init__(self):
        self.shopping_cart = ShoppingCart()

        tornado.web.Application.__init__(self, urls, **settings)

application = Application()