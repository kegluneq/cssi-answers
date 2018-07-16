#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-

#from __future__ import unicode_literals

from bs4 import BeautifulSoup
from urllib2 import urlopen

inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

moana_movie = {
    "title": "Moana",
    "id": "tt3521164",
    "year_released": 2016,
    "rating": "PG",
    "score": 7.6,
    "out_of": 10,
    "reviews": 195168
}

qos_movie = {
    "title": "Qantum of Solace",
    "id": "tt3521164",
    "year_released": 2008,
    "rating": "PG-13",
    "score": 6.6,
    "out_of": 10,
    "reviews": 364036
}

# Do not edit the code above!


# Write your code below to update the information in accordance with its
# IMDB page:


def solution1(dict):
    dict['year_released'] = 2015
    dict['score'] = 8.2
    dict['reviews'] = 488465
    dict['genres'] = ['Animation','Adventure','Comedy']
    dict.pop("out_of")
    print(dict)
    return dict


inside_movie = solution1(inside_movie)

def solution2(dict1, dict2):
    dict1['genres'] = ['Animation','Adventure','Comedy']
    dict1.pop("out_of")
    dict2['genres'] = ['Action', 'Adventure','Thriller']
    dict2.pop("out_of")
    print(dict1)
    print(dict2)
    return [dict1, dict2]

sol2 = solution2(moana_movie, qos_movie)
moana_movie = sol2[0]
qos_movie = sol2[1]

movies = [inside_movie, moana_movie, qos_movie]

user_genre = raw_input("What genre would you like to search for? ")

def genre_search(ug):
    top_score = 0
    top_movie = ""
    for movie in movies:
        if ug in movie['genres']:
            if movie['score'] > top_score:
                top_score = movie['score']
                top_movie = movie['title']
    return top_movie

print(genre_search(user_genre))





"""
def movieUpdate(mov_dict):
    url = 'https://www.imdb.com/title/' + mov_dict["id"] + '/'
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    real_title = soup.find(itemprop='name').get_text().split('(')[0].strip()
    real_year = soup.find(itemprop='name').get_text().split('(')[1].split(')')[0]
    real_rating = str(soup.find(itemprop="contentRating")).split("=")[1].split(' ')[0].strip('/"')
    real_score = soup.find(itemprop = "ratingValue").get_text()
    real_reviews = soup.find(itemprop = "ratingCount").get_text()
    genres = soup.findAll(itemprop = "genre", limit = 3)
    real_genres = []
    for tag in genres:
        genre = tag.get_text()
        real_genres.append(genre)

    mov_dict['title'] = real_title
    mov_dict['year_released'] = real_year
    mov_dict['rating'] = real_rating
    mov_dict['score'] = real_score
    mov_dict['reviews'] = real_reviews
    mov_dict['genre_types'] = real_genres
    mov_dict.pop("out_of")

    return(mov_dict)

print(movieUpdate(inside_movie))
"""
