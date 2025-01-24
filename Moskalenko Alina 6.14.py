text = input()

cleaned_text = text.replace(" ", "")
if cleaned_text == cleaned_text[::-1]:
    print("YES")
else:
    print("NO")