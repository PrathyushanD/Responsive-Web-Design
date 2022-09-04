def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_words(words):
    """Prints the first words after pooping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after pooping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)#First, run this with python3.6 ex25.py to find any errors you have made. Once you hace found all of the errors you can and fixed them, you will then want to folow the what you should see section to complete the exercise.
