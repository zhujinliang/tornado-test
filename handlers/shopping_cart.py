# -*- coding: utf-8 -*-

from uuid import uuid4
from tornado.web import asynchronous
from tornado.web import RequestHandler
from handlers.base import TemplateHandler


class ShoppingCart(object):
    total_inventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

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
        for c in self.callbacks:
            self.callback_helper(c)

        self.callbacks = []

    def callback_helper(self, callback):
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


class StatusHandler(RequestHandler):
    @asynchronous
    def get(self):
        self.application.shopping_cart.register(self.on_message)

    def on_message(self, count):
        self.write('{"inventoryCount": "%d"}' % count)
        self.finish()

