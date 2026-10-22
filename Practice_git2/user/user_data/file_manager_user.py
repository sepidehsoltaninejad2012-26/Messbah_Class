import os
import pickle


def write_to_file(file_name, data):
    my_file = open(file_name, "wb")
    pickle.dump(data, my_file)
    my_file.close()


def read_from_file(file_name):
    if os.path.exists(file_name):
        my_file = open(file_name, "rb")
        data = pickle.load(my_file)
        my_file.close()
        return data
    else:
        print("File not found")