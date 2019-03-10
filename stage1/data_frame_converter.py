def generate_data_frame(examples, feature_vectors, class_label):
    data_frame = []
    for i in range(0, len(examples)):
        data_frame.append((examples[i][1],
                           # TODO: Add more features here as the feature vector expands
                           feature_vectors[i][0], feature_vectors[i][1], feature_vectors[i][2],
                           feature_vectors[i][3],feature_vectors[i][4], feature_vectors[i][5], feature_vectors[i][6],  feature_vectors[i][7],
                           class_label))

    return data_frame
