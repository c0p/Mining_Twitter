import string
import twitter
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn


api = twitter.Api(consumer_key='FILL-ME-IN',
  consumer_secret='FILL-ME-IN',
  access_token_key='FILL-ME-IN',
  access_token_secret='FILL-ME-IN')



FRIENDLY_WORD_CLASS = {
    "n": "Noun",
    "v": "Verb",
    "a": "Adjective",
    "s": "Adjective Satellite",
    "r": "Adverb"
}

TRUMP_TWEET = (
    'fake news as always'
    'china is probably fake news'
    'all this isis stuff, fake news as always'
    'crooked hillary at it again with the fake news!'
    'false advertising. fake!'
    'the deal with iran is fake!'
    'luckily, all the fake news is gone'
)

# 1. Tokenize Words
words = nltk.word_tokenize(TRUMP_TWEET)

#print(words)
# 2. Generate a list of stop words (e.g. and, or, at, for)
stop_words = stopwords.words('english') + list(string.punctuation) + ['“','”']
# 3. Cleanse tokenized list of words
filtered_words = [word for word in words if word not in stop_words]

#print(filtered_words)

counted_words = Counter(filtered_words)

print(counted_words)



def get_word_class(word):
    """
    Get World Class
    """
    # Initialise the Word Class variable
    word_class = None
    
    # Proceed if the word exists in the data package
    if len(wn.synsets(word)) > 0:
        # Get word class
        word_class = wn.synsets(word)[0].pos()
        # Convert word class key to friendly text
        word_class = FRIENDLY_WORD_CLASS[word_class]
    else:
        pass

    # Return Word Class
    return word_class

for word, count in counted_words.most_common():
    word_class = get_word_class(word)
    row = [word, count, word_class]
    print(row)

