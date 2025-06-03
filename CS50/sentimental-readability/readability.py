from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    index = calculate_index(letters, words, sentences)
    print_index(index)


def count_letters(text):
    letter = 0
    # Go through each letter
    for i in range(len(text)):
        # If letter count up
        if text[i].isalpha() == True:
            letter += 1
    return letter


def count_words(text):
    word = 1
    # Go thru each word
    for i in range(len(text)):
        # If word ends count up
        if text[i] == ' ':
            word += 1
    return word


def count_sentences(text):
    sentence = 0
    # Go thru each sentence
    for i in range(len(text)):
        # if sentence ends count up
        if text[i] in ['.', '!', '?']:
            sentence += 1
    return sentence


def calculate_index(letters, words, sentences):
    # Calculate
    avgletters = (letters / words) * 100
    avgsentences = (sentences / words) * 100
    index = 0.0588 * avgletters - 0.296 * avgsentences - 15.8
    index = round(index)
    return index


def print_index(index):
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print("Grade ", index)


main()