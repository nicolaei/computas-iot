import tweepy

def find_hashtag(hashtag='#iot_uio', tid):
    # SETUP, only works with the twitter account gruvebarn
    CONSUMER_KEY = 'GwfNRjFAc98ALxBU55X7RL9jp'
    CONSUMER_SECRET = '058qFhSL87dsShwE5OgnCSRCmimuZrIOKPWmAFB3XGQNcI2Oer'
    ACCESS_KEY = '778979158684790784-7x6Hk296CEpA4vN3f3iD0sye8a26C1z'
    ACCESS_SECRET = '1eIWU8fsmiJ1GeJNxakMhMZkHN8VcAQR8qhUYsw112Iuf'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    # Search for hashtag
    search_text = hashtag
    search_result = api.search(search_text)
    
    for i in search_result:
        if i.created_at > tid:
            return True
    return False
