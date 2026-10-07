import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

print("\nOriginal Tokens")
print(tokens)

print("\nUnigrams")
for gram in ngrams(tokens, 1):
    print(gram)

print("\nBigrams")
for gram in ngrams(tokens, 2):
    print(gram)

print("\nTrigrams")
for gram in ngrams(tokens, 3):
    print(gram)
