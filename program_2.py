def word_separator(sentence):
    new_sentence = ""
    current_word = ""

    for char in sentence:
        if char.isupper() and current_word:
            new_sentence += current_word + " "
            current_word = char
        else:
            current_word += char

    new_sentence += current_word
    new_sentence = new_sentence.lower()
    new_sentence = new_sentence.capitalize()

    return new_sentence.strip()

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
