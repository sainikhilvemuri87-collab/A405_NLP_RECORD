from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

s = "hold your breath till you touch one or two which is for"
words = word_tokenize(s)
stop_words = set(stopwords.words('english'))
non_stop_words = [word for word in words if word.lower() not in stop_words]
print(non_stop_words)
