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

def sort_and_display(word_counts):
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

def main():
    file_path = 'text.txt'
    words = parse_text()
    word_counts = count_word(words)
    sort_and_display(word_counts)
if __name__ == "__main__":
    main()