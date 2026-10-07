from nltk.tokenize import sent_tokenize, word_tokenize

text = "Every small step you take today brings you closer to your goals."
print(sent_tokenize(text))
print(word_tokenize(text))
for i in word_tokenize(text):
    print(i)
