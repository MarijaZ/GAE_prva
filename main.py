#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello Marija!')

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('O nas')

app = webapp2.WSGIApplication([
    ("/", MainHandler)
    ('/about', AboutHandler),
], debug=True)
#GAE_prva
