from collections import Counter


def anagrams(word, words):
    return [inner_word for inner_word in words if Counter(inner_word) == Counter(word)]
