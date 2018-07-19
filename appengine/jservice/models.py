from google.appengine.ext import ndb

class JUser(ndb.Model):
    # user_id is part of the key
    nickname = ndb.StringProperty(required=True)
    email    = ndb.StringProperty(required=True)
    page_view_count = ndb.IntegerProperty(required=True)

    def add_page_view(self):
        self.page_view_count = self.page_view_count + 1

class Clue(ndb.Model):
    question = ndb.StringProperty(required=True)
    answer = ndb.StringProperty(required=True)
    category = ndb.StringProperty(required=True)
    category_id = ndb.IntegerProperty(required=True)
    value = ndb.IntegerProperty()

    def as_dictionary(self):
        count = UserFavorite.query(UserFavorite.clue==self.key).count()
        return {
          'value': self.value,
          'question': self.question,
          'answer': self.answer,
          'id': self.key.id(),
          'category': {
             'title': self.category,
             'id': self.category_id
          },
          'count': count
        }

class UserFavorite(ndb.Model):
    # parent of the JUser
    clue = ndb.KeyProperty(required=True, kind=Clue)
