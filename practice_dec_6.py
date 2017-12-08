from nltk.corpus import stopwords
import nltk
import string
from nltk.tokenize import word_tokenize

print(type(string.punctuation))
stpwords = set(stopwords.words('english'))
print(stpwords)

words = word_tokenize('tweet asd a sd asd d')
print(type(words))


l = ' '.join(word.lower() for word in ['words', 'are', "but", 'my'] if word not in stpwords
             and word not in string.punctuation and word not in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
print(l)
