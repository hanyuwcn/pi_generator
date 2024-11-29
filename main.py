from quotations import hello_world
from reader import read_configurations
from writer import write_to_file

if __name__ == '__main__':
    hello_world()
    data = read_configurations()

    print(data['name'])
    write_to_file(data['address'])