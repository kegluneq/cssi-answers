import webapp2
import os
import jinja2
# You need base64 to send the image to HTML as a string the browser can
# understand
import base64
from google.appengine.api import users
from google.appengine.ext import ndb
from models import Visitor

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Gets a key for the provided logged-in user.
def get_key(me):
    return ndb.Key('Visitor', me.user_id())

# Returns the Visitor object associated with the logged-in user.
# If there is no user logged in, returns None.
def get_visitor():
    me = users.get_current_user()
    if not me:
        return None
    my_key = get_key(me)
    return my_key.get()

class MyHandler(webapp2.RequestHandler):
    def get(self):
        me = users.get_current_user()
        if not me:
            # No user is logged in, send them to the welcome page.
            start_template = jinja_current_dir.get_template("templates/welcome.html")
            jinja_values = {
                'signin_page_url': users.create_login_url('/')
            }
            self.response.write(start_template.render(jinja_values))
        else:
            # A user is logged in
            my_visitor = get_visitor()
            if not my_visitor:
                # If we don't have an entry in DataStore for this user, add one.
                my_visitor = Visitor(
                    key = get_key(me),
                    id = me.user_id(),
                    name = me.nickname(),
                    email = me.email(),
                )
                # We only save if we're creating a new one because we don't
                # modify existing Visitor objects.
                my_visitor.put()

            withuser_template = jinja_current_dir.get_template("templates/withuser.html")
            jinja_values = {
                'name': me.nickname(),
                'email_addr': me.email(),
                'user_id': me.user_id(),
                'signout_page_url': users.create_logout_url('/'),
            }
            if my_visitor.image:
                # base64.b64encode converts the BlobProperty image
                # into a string the browser knows how to show as an image.
                # See withuser.html for the <img> code needed to show a string
                # as an image.
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
    ('/', MyHandler),
], debug=True)
