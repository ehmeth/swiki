"""[ main.py ]
Main handler file
"""

DEBUG = False

import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Signup(Handler):
    def get(self):
        self.write("Signup!")

class Login(Handler):
    def get(self):
        self.write("Login!")

class Logout(Handler):
    def get(self):
        self.write("Logout!")

class WikiPage(Handler):
    def get(self, entry):
        self.write("%s WikiPage!" % entry)

class EditPage(Handler):
    def get(self, entry):
        self.write("%s EditPage!" % entry)

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
app = webapp2.WSGIApplication([('/signup', Signup),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/_edit' + PAGE_RE, EditPage),
                               (PAGE_RE, WikiPage),
                               ],
                               debug=DEBUG)

