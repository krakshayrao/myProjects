import tweepy
import time
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
count=1

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    	f_read = open(file_name, 'r')
    	last_seen_id = int(f_read.read().strip())
    	f_read.close()
    	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
    	f_write.write(str(last_seen_id))
    	f_write.close()
    	return

def reply_to_tweets():
    	print('retrieving and replying to tweets...')
    	last_seen_id = retrieve_last_seen_id(FILE_NAME)
    	searched=api.search(q='Kannad',since_id=last_seen_id,tweet_mode='extended')

	for searchedResult in reversed(searched):
	if(searchedResult.text[0]!='R' and searchedResult.text[1]!='T'):
		print(str(searchedResult.id)+'-'+searchedResult.text+'/'+searchedResult.lang)

        last_seen_id = searchedResult.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'kannad' in searchedResult.full_text.lower():
            print('found Kannad!')
            print('responding back...')
            api.update_status('@' + searchedResult.user.screen_name +
                    'Hi! I am a bot. The actual spelling of Kannad is KannadA. There is an A in the end. Please pronounce it right when you use it next time. I have corrected '+count+' people till now. Thank you.!', searchedResult.id)
	    count++
while True:
    reply_to_tweets()
    time.sleep(300)







twts = api.search(q="Kannad")

#list of specific strings we want to check for in Tweets
t = [' Kannad ']

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)


for results in searchResults()
if(results.is_quote_status!=true)
{
print results.text
}