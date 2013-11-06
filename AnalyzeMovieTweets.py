from textblob import TextBlob

tweet = TextBlob(" If Krrish 3 is anything to go by, I'm not sure I ever want children")

print(tweet.tags)
print('\n')

print(tweet.noun_phrases)
print('\n')

print(tweet.sentiment)
print('\n')
