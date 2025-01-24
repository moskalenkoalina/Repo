text = input()
text2 = ""
for i in text:
    if i.isalpha():
        text2 += i * 2
    else:
        text2 += i
print(text2)