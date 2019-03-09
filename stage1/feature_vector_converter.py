# TODO: UPDATE WHITELISTED WORDS BY RUNNING A SCRIPT TO FETCH ALL LOCATIONS.
whitelisted_words = ["new york"]


# TODO: Add all relevant rules here for creation of feature vector
def convert_example_to_feature_vector(word_list, example):

    feature_vector = []

    example_index = example[0]
    example_text = example[1]
    prev_word_index = example_index - 1
    prev_prev_word_index = example_index - 2
    next_word_index = example_index + 1
    next_next_word_index = example_index + 2

    # TODO: As you add more features here, also update the dataframe_converter script

    # at <location>
    if prev_word_index >= 0 and word_list[prev_word_index].lower() == 'at':
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    # of the <location>
    if prev_word_index >= 0 and prev_prev_word_index >= 0 \
        and word_list[prev_prev_word_index].lower() == 'of' \
        and word_list[prev_word_index].lower() == 'the':
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    # Feature for whitelisting
    if example_text.lower() in whitelisted_words:
        feature_vector.append(1)
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
