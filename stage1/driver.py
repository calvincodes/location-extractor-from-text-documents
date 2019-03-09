import os
from input_reader import read_file
from example_generator import generate_examples
from feature_vector_converter import convert_examples_to_feature_vectors

data_set_directory = 'all_labelled_data_set/'
dirname = os.path.dirname(__file__)

global_feature_vector_list = []

for file_no in [318, 325, 297, 335, 163, 124]:
    filename = os.path.join(dirname, data_set_directory+str(file_no)+".txt")
    word_list = read_file(filename)
    examples = generate_examples(word_list)
    feature_vectors = convert_examples_to_feature_vectors(word_list, examples)
    global_feature_vector_list.extend(feature_vectors)
    print(str(examples.positive))

