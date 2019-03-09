def read_file(filename):
    stream = open(filename, "r")
    raw_data_set = stream.read()
    raw_data = raw_data_set.split()
    word_list = [word.strip(" .,;:()") for word in raw_data]
    return word_list
