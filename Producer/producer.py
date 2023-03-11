#import libraries for confludent kafka prodcer and twiteer api
from confluent_kafka import Producer    
import tweepy
import json
import time
import os
import sys

bearer_token = 'AAAAAAAAAAAAAAAAAAAAABCQmAEAAAAAU7jmV4Wvkh120%2F3xRgrAH4yThYI%3Dibi13EbftCc2Ds5Bm7Adiz0XWBd9esWyn2Niwy079L2Lu4Dn1d'

#Create a class to listen to tweets
class CustomStream(tweepy.StreamingClient):
    def on_data(self, data):
        print(data)
    def on_connect(self):
        print("You are now connected to the streaming API.")
    
#start stremaing tweets
stream = CustomStream(bearer_token)

# create a rule
rule1 = tweepy.StreamRule('#covid19', tag='covid19')
stream.add_rules([rule1])
stream.filter()

# #Create a kakfa Producer class to listen to tweets using poll method
# class KafkaProducer(object):
#     def __init__(self, topic_name):
#         self.topic_name = topic_name
#         self.producer = Producer({'bootstrap.servers': 'localhost:9092'})
#     def produce(self, data):
#         try:
#             self.producer.produce(self.topic_name, data.encode('utf-8'))
#             self.producer.poll(0)
#         except BufferError:
#             sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again')

    