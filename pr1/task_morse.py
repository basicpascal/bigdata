morse_symbol = {'a': '.-', 'b': '-…', 'c': '-.-.', 'd': '-..',
                'e': '.', 'f': '..-.', 'g': '--.', 'h': '….',
                'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                'q': '--.-', 'r': '.-.', 's': '…', 't': '-',
                'u': '..-', 'v': '…-', 'w': '.--', 'x': '-..-',
                'y': '-.--', 'z': '--..'}


def encode_morse(text):
    words = text.split()
    morse_words = []

    for word in words:
        morse_word = ""
        for letter in word:
            if letter.lower() in morse_symbol:
                morse_word += morse_symbol[letter.lower()] + " "
        morse_words.append(morse_word.strip())

    return morse_words


input_text = input("Введите текст: ")
encoded_text = encode_morse(input_text)

for word in encoded_text:
    print(word)
