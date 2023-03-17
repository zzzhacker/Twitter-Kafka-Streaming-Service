import time
from confluent_kafka import Consumer
from utils.kafka_config import *
## create kafka consumer class to listen to tweets
class KafkaConsumer(object):
    def __init__(self, topic_name,start_from_beginning=False):
        self.topic_name = topic_name

        if start_from_beginning:
            self.consumer = Consumer({'bootstrap.servers': brokers, 'group.id': '0', 'auto.offset.reset': 'earliest'})
        else:
            self.consumer = Consumer({'bootstrap.servers': brokers, 'group.id': '0'})
        self.consumer.subscribe([self.topic_name])

        
        #check if successfully subscribed to topic
        topic_metadata = self.consumer.list_topics(topic=self.topic_name)
        if self.topic_name in set(t.topic for t in iter(topic_metadata.topics.values())):
            print(f'Successfully subscribed to topic {self.topic_name}')
        else:
            print(f'Failed to subscribe to topic {self.topic_name}')




    def consume(self):
        print('starting to consume messages from topic {}'.format(self.topic_name))
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                print('no message received by consumer')
            elif msg.error() is not None:
                print("error from consumer")
            else:
                print('consumed message {}'.format(msg.value().decode('utf-8')))
            time.sleep(1)