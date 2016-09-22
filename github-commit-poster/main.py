#!/bin/python3
import time
from light_switch import Switch
from tweet_bot import Tweeto
from datetime import datetime

if __name__ == "__main__":

    switch = Switch("admin", "WelcometoCX01", "10.0.1.11", "6-0-37")

    newest_time = datetime.now()
    tweeto = Tweeto()

    while True:
        time.sleep(5)
        try:
            tweet_time = tweeto.find_new_hashtag(hashtag='#coffee_iot', tid=newest_time)
            
            if tweet_time:
                newest_time = datetime.now()
                
                switch.on()
                time.sleep(60*3)
                switch.off()
                
                tweeto.post_update("Coffee is ready!")
                print("posted new update")
        except TweepError:
            continue
