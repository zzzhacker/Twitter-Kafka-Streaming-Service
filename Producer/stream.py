from Producer.producer import KafkaProducer
import tweepy
import json


#Create a class to listen to tweets
class CustomStream(tweepy.StreamingClient):
    def __init__(self,auth,hashtags,topic):
        super().__init__(auth)
        self.hashtgas = hashtags
        self.rules = [tweepy.StreamRule('#covid19', tag=topic) for hashtag in hashtags]## Create a rules for the stream
        self.topic_name = f'org.tweets.{topic}'
        self.producer = KafkaProducer(self.topic_name)
        self.add_rules(self.rules)

    def on_data(self, data):
        data = json.loads(data)['data']
        if 'text' in data:
            print(data['text'])
    def on_connect(self):
        print("You are now connected to the streaming API.")


