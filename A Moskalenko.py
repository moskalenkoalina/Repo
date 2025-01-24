import re
def parse_text() :
    with open('text.txt', 'r', encoding='windows-1251') as file:
        t = file.read()
    words = re.findall(r'\b\w+\b', t.lower())
    return words

def count_word(words):
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts 