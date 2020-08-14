import GetOldTweets3 as got
import json
import jsonpickle

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#30DSJC')
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

tweetsJson = jsonpickle.encode(tweets, unpicklable=False)

f = open("json-files/raw_tweets.json", "w")
f.write(tweetsJson)
f.close()
