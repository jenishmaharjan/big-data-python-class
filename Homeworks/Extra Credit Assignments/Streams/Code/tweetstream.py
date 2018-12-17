#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy.auth import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1059593980374142981-t4guYC1q6o8RUpSzw3CIbgyHZ3XOkB"
access_token_secret = "o2qBxUrAzu2HU5d60bb6vXpeDkJSUD39pSs5bhmnBfJ0K"
consumer_key = "PeQ7nqZbgkDsLPYwUhZnCVmEc"
consumer_secret = "StESHDuT5ojw4hkeN6SCS3g6bn2graXr4X1PPUiqtz1oxewsp8"

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        
        #file=open("TweetOut.txt","a")
        #file.write(data)
        print(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

      # This line filter Twitter Streams to capture data by the keywords: 'Tesla', 'Stock'

    stream.filter(track=['Tesla', 'SpaceX','Elon','Musk'])