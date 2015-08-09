# Social-Art-Feed
The Social Art Feed is designed to pull targetted livestream information from twitter and build a webpage out of the results. 

<hr>

## Requirements
Social-Art-Feed uses the following:
Python 2.7.6 (may work with other versions but this is what I tested with)
Tweepy (To get Tweepy check out <a href:="https://github.com/tweepy/tweepy">https://github.com/tweepy/tweepy</a>)

<hr>

## Setup
Tweepy Config Set-Up:
- Sign into Twitter (<a href="https://twitter.com"> Twitter </a>)
- Go to <a href="https://apps.twitter.com/"> https://apps.twitter.com/ </a>
- Choose to create a new app
- Authorize said application for your own account
- Go to the applications Keys and Access Tokens Page and you will need to get you Access Token, Access Secret, Consumer Token, and Consumer Secret. (Please note keep these private as they can be used to control your Twitter acount)
- Open the Config.txt file and plug in the information:
```
CONSUMER_KEY:your_consumer_key
CONSUMER_SECRET:your_consumer_secret
ACCESS_KEY:your_access_key
ACCESS_SECRET:your_access_secret
```
(Important when switching out the information in this file don't put in a space after the colon)

Application Configuration:
- Defining Search terms for LiveStream
-- Add desired search filters to look for in the data stream
```
    # Filter Data here
    stream.filter(track=['#happy', '#life', '#love'])
```
(Each term is closed in using ' and seperated with , so here you see by default we are looking for post containing #happy, #life, and #love)
- Build the filter file which contains which terms to exclude.
-- Open filter.txt and add what you would like to filter out with each one on it's own line.
```
retweeted_status
#FOLLOWTRICK
bieber
quoted_status
```
(You can also put in the json parameters from Twitter like "possibly_sensitive":true to block many adult post. Some will get through if the user isn't using Twitter properly.)
<hr>
