from auth import *
import json
import tweepy

# Return information of user
# print(api.get_user('sergiodxa'))

# Return information of my user
# print(api.me())

# Followers
# print(api.followers('sergiodxa'))

# 1052298712960126987
info = api.home_timeline('1052298712960126987')
status = info[0]
response = json.dumps(status._json)
response = json.loads(response)
print(response['created_at'])
