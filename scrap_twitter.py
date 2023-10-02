import tweepy
import snscrape.modules.twitter as sntwitter

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API key", "API secret key")
auth.set_access_token("Access token", "Access token secret")


# Create API object
api = tweepy.API(auth)

# Define the search term and the date_since date as variables
search_words = "example"
date_since = "2022-01-01"

# Collect tweets using Tweepy
tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since_id=date_since).items(5)

# Collect tweets using Snscrape
tweets = sntwitter.TwitterSearchScraper(search_words + ' since:' + date_since + ' lang:en').get_items()

# Print the tweets
for tweet in tweets:
    print(tweet.content)
