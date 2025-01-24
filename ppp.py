letters = input()
word = input()
counter = {}
for letter in letters:
    counter = counter.get(letter, 0) + 1

for letter in word:
    counter[letter] = counter.get(letter, 0) - 1
    if counter[letter] < 0:
        print("No")
        break
    else:
       print("Yes")