import TwitterAPI import TwitterAPI

#Add your twitter API keys https://dev.twitter.com
con_key = ''
con_secret = ''
access_token_key = ''
access_token_secret = ''

#Authenticate with Twitter
twitter = TwitterAPI(con_key, con_secret, access_token_key, access_token_secret)

#Print a simple tweet and return the status code
request = twitter.request('statuses/update', {'status':'A tweet from Vancouver'})
print request.status_code
