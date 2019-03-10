import os
from input_reader import read_file
from example_generator import generate_examples
from feature_vector_converter import convert_examples_to_feature_vectors
from data_frame_converter import generate_data_frame
from scikit_helper import run_training_phase
from scikit_helper import run_testing_phase

data_set_directory = 'data_set/'
dirname = os.path.dirname(__file__)

train_data_range = range(111, 422)
test_data_range = range(0, 110)

global_data_frames = []
global_test_data_frames = []
test_positive_examples = []  # Used only for debugging purpose
test_negative_examples = []  # Used only for debugging purpose
train_positive_examples = []  # Used only for debugging purpose
train_negative_examples = []  # Used only for debugging purpose

pos_count = 0


def read_and_process_data(data_type):

    data_range = train_data_range if data_type == 'train' else test_data_range
    for file_no in data_range:

        # Step 1: Create absolute path for the file and check if the file exists.
        filename = os.path.join(dirname, data_set_directory + "/" + data_type + "/" + str(file_no) + ".txt")
        if not os.path.isfile(filename):
            continue

        # Step 2: Read the file and create a list of all words in the file.
        word_list = read_file(filename)

        # Step 3: Generate both positive and negative, uni-gram and bi-gram examples from the dataset.
        examples = generate_examples(word_list)

        if data_type == 'train':
            train_positive_examples.extend(examples.positive)
            train_negative_examples.extend(examples.negative)
        else:
            test_positive_examples.extend(examples.positive)
            test_negative_examples.extend(examples.negative)

        # Step 4: Convert the examples into feature vectors.
        positive_feature_vectors, negative_feature_vectors = convert_examples_to_feature_vectors(word_list, examples)

        # Step 5: Convert the feature vectors into panda DataFrames which can be fed to sci-kit.
        positive_data_frames = generate_data_frame(examples.positive, positive_feature_vectors, 1)
        negative_data_frames = generate_data_frame(examples.negative, negative_feature_vectors, 0)

        # Step 6: Add all data_frames to a common global data_frame list.

        if data_type == 'train':
            global_data_frames.extend(positive_data_frames)
            global_data_frames.extend(negative_data_frames)
        else:
            global_test_data_frames.extend(positive_data_frames)
            global_test_data_frames.extend(negative_data_frames)


read_and_process_data('train')
read_and_process_data('test')

print("************************ Training Examples *******************************")
print("Positive examples for TRAIN = " + str(len(train_positive_examples)))
print("Negative examples for TRAIN = " + str(len(train_negative_examples)))
print("\n************************ Training Examples *******************************")
print("Positive examples for TEST = " + str(len(test_positive_examples)))
print("Negative examples for TEST = " + str(len(test_negative_examples)))

run_training_phase(global_data_frames)
run_testing_phase(global_test_data_frames)
