import TwitterAPI import TwitterAPI

con_key = ''
con_secret = ''
access_token_key = ''
access_token_secret = ''

twitter = TwitterAPI(con_key, con_secret, access_token_key, access_token_secret)

request = twitter.request('search/tweets', {'q':'vancouver'})
for item in r:
	print item
