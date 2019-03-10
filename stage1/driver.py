import os
from input_reader import read_file
from example_generator import generate_examples
from feature_vector_converter import convert_examples_to_feature_vectors
from data_frame_converter import generate_data_frame
from scikit_helper import train_all_models

data_set_directory = 'all_labelled_data_set/'
dirname = os.path.dirname(__file__)
global_data_frames = []
global_test_data_frames = []
test_positive_examples = []
test_negative_examples = []
all_positive_examples = []  # Used only for debugging purpose
all_negative_examples = []  # Used only for debugging purpose

pos_count = 0

for file_no in range(111, 422):
    # Step 1: Create absolute path for the file and check if the file exists.
    filename = os.path.join(dirname, data_set_directory+"/train/"+str(file_no)+".txt")
    if not os.path.isfile(filename):
        continue

    # Step 2: Read the file and create a list of all words in the file.
    word_list = read_file(filename)

    # Step 3: Generate both positive and negative, uni-gram and bi-gram examples from the dataset.
    examples = generate_examples(word_list)
    all_positive_examples.extend(examples.positive)
    all_negative_examples.extend(examples.negative)

    # Step 4: Convert the examples into feature vectors.
    positive_feature_vectors, negative_feature_vectors = convert_examples_to_feature_vectors(word_list, examples)

    # pos_count += len(examples.positive)
    # if pos_count < 70:
    #     all_positive_examples.extend(examples.positive)
    #     positive_data_frames = generate_data_frame(examples.positive, positive_feature_vectors, 1)
    #     global_data_frames.extend(positive_data_frames)

    # Step 5: Convert the feature vectors into panda DataFrames which can be fed to sci-kit.
    positive_data_frames = generate_data_frame(examples.positive, positive_feature_vectors, 1)
    negative_data_frames = generate_data_frame(examples.negative, negative_feature_vectors, 0)

    # Step 6: Add all data_frames to a common global data_frame list.
    global_data_frames.extend(positive_data_frames)
    global_data_frames.extend(negative_data_frames)


for file_no in range(0, 110):
    filename = os.path.join(dirname, data_set_directory + "/test/" + str(file_no) + ".txt")
    if not os.path.isfile(filename):
        continue

    # Step 2: Read the file and create a list of all words in the file.

    word_list = read_file(filename)

    # Step 3: Generate both positive and negative, uni-gram and bi-gram examples from the dataset.
    examples = generate_examples(word_list)
    test_positive_examples.extend(examples.positive)
    test_negative_examples.extend(examples.negative)

    # Step 4: Convert the examples into feature vectors.
    positive_feature_vectors, negative_feature_vectors = convert_examples_to_feature_vectors(
        word_list, examples)

    # pos_count += len(examples.positive)
    # if pos_count < 70:
    #     all_positive_examples.extend(examples.positive)
    #     positive_data_frames = generate_data_frame(examples.positive, positive_feature_vectors, 1)
    #     global_data_frames.extend(positive_data_frames)

    # Step 5: Convert the feature vectors into panda DataFrames which can be fed to sci-kit.
    positive_data_frames = generate_data_frame(examples.positive,
                                               positive_feature_vectors, 1)
    negative_data_frames = generate_data_frame(examples.negative,
                                               negative_feature_vectors, 0)

    # Step 6: Add all data_frames to a common global data_frame list.
    global_test_data_frames.extend(positive_data_frames)
    global_test_data_frames.extend(negative_data_frames)


print("Positive cases for train = " + str(len(all_positive_examples)))
print("Negative cases for train = " + str(len(all_negative_examples)))
print("Positive cases for test = " + str(len(test_positive_examples)))
print("Negative cases for test = " + str(len(test_negative_examples)))

train_all_models(global_data_frames, global_test_data_frames)
