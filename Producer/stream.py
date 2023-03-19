from Producer.producer import KafkaProducer, AvroKafkaProducer
import tweepy
import json
import os


#Create a class to listen to tweets
class CustomStream(tweepy.StreamingClient):
    def __init__(self,auth,hashtags,topic,avro=False,schema_name=None):
        super().__init__(auth)
        self.hashtgas = hashtags
        self.rules = [tweepy.StreamRule('#covid19', tag=topic) for hashtag in hashtags]## Create a rules for the stream
        if avro:
            schema_path = f"avro_schemas/{schema_name}"
            self.topic_name = f'org.tweets.avro.{topic}'
            self.producer = AvroKafkaProducer(self.topic_name, schema_path)
        else:
            self.topic_name = f'org.tweets.{topic}'
            self.producer = KafkaProducer(self.topic_name)
        self.add_rules(self.rules)

    def on_data(self, data):
        data = json.loads(data)['data']
        self.producer.produce(data['text'])
        print(f"Tweet Prodcued: {data}")
    def on_connect(self):
        print("You are now connected to the streaming API.")


