# -*- coding: utf-8 -*-

from uuid import uuid4
from tornado.web import asynchronous
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
from handlers.base import TemplateHandler


class ShoppingCart(object):
    total_inventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def move_item_to_cart(self, session):
        if session in self.carts:
            return None

        self.carts[session] = True
        self.notify_callbacks()

    def remove_item_from_cart(self, session):
        if session not in self.carts:
            return None

        del(self.carts[session])
        self.notify_callbacks()

    def notify_callbacks(self):
        for callback in self.callbacks:
            callback(self.get_inventory_count())

    def get_inventory_count(self):
        return self.total_inventory - len(self.carts)


class CartDetailHandler(TemplateHandler):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        session = uuid4()
        print 'session: ', session
        count = self.application.shopping_cart.get_inventory_count()
        context = {
            'session': session,
            'count': count
        }
        return context

class CartHandler(RequestHandler):
    def post(self):
        action = self.get_argument('action')
        session = self.get_argument('session')
        if not session:
            self.set_status(400)
            return None

        print 'In cart handler post'
        if action == 'add':
            self.application.shopping_cart.move_item_to_cart(session)
        elif action == 'remove':
            self.application.shopping_cart.remove_item_from_cart(session)
        else:
            self.set_status(400)


class StatusHandler(WebSocketHandler):
    def open(self):
        self.application.shopping_cart.register(self.callback)

    def on_close(self):
        self.application.shopping_cart.unregister(self.callback)

    def on_message(self):
        pass

    def callback(self, count):
        print 'Send message to websocket!'
        self.write_message('{"inventoryCount": "%d"}' % count)


