import re


def read_file(filename):
    stream = open(filename, "r")
    raw_data_set = stream.read()
    re.sub(' +', ' ', raw_data_set)  # Convert all multiple spaces to single.
    raw_data_list = raw_data_set.split()
    sanitized_word_list = [word.strip(" .,;:()") for word in raw_data_list]
    list(filter(lambda word: word != "", sanitized_word_list))  # Remove all occurrences of empty words from list
    return sanitized_word_list
