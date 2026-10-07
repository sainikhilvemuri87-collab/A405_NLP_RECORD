from nltk.stem import PorterStemmer

ps = PorterStemmer()

example_words = ["implement", "implements", "implemented",
                 "implementing"]

for w in example_words:
    print(ps.stem(w))
