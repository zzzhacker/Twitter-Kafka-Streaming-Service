from Producer.stream import CustomStream
from utils.twitter_credentials import bearer_token

topic= 'covid19'
hashtags = ['#covid19']
    
#start stremaing tweets
stream = CustomStream(bearer_token, hashtags, topic)
stream.filter()