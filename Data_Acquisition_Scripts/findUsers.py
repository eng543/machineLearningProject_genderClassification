#!/usr/bin/python

#https://dev.twitter.com/rest/reference/get/users/search

from twitter import *
from tweepy import *
import time

twitter = Twitter(auth = OAuth('512739542-yp06o7mXg6Yrexxz7zdGqpETL5k44PxOYhVKN2bw',
                               'cw9Z5PeK5YG7zuDtXpUZD40Apf2VFrUMo1XzWUHN6dn7F',
                               'D8XxzNAHM6uUPRlnQJUIYDhex',
                               'bubnRJsyEVFchIzY4078GgrUCEZCtPgR83VKctSwYajurpHOrb'))

auth = OAuthHandler('D8XxzNAHM6uUPRlnQJUIYDhex', 'bubnRJsyEVFchIzY4078GgrUCEZCtPgR83VKctSwYajurpHOrb')
auth.set_access_token('512739542-yp06o7mXg6Yrexxz7zdGqpETL5k44PxOYhVKN2bw', 'cw9Z5PeK5YG7zuDtXpUZD40Apf2VFrUMo1XzWUHN6dn7F')

api = API(auth)

users = {}

# start with most informative queries
queries = ['mom', 'dad', 'mother', 'father', 'sister', 'brother', 'aunt', 'uncle', 'gramma', 'grampa', 'grandma', 'grandpa',
           'grandmother', 'grandfather', 'mama', 'momma', 'papa', 'male', 'female', 'girl', 'boy', 'man', 'woman',
           'trans', 'queer', 'gender', 'binary', 'fluid', 'andro',
           'eunuch', 'MTF', 'FTM', 'MTX', 'FTX']

query_sub = ['mother', 'father', 'male', 'female', 'girl', 'boy', 'man', 'woman', 'trans', 'gender']

wf = open("results.txt", "w")

# 50 pages per call (1000 total users)
page = 1
while True:
    try:
        results = twitter.users.search(q='"MTF"', page=page, count=20)
        if results:
            for user in results:
                if user["lang"] == "en":
                    users[user["id_str"].encode('utf-8')] = [user["location"].encode('utf-8'), user["lang"].encode('utf-8'), user["description"].encode('utf-8')]
                    user2 = {user["id_str"].encode('utf-8'): [user["location"].encode('utf-8'), user["lang"].encode('utf-8'), user["description"].encode('utf-8')]}
                    wf.write(str(user2))
                    wf.write("\n")
        else:
            break

        page += 1


    except TweepError: ## some error
        time.sleep(60 * 15)
        continue

    except StopIteration:
        break

#wf = open("results.txt", "w")
#for i in range(0, len(users)):
#    wf.write(i)
#    wf.write("\n")

wf.close()