text = input().strip()
n = int(input().strip())
text2 = ""

for i in text:
    c = chr((ord(i) - ord('A') - n) % 26 + ord('A'))
    text2 += c

print(text2)