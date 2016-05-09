# -*- coding: utf-8 -*_

import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

settings = {
    'debug': True,
    'serve_traceback': True,
    'template_path': os.path.join(PROJECT_PATH, 'templates'),
    'static_path': os.path.join(PROJECT_PATH, 'static'),
    'login_url': '/login',
    'xsrf_cookies': False,
}