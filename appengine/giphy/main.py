import jinja2
import webapp2
import os
import json
import urllib
import urllib2
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(
        os.path.dirname(__file__) + '/templates'))

class UserSearch(ndb.Model):
    term = ndb.StringProperty(required=True)
    count = ndb.IntegerProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now=True)

    def increment(self):
        self.count = self.count + 1


@ndb.transactional
def updateSearchCount(term):
    lterm = term.lower()
    # create key
    key = ndb.Key('UserSearch', lterm)
    # Read database
    search = key.get()
    if not search:
        # Create if not there
        search = UserSearch(key=key, count=0, term=term)
    # Update count
    search.increment()
    # Save
    search.put()

def getRecentSearches():
    return UserSearch.query().order(-UserSearch.created_at).fetch(limit=10)

def getPopularSearches():
    return UserSearch.query().order(-UserSearch.count).fetch(limit=10)

class RecentPage(webapp2.RequestHandler):
    def get(self):
        searches = getRecentSearches()

        template = jinja_environment.get_template('recent.html')
        variables = {'searches': searches}
        self.response.write(template.render(variables))

class PopularPage(webapp2.RequestHandler):
    def get(self):
        searches = getPopularSearches()

        template = jinja_environment.get_template('popular.html')
        variables = {'searches': searches}
        self.response.write(template.render(variables))


class MainPage(webapp2.RequestHandler):
    def get(self):
        search_term = self.request.get('q')
        if search_term:
            updateSearchCount(search_term)
        else:
            search_term = "dog"
        params = {'api_key': 'b2581db71e2847f79b8671b6f9f34d54',
                  'q': search_term,
                  'rating': 'g',
                  'limit': 10}
        form_data = urllib.urlencode(params)
        api_url = 'http://api.giphy.com/v1/gifs/search?' + form_data

        response = urllib2.urlopen(api_url)
        content = json.loads(response.read())

        gif_urls = []
        for img in content['data']:
            url = img['images']['downsized']['url']
            gif_urls.append(url)

        template = jinja_environment.get_template('main.html')
        variables = {'gif_urls': gif_urls,
                     'q': search_term}
        self.response.write(template.render(variables))

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/recent', RecentPage),
  ('/popular', PopularPage),
])
