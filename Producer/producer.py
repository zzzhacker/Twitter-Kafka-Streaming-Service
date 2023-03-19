#import libraries for confludent kafka prodcer and twiteer api
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic   
from utils.kafka_config import *
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
#import schema registry client

from confluent_kafka import avro


import tweepy
import json
import time
import os
import sys


#Create a kakfa Producer class to listen to tweets using poll method
class KafkaProducer(object):
    def __init__(self, topic_name):
        self.topic_name = topic_name
        if self.check_topic_exists() is False:
            self.create_topic()
        else: print(f'Topic {self.topic_name} already exists')
        self.producer = Producer({'bootstrap.servers': brokers})

    def create_topic(self):
        client = AdminClient({'bootstrap.servers': brokers})
        futures = client.create_topics([NewTopic(topic=self.topic_name, num_partitions=3, replication_factor=2)])
        for topic, future in futures.items():
            try:
                future.result()
                print("Topic {} created".format(topic))
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))

    def check_topic_exists(self):
        client = AdminClient({'bootstrap.servers': brokers})
        topic_metadata = client.list_topics(timeout=5)
        return self.topic_name in set(t.topic for t in iter(topic_metadata.topics.values()))
    
    def produce(self, data):
        try:
            self.producer.produce(self.topic_name, data.encode('utf-8'))
            self.producer.poll(0)
        except BufferError:
            sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again')


## Create Prodcuer class with AvroSerializer and schemaregistryclient to listen to tweets
class AvroKafkaProducer(KafkaProducer):
    def __init__(self, topic_name, schema_path):
        self.topic_name = topic_name
        if self.check_topic_exists() is False:
            self.create_topic()
        else: print(f'Topic {self.topic_name} already exists')
        # Load Avro schema from .avsc file
        with open(schema_path, "r") as f:
            schema_str = f.read()

        # # Create Avro Schema object
        # self.schema = avro.loads(schema_str)
        # Connect to Schema Registry
        self.schema_registry_client = SchemaRegistryClient({"url": schema_registry_url})
        # Create Avro Serliazer
        self.avro_serializer = AvroSerializer(self.schema_registry_client, schema_str)

        self.producer = Producer({'bootstrap.servers': brokers})
    def produce(self, data):
        try:
            self.producer.produce(topic=self.topic_name, value=self.avro_serializer(data))
            self.producer.poll(0)
        except BufferError:
            sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' % len(self.producer))
        except Exception as e:
            print(e)
            sys.stderr.write('%% Exception while producing\n')
        self.producer.flush()



