# import the tweepy library
import tweepy

# import the config file
import config

# create client with tweepy.Client with consumer key and secret and access token as arguments
client = tweepy.Client(consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET_KEY,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)


# create a  variable called tweet with a string that says 'I wrote this tweet with Copilot
tweet = "I wrote this tweet with Copilot"

# send a tweet with the client.create_tweet method and text as the argument. Save the result in a variable called response
response = client.create_tweet(text=tweet)

# print the response
print(response)