import re

def parse_text():
    """
    Зчитує текст із файлу 'text.txt', видаляє непотрібні символи та розбиває його на слова.
    """
    with open('text.txt', 'r', encoding='utf-8') as file:
        t = file.read()  # Зчитуємо текст з файлу
    words = re.findall(r'\b\w+\b', t.lower())  # Видаляємо розділові знаки та приводимо текст до нижнього регістру
    return words

def count_word(words):
    """
    Підраховує частоту кожного слова в списку.
    """
    word_counts = {}  # Створюємо порожній словник для зберігання частоти слів
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  # Якщо слово вже є, збільшуємо його лічильник
        else:
            word_counts[word] = 1  # Якщо слова немає в словнику, додаємо його з лічильником 1
    return word_counts

def sort_and_display(word_counts):
    """
    Сортує слова за частотою та виводить їх на екран.
    """
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)  # Сортуємо за кількістю
    for word, count in sorted_words:
        print(f"{word}: {count}")  # Виводимо слово та його кількість

def main():
    """
    Основна функція програми.
    """
    words = parse_text()  # Отримуємо список слів із файлу
    word_counts = count_word(words)  # Підраховуємо частоту слів
    sort_and_display(word_counts)  # Сортуємо і виводимо на екран

if __name__ == "__main__":
    main()  # Виконуємо основну програму
