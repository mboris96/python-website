#!/usr/bin/env python
"""This script creates a 'Hello World' website on http://localhost:8080"""
import web

URLS = (
    '/', 'Index'
)

APP = web.application(URLS, globals())

RENDER = web.template.render('templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World!"
        return RENDER.index(greeting=greeting)

if __name__ == "__main__":
    APP.run()
