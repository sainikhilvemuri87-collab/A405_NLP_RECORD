import nltk
from nltk.tag import hmm

training_data = [
    [
        ("The", "DET"),
        ("customer", "NOUN"),
        ("needs", "VERB"),
        ("help", "NOUN")
    ],
    [
        ("The", "DET"),
        ("user", "NOUN"),
        ("reports", "VERB"),
        ("problem", "NOUN")
    ],
    [
        ("A", "DET"),
        ("customer", "NOUN"),
        ("requests", "VERB"),
        ("support", "NOUN")
    ],
    [
        ("The", "DET"),
        ("agent", "NOUN"),
        ("provides", "VERB"),
        ("assistance", "NOUN")
    ]
]

trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(training_data)

sentence = input("Enter a customer message: ")

words = nltk.word_tokenize(sentence)
tagged_words = tagger.tag(words)

print("\nWord\tPOS Tag")
print("--------------------")

for word, tag in tagged_words:
    print(f"{word}\t{tag}")
