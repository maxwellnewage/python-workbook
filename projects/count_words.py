"""
Cuenta la cantidad de palabras que tiene un string
"""


def remove_punctuation_marks(text: str):
    punctuation_marks = [".", ",", ";", ":", "!", "?", "-", "_", "(", ")"]

    for mark in punctuation_marks:
        text = text.replace(mark, "")

    return text


def count_words(text):
    text = text.lower()
    text = remove_punctuation_marks(text)

    words = text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


if __name__ == '__main__':
    sample_text = "Hello, world! This is a sample text: a simple text."
    result = count_words(sample_text)
    for word, count in result.items():
        print(f"'{word}': {count} times")
