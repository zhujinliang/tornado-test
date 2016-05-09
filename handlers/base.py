# -*- coding: utf-8 -*-

from tornado.web import RequestHandler


class TemplateMixin(object):
    template_name = None

    def get_template_name(self):
        if self.template_name is None:
            raise Exception('template_name is None!')

        return self.template_name


class TemplateHandler(TemplateMixin, RequestHandler):

    def get_context_data(self, **kwargs):
        return {
            'params': kwargs
        }

    def render_template(self, context):
        template_name = self.get_template_name()
        self.render(template_name, **context)

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.render_template(context)
