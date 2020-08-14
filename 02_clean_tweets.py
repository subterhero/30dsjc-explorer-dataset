import json
import re
import jsonpickle
import os

f = open("json-files/raw_tweets.json", "r")
allTweetsJson = f.read()

# allTweets = jsonpickle.decode(allTweetsJson)
allTweets = json.loads(allTweetsJson)

cleanedTweets = []
pattern = "^\s*\[?(\d+)\]?\s+"
for key, tweet in enumerate(allTweets) :
    match = re.search(pattern, tweet['text'])
    if match != None:
        day = int(match.group(1))
        tweet['day'] = day
        cleanedTweets.append(tweet)

if os.path.exists("json-files/tweets_integrations.json"):
    # gets the tweets to integrate
    f = open("json-files/tweets_integrations.json", "r")
    tweetIntegrationsJson = f.read()
    tweetIntegrations = json.loads(tweetIntegrationsJson)
    cleanedTweets = cleanedTweets + tweetIntegrations

print("extracted tweets: "+str(len(cleanedTweets)))

cleanedTweets = sorted(cleanedTweets, key=lambda i: i['day'])
tweetsJson = jsonpickle.encode(cleanedTweets, unpicklable=False)

f = open("json-files/tweets.json", "w")
f.write(tweetsJson)
f.close()
