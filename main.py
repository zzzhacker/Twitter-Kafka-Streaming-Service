from Producer.stream import CustomStream
from utils.twitter_credentials import bearer_token
from utils.kafka_config import brokers
from Consumer.consumer import KafkaConsumer, AvroKafkaConsumer

topic= 'covid19'
hashtags = ['#covid19']
    
#start stremaing tweets
# stream = CustomStream(bearer_token, hashtags, topic,avro=True,schema_name='tweet_value.avsc')
# stream.filter()

#Initialize the consumer
consumer = AvroKafkaConsumer(f'org.tweets.avro.{topic}',True,schema_path='avro_schemas/tweet_value.avsc')
consumer.consume()
