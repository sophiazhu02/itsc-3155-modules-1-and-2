words = []

for i in range(5):
    word = input("Enter a word : ")
    words.append(word)

string = ' '.join(words)

print(f"Words: {words}")
print(f"One String: {string}")

# https://www.w3schools.com/python/ref_string_join.asp
# used the above link to learn about the join method