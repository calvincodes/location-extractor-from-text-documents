import os
from input_reader import read_file
from example_generator import generate_examples

data_set_directory = 'all_labelled_data_set/'
dirname = os.path.dirname(__file__)

# for file_no in [163]:
for file_no in [318, 325, 297, 335, 163, 124]:
    filename = os.path.join(dirname, data_set_directory+str(file_no)+".txt")
    word_list = read_file(filename)
    examples = generate_examples(word_list)
    print(str(examples.positive))

