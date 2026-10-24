from nltk.metrics import edit_distance

str1 = input("Enter the first string: ").lower().strip()
str2 = input("Enter the second string: ").lower().strip()

distance = edit_distance(str1, str2)

max_length = max(len(str1), len(str2))

if max_length == 0:
    similarity = 1.0
else:
    similarity = 1 - (distance / max_length)

print("\nString 1:", str1)
print("String 2:", str2)
print("Edit Distance:", distance)
print("Similarity Score:", round(similarity, 4))
print("Similarity Percentage:", round(similarity * 100, 2), "%")

if similarity >= 0.80:
    print("Result: Highly Similar")
elif similarity >= 0.50:
    print("Result: Moderately Similar")
else:
    print("Result: Less Similar")
