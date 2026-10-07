from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example_words = "It is very important to be patiently while you are Python with Python, all my expenses have been published once"

for w in example_words:
    print(ps.stem(w))
