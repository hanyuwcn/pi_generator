import os


def write_to_file(contents):
    file_path = os.getcwd() + '/world.txt'

    file = open(file_path, "w", encoding='utf-8')
    file.write(contents)
    file.close()