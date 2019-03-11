from constants import neighboring_verbs_for_negative_examples, blacklist_words, possible_strong_prev_words
from nltk.corpus import wordnet as wn


def convert_example_to_feature_vector(word_list, example):
    feature_vector = []

    example_index = example[0]
    example_text = example[1]
    prev_word_index = example_index - 1
    prev_prev_word_index = example_index - 2
    next_word_index = example_index + 1
    next_next_word_index = example_index + 2

    # Steps to add new features.
    # As you add more features (/rules) below, you should also update
    # 1. data_frame_converter.py
    # 2. constants.py scripts

    # Feature representing if first letters is UPPER CASE.
    if example_text[0].isupper():
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    # Feature representing if all letters are UPPER CASE.
    if example_text.isupper():
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if prev_word_index >= 0 and word_list[prev_word_index].lower() in neighboring_verbs_for_negative_examples:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if next_word_index < len(word_list) \
            and word_list[next_word_index].lower() in neighboring_verbs_for_negative_examples:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if example_text in blacklist_words or example_text[0:-1] in blacklist_words:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    # Previous word is a strong word like 'of', 'at', 'near'
    if prev_word_index >= 0 \
            and word_list[prev_word_index].lower() in possible_strong_prev_words:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    # Previous word is a strong word like 'of', 'at', 'near'
    # AND Previous to Previous word is "THE"
    if prev_word_index >= 0 and prev_prev_word_index >= 0 \
            and word_list[prev_prev_word_index].lower() in possible_strong_prev_words \
            and word_list[prev_word_index].lower() == 'the':
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if example_index in [0, 1, 2] \
            and example_text[0].isupper() \
            and word_list[next_next_word_index] == '—':
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if next_word_index < len(word_list):
        dictionary = wn.synsets(word_list[next_word_index])
        if len(dictionary) > 0 and dictionary[0].pos() == 'v':
            feature_vector.append(1)
        elif next_next_word_index < len(word_list):
            dictionary = wn.synsets(word_list[next_next_word_index])
            if len(dictionary) > 0 and dictionary[0].pos() == 'v':
                feature_vector.append(1)
            else:
                feature_vector.append(0)
        else:
            feature_vector.append(0)
    else:
        feature_vector.append(0)

    return feature_vector


def convert_examples_to_feature_vectors(word_list, examples):
    positive_feature_vectors = []
    negative_feature_vectors = []
    for i in range(0, len(examples.positive)):
        positive_feature_vectors.append(convert_example_to_feature_vector(word_list, examples.positive[i]))
    for i in range(0, len(examples.negative)):
        negative_feature_vectors.append(convert_example_to_feature_vector(word_list, examples.negative[i]))
    return positive_feature_vectors, negative_feature_vectors
