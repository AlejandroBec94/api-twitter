import tweepy

consumer_key = 'J3Inz6C1B6HwJMaIVGOWt7SKV'
consumer_secret = '6k5eud1PQGVOvrvPeca2jBv3zu02oa7w5S4mEP3BOeDQVn5MMj'
access_token = '1052298712960126987-f3GUjhs5deEF3wBRgzVu47Dr4aOKx1'
access_token_secret = '5cY1SSR2TjseMpTTZ2qLb897S12GiiZgLQFl2rY3bwZe5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

