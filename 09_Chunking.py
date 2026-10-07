import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = input("Enter a sentence: ")

tokens = word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)

grammar = r"""
NP: {<DT>?<JJ>*<NN.*>+}
"""

chunk_parser = nltk.RegexpParser(grammar)

chunk_tree = chunk_parser.parse(tagged)

print("\nPOS Tagged Sentence")
print(tagged)

print("\nChunk Tree")
print(chunk_tree)

chunk_tree.draw()
