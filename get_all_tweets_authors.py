import os
import json

if os.path.exists("json-files/all_tweets_authors.json"):
    f = open("json-files/all_tweets_authors.json", "r")
    authorsJson = f.read()
    authors = json.loads(authorsJson)
else:
    f = open("json-files/tweets.json", "r")
    allTweetsJson = f.read()
    allTweets = json.loads(allTweetsJson)

    authors = []
    for key, tweet in enumerate(allTweets) :
        username = tweet['username']
        author = {
            'username': username,
            'screen_name': username
        }
        if author not in authors :
            authors.append(author)

authors = sorted(authors, key=lambda i: i['screen_name'].lower())
authorsJson = json.dumps(authors, sort_keys=True, indent=4)

f = open("json-files/all_tweets_authors.json", "w")
f.write(authorsJson)
f.close()
