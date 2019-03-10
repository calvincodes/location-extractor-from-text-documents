from constants import whitelisted_words, neighboring_verbs_for_negative_examples, blacklist_words
from nltk.corpus import wordnet as wn



# TODO: Add all relevant rules here for creation of feature vector
def convert_example_to_feature_vector(word_list, example):
    feature_vector = []

    example_index = example[0]
    example_text = example[1]
    prev_word_index = example_index - 1
    prev_prev_word_index = example_index - 2
    next_word_index = example_index + 1
    next_next_word_index = example_index + 2

    # TODO: As you add more features (/rules) here, also update the data_frame_converter.py and constants.py scripts
    # if(example_text == "SAN FRANCISCO"):
    #     print ("reached")
    if example_text[0].isupper():
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if example_text.isupper():
        feature_vector.append(1)
    else: feature_vector.append(0)

    if prev_word_index >= 0 and word_list[prev_word_index].lower() in neighboring_verbs_for_negative_examples:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if next_word_index < len(word_list) and word_list[next_word_index].lower() in neighboring_verbs_for_negative_examples:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if example_text in blacklist_words or example_text[0:-1] in blacklist_words:
        feature_vector.append(1)
    else:
        feature_vector.append(0)


    # if next_next_word_index < len(word_list) and word_list[next_next_word_index][0].isupper():
    #     feature_vector.append(1)
    # else:
    #     feature_vector.append(0)

    # at <location>
    if prev_word_index >= 0 and \
            (word_list[prev_word_index].lower() == 'of'
        or word_list[prev_word_index].lower() == 'at'
        or word_list[prev_word_index].lower() == 'between'
        or word_list[prev_word_index].lower() == 'neighbouring'
        or word_list[prev_word_index].lower() == 'neighboring'
        or word_list[prev_word_index].lower() == 'into'
        or word_list[prev_word_index].lower() == 'from'
        or word_list[prev_word_index].lower() == 'near'
        or word_list[prev_word_index].lower() == 'across'
        or word_list[prev_word_index].lower() == 'over'
        or word_list[prev_word_index].lower() == 'around'
        or word_list[prev_word_index].lower() == 'outside'
        or word_list[prev_word_index].lower() == 'to'
        or word_list[prev_word_index].lower() == 'in'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    # of the <location>
    if prev_word_index >= 0 and prev_prev_word_index >= 0 \
            and (word_list[prev_prev_word_index].lower() == 'of'
            or word_list[prev_prev_word_index].lower() == 'at'
            or word_list[prev_prev_word_index].lower() == 'between'
            or word_list[prev_prev_word_index].lower() == 'neighbouring'
            or word_list[prev_prev_word_index].lower() == 'neighboring'
            or word_list[prev_prev_word_index].lower() == 'into'
            or word_list[prev_prev_word_index].lower() == 'from'
            or word_list[prev_prev_word_index].lower() == 'near'
            or word_list[prev_prev_word_index].lower() == 'across'
            or word_list[prev_prev_word_index].lower() == 'over'
            or word_list[prev_prev_word_index].lower() == 'around'
            or word_list[prev_prev_word_index].lower() == 'outside'
            or word_list[prev_prev_word_index].lower() == 'to'
            or word_list[prev_prev_word_index].lower() == 'in') \
            and word_list[prev_word_index].lower() == 'the':
        feature_vector.append(1)
    else:
        feature_vector.append(0)


    # Feature for whitelisting
    if example_text.lower() in whitelisted_words:
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if next_word_index < len(word_list):
        dict = wn.synsets(word_list[next_word_index])
        if len(dict) > 0 and dict[0].pos() == 'v':
            feature_vector.append(1)
        elif next_next_word_index < len(word_list):
            dict = wn.synsets(word_list[next_next_word_index])
            if len(dict) > 0 and dict[0].pos() == 'v':
                feature_vector.append(1)
            else: feature_vector.append(0)
        else: feature_vector.append(0)
    else: feature_vector.append(0)


    return feature_vector




def convert_examples_to_feature_vectors(word_list, examples):
    positive_feature_vectors = []
    negative_feature_vectors = []
    for i in range(0, len(examples.positive)):
        positive_feature_vectors.append(convert_example_to_feature_vector(word_list, examples.positive[i]))
    for i in range(0, len(examples.negative)):
        negative_feature_vectors.append(convert_example_to_feature_vector(word_list, examples.negative[i]))
    return positive_feature_vectors, negative_feature_vectors
