# encoding=utf-8

import os
import sys
import wsgiref.handlers
import webapp2


from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import handlers

config = {}
config['webapp2_extras.i18n'] = {
    'translations_path': 'path/to/my/locale/directory',
}

application = webapp2.WSGIApplication(handlers.handlers, config=config)


sys.path.insert(0, os.path.dirname(__file__))
template.register_template_library('templatetags.filters')
