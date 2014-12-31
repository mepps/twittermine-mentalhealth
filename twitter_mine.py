import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = './twitter_mentalhealth.json'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

print "tweets data length"
print len(tweets_data)

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)

def word_in_text(word, text):
	word = word.lower()
	text = text.lower()
	match = re.search(word, text)
	if match:
		return True
	return False


disorders = ['bipolar', 'depression', 'schizophrenia', 'anxiety']

#uncomment this code to allow manual input of text to search for
# disorders = []

# input = raw_input('Add a term for comparison. To stop enter "done".\n')
# while input.lower() != "done":
# 	disorders.append(input.lower())
# 	input = raw_input('Add a term for comparison. To stop enter "done".\n')

count = {}

tweets_by_disorder = {}

for disorder in disorders:
 tweets[disorder] = tweets['text'].apply(lambda tweet: word_in_text(disorder, tweet))
 count[disorder] = tweets[disorder].value_counts()[True]

tweets_by_disorder = pd.Series(count)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Disorder', fontsize=16)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Disorders', fontsize=15,fontweight='bold')
tweets_by_disorder.plot(ax=ax, kind='bar', color='red')

plt.show()
