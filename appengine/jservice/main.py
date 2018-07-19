import logging
import os
import jinja2
import webapp2
import json
import urllib2
from google.appengine.api import urlfetch
from google.appengine.api import users
from google.appengine.ext import ndb
from models import JUser, Clue, UserFavorite

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))


@ndb.transactional
def find_or_create_user():
    user = users.get_current_user()
    if user:
        key = ndb.Key('JUser', user.user_id())
        juser = key.get()
        if not juser:
            juser = JUser(key=key,
                          nickname=user.nickname(),
                          email=user.email(),
                          page_view_count=0)
        juser.add_page_view()
        juser.put()
        return juser;
    return None

@ndb.transactional
def save_clue(clue):
    key = ndb.Key('Clue', str(clue['id']))
    if not key.get():
        Clue(key=key,
             question = clue['question'],
             answer = clue['answer'],
             category = clue['category']['title'],
             category_id = clue['category']['id'],
             value = clue['value']).put()

def get_log_inout_url(user):
    if user:
        return users.create_logout_url('/')
    else:
        return users.create_login_url('/')

@ndb.transactional
def add_user_favorite(juser, id):
    key = ndb.Key(juser.key.kind(), juser.key.id(),
                  'UserFavorite', id)
    favorite = key.get()
    if not favorite:
        UserFavorite(key=key, clue=ndb.Key('Clue', id)).put()

@ndb.transactional
def remove_user_favorite(juser, id):
    ndb.Key(juser.key.kind(), juser.key.id(),
            'UserFavorite', id).delete()

class AddFavorite(webapp2.RequestHandler):
    def get(self):
        user = find_or_create_user()
        if not user:
          self.redirect("/?error=nouser")
          return

        quest_id = self.request.get('id')
        add_user_favorite(user, quest_id)

        self.redirect("/favorites")


class RemoveFavorite(webapp2.RequestHandler):
    def get(self):
        user = find_or_create_user()
        if not user:
          self.redirect("/?error=nouser")
          return

        remove_user_favorite(user, self.request.get('id'))
        self.redirect('/favorites')


class ListFavorites(webapp2.RequestHandler):
    def get(self):
        user = find_or_create_user()
        if not user:
          self.redirect("/?error=nouser")
          return
        log_url = get_log_inout_url(user)

        user_favs = UserFavorite.query(ancestor = user.key).fetch()
        favorites = [fav.clue.get().as_dictionary() for fav in user_favs]

        #for user_fav in user_favs:
        #    key = ndb.Key('Clue', user_fav.question_id)
        #    fav = key.get()
        #    print(fav)
        #    if fav:
        #        favorites.append(fav.as_dictionary())
        #    else:
        #        favorites.append(None)

        template = jinja_environment.get_template('favorites.html')
        variables = {'user': user,
                     'favorites': favorites,
                     'log_url': log_url}
        self.response.out.write(template.render(variables))

class MainPage(webapp2.RequestHandler):
    def get(self):
        message = None
        if self.request.get('error'):
            if self.request.get('error') == 'nouser':
                message = 'You must be logged in to do that.'

        user = find_or_create_user()
        log_url = get_log_inout_url(user)

        response = urlfetch.fetch("http://jservice.io/api/random?count=1")
        clue = json.loads(response.content)[0]

        # if the user is logged in, we'll save the clue
        if user:
            save_clue(clue)

        template = jinja_environment.get_template('main.html')
        variables = {'clue': clue,
                     'user': user,
                     'log_url': log_url,
                     'error': message}
        self.response.out.write(template.render(variables))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/remove', RemoveFavorite),
    ('/favorite', AddFavorite),
    ('/favorites', ListFavorites),
], debug=True)
