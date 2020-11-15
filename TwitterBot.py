import tweepy
import time

auth = tweepy.OAuthHandler('************************************','****************************************')
auth.set_access_token('**************************************', '****************************************')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search1 = '#Python #ML #DataScience'
search2 = '#CyberSecurity #Azure #AWS'
search3 = '#Flutter #GoLang'
search4 = '#Redhat #Linux'
nrTweets = 100
likeCount = 0
retweetCount = 0

for tweet in tweepy.Cursor(api.search, search1).items(nrTweets):
    try:
        tweet.favorite() #Liked a tweet
        likeCount += 1
        print()
        print('Like Count: ' + str(likeCount))
        time.sleep(5)
        tweet.retweet() # retweets a tweet
        retweetCount += 1
        print('Retweet Count: ' + str(retweetCount))
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
