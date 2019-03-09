def read_file(filename):
    stream = open(filename, "r")
    raw_data_set = stream.read()
    raw_data_list = raw_data_set.split()
    sanitized_word_list = [word.strip(" .,;:()") for word in raw_data_list]
    return sanitized_word_list
