import webapp2
import os
import jinja2
import base64
from google.appengine.api import users
from google.appengine.ext import ndb
from models import Visitor

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_visitor():
    me = users.get_current_user()
    if not me:
        return None
    my_key = ndb.Key('Visitor', me.user_id())
    return my_key.get()

class SigninHandler(webapp2.RequestHandler):
    def get(self):
        me = users.get_current_user()
        if not me:
            start_template = jinja_current_dir.get_template("templates/welcome.html")
            jinja_values = {
                'signin_page_url': users.create_login_url('/')
            }

            self.response.write(start_template.render(jinja_values))
        else:
            my_key = ndb.Key('Visitor', me.user_id())
            my_visitor = get_visitor()
            if not my_visitor:
                my_visitor = Visitor(
                    key = my_key,
                    id = me.user_id(),
                    name = me.nickname(),
                    email = me.email(),
                )
            my_visitor.put()

            withuser_template = jinja_current_dir.get_template("templates/withuser.html")
            jinja_values = {
                'name': me.nickname(),
                'email_addr': me.email(),
                'user_id': me.user_id(),
                'signout_page_url': users.create_logout_url('/'),
            }
            if my_visitor.image:
                jinja_values['img'] = base64.b64encode(my_visitor.image)

            self.response.write(withuser_template.render(jinja_values))

    def post(self):
        my_visitor = get_visitor()
        if my_visitor:
            img = self.request.get("myfile")
            my_visitor.image = img
            my_visitor.put()

        self.redirect('/')


app = webapp2.WSGIApplication([
    ('/', SigninHandler),
], debug=True)
