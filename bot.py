# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import tweepy
from config import consumer_key, consumer_secret, access_key, access_secret
import protect_secret as ps

class Bot(tweepy.streaming.StreamListener):
    """
    Public Timelineを監視
    適当なツイートを秘密保護してぱくつい
    """
    def __init__(self):
        super(Bot, self).__init__()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth_handler = auth, api_root = '/1.1', secure = True)
        self.next_time = datetime(2000, 1, 1)

    def on_status(self, tweet):
        lang = getattr(tweet, 'lang', u'')
        if lang != u'ja':
            return
        if datetime.now() > self.next_time:
            self.tweet_tekito(tweet.text)

    def tweet(self, text):
        try:
            self.api.update_status(text)
            print text
        except tweepy.error.TweepError:
            print 'ついーとえらーだって'
        print

    def run(self):
        stream = tweepy.Stream(self.api.auth, listener = self, retry_count = 10, retry_time = 60.0)
        try:
            stream.sample()
        except KeyboardInterrupt:
            pass

    def tweet_tekito(self, text):
        self.next_time = datetime.now() + timedelta(seconds = 30)
        protected = ps.protect_secret(text)
        self.tweet(protected)


if __name__ == '__main__':
    Bot().run()

