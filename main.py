#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('fakebook')

class FakebookHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('profil na fakebooku')

app = webapp2.WSGIApplication([
    ("/", MainHandler)
    ('/fejstbok', FakebookHandler),
], debug=True)
#GAE_prva

