def generate_data_frame(examples, feature_vectors, class_label):
    data_frame = []
    for i in range(0, len(examples)):
        data_frame.append((examples[i][1],
                           # TODO: Add more features here as the feature vector expands
                           feature_vectors[i][0], feature_vectors[i][1], feature_vectors[i][2],
                           class_label))

    return data_frame
