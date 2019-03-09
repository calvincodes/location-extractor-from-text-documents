import os
from input_reader import read_file
from example_generator import generate_examples
from feature_vector_converter import convert_examples_to_feature_vectors
from data_frame_converter import generate_data_frame
from scikit_helper import train_all_models

data_set_directory = 'all_labelled_data_set/'
dirname = os.path.dirname(__file__)

global_data_frames = []

for file_no in [318, 325, 297, 335, 163, 124]:

    # Step 1: Read the file and create a list of all words in the file.
    filename = os.path.join(dirname, data_set_directory+str(file_no)+".txt")
    word_list = read_file(filename)

    # Step 2: Generate both positive and negative, uni-gram and bi-gram examples from the dataset.
    examples = generate_examples(word_list)

    # Step 3: Convert the examples into feature vectors.
    positive_feature_vectors, negative_feature_vectors = convert_examples_to_feature_vectors(word_list, examples)

    # Step 4: Convert the feature vectors into panda DataFrames which can be fed to sci-kit.
    positive_data_frames = generate_data_frame(examples.positive, positive_feature_vectors, 1)
    negative_data_frames = generate_data_frame(examples.negative, negative_feature_vectors, 0)

    # Step 5: Add all data_frames to a common global data_frame list.
    global_data_frames.extend(positive_data_frames)
    global_data_frames.extend(negative_data_frames)

train_all_models(global_data_frames)
