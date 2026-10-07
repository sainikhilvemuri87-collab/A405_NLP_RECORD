import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a sentence: ")

doc = nlp(text)

print("\nNamed entities")

print("----------------")

for ent in doc.ents:
    print(f"Entity : {ent.text}")
    print(f"Label  : {ent.label_}")
    print("----------------")
