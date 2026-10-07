import nltk
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
nltk.download('punkt')

nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)

pos_tags = nltk.pos_tag(words)

full_form = {
    "NN": "Noun",
    "NNS": "Plural noun",
    "NNP": "Proper noun",
    "NNPS": "Proper plural noun",
    "VB": "Verb",
    "VBD": "Verb (Past)",
    "VBG": "Verb (Gerund)",
    "VBN": "Verb (Past participle)",
    "VBP": "Verb (Present)",
    "JJ": "Adjective",
    "JJR": "Comparative Adjective",
    "JJS": "Superlative Adjective",
    "RB": "Adverb",
    "RBR": "Comparative Adverb",
    "RBS": "Superlative Adverb",
    "DT": "Determiner",
    "IN": "Preposition",
    "PRP": "Pronoun",
    "TO": "To",
    "CC": "Conjunction"
}

print("\nWORD | POS TAG | FULL FORM")

for word, tag in pos_tags:
    print(f"{word} | {tag} | {full_form.get(tag, tag)}")
