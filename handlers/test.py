# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from tornado.web import RequestHandler
from tornado.web import asynchronous

from handlers.base import TemplateHandler


class MainHandler(RequestHandler):
    @asynchronous
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
        self.finish()

    def post(self):
        self.set_header('Content-Type', 'text/plain')
        self.write('You wrote ' + self.get_argument('message'))


class HelloHandler(TemplateHandler):
    template_name = 'hello.html'

    def get_context_data(self, **kwargs):
        items = [
            'Item 1',
            'Item 2',
            'Item 3'
        ]
        title = self.get_argument('title', 'Hello')
        context = {
            'title': title,
            'items': items
        }
        return context


class StoryHandler(RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)





