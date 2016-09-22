import tweepy, configparser

def find_hashtag(hashtag='#iot_uio', tid='0'):
    # SETUP, see auth property file
    config = configparser.ConfigParser()
    config.read('auth')
    config_twit = config['twitter']
    
    CONSUMER_KEY = config_twit['CONSUMER_KEY']
    CONSUMER_SECRET = config_twit['CONSUMER_SECRET']
    ACCESS_KEY = config_twit['ACCESS_KEY']
    ACCESS_SECRET = config_twit['ACCESS_SECRET']
    
    # Authentication, see tweepy docs
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    # Search for hashtag
    search_text = hashtag
    search_result = api.search(search_text)

    # Return hashtag newer than in arg tid
    for i in search_result:
        if i.created_at > tid:
            return True
    return False
