#!/usr/bin/python

#https://dev.twitter.com/rest/reference/get/users/search

from twitter import *

twitter = Twitter(auth = OAuth('512739542-yp06o7mXg6Yrexxz7zdGqpETL5k44PxOYhVKN2bw',
                               'cw9Z5PeK5YG7zuDtXpUZD40Apf2VFrUMo1XzWUHN6dn7F',
                               'D8XxzNAHM6uUPRlnQJUIYDhex',
                               'bubnRJsyEVFchIzY4078GgrUCEZCtPgR83VKctSwYajurpHOrb'))

users = []

# number of pages to generate (20 users per page)
for i in range(1, 5):
    # some sort of query... figure out the best thing here
    # could just query from out set of gender labels...
    # as far as I can tell this queries from anywhere in user information?
    results = twitter.users.search(q = '"neymar"', page = i)
    for user in results:
        # can add/remove from this set of features
        userData = [user["screen_name"], user["name"], user["id_str"], user["location"], user["lang"], user["description"]]
        users.append(userData)