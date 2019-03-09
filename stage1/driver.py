import os
from input_reader import read_file

data_set_directory = 'all_labelled_data_set/'
dirname = os.path.dirname(__file__)

for file_no in [311, 318, 335, 163, 124]:
    filename = os.path.join(dirname, data_set_directory+str(file_no)+".txt")
    examples = read_file(filename)

print("END")
