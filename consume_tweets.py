from Consumer.consumer import KafkaConsumer, AvroKafkaConsumer


topic= 'covid19'
#Initialize the consumer
consumer = AvroKafkaConsumer(f'org.tweets.avro.{topic}',True,schema_path='avro_schemas/tweet_value.avsc')
consumer.consume()