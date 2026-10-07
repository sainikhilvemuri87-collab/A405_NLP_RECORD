import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = input("Enter a sentence: ")

tokens = word_tokenize(sentence)

tagged_words = pos_tag(tokens)

print("\nPart-of-Speech Tagged Sentence")
print("-" * 40)

for word, tag in tagged_words:
    print(f"{word:<15} {tag}")
