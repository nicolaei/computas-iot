import tweepy, configparser, time
from datetime import datetime

class Tweeto:

    def __init__(self):
        # Authentication, see tweepy docs
        config = configparser.ConfigParser()
        config.read('auth')
        config_twit = config['twitter']
        
        self.CONSUMER_KEY = config_twit['CONSUMER_KEY']
        self.CONSUMER_SECRET = config_twit['CONSUMER_SECRET']
        self.ACCESS_KEY = config_twit['ACCESS_KEY']
        self.ACCESS_SECRET = config_twit['ACCESS_SECRET']

        self.auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        self.api = tweepy.API(auth_handler=self.auth, wait_on_rate_limit=True,\
                              wait_on_rate_limit_notify=True)
    
    def find_new_hashtag(self, hashtag='#iot_uio', tid=datetime.now()):
        # Search for hashtag
        search_text = hashtag

        search_result = self.api.search(search_text)
        
        # Return hashtag newer than in arg tid
        for i in search_result:
            if i.created_at > tid:
                return True
        return False

    def post_update(self, update_text):
        self.api.update_status(update_text)
