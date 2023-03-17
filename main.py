from Producer.stream import CustomStream
from utils.twitter_credentials import bearer_token
from utils.kafka_config import brokers
from Consumer.consumer import KafkaConsumer

topic= 'covid19'
hashtags = ['#covid19']
    
#start stremaing tweets
# stream = CustomStream(bearer_token, hashtags, topic)
# stream.filter()

##Initialize the consumer
consumer = KafkaConsumer(f'org.tweets.{topic}',True)
consumer.consume()
