import GetOldTweets3 as got
import sys
import re
import jsonpickle

if len(sys.argv) == 2:
    searchQuery = sys.argv[1]
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(searchQuery).setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    tweet = tweet[0]

    pattern = "^\s*\[?(\d+)\]?\s+"
    match = re.search(pattern, tweet.text)
    if match != None:
        day = int(match.group(1))
        tweet.day = day
    else:
        tweet.day = -1
    
    jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    tweetJson = jsonpickle.encode(tweet, unpicklable=False)
    print(tweetJson)

else:
    print("insert the query string as argument of the script on the CLI")


