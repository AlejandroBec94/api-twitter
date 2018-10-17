from auth import *

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
    # print (tweet.text)

user = api.get_user('AlejandroBec3')
print (user.screen_name)
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)