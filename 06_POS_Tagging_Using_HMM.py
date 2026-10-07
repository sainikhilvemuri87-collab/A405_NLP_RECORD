import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print("\nPart-of-Speech Tags")
print("-" * 35)

for word, tag in tags:
    print(f"{word:<15} {tag}")
