import config
from processor import SpicesProcessor
from system import logger

## (TODO) Add python documents to methods and classes, including responsibilities of each modules(on the abstract class)

# def present():
#     a, b = get_value()
#     print(a)
#
# def get_value():
#     return 1, 2

# def present():
#     str, x = fun()
#     print(str)
#
# def fun():
#     str = "geeksforgeeks"
#     x = 20
#     return str, x

if __name__ == '__main__':
    logger.info("Start application [{application}]...".format(application=config.APPLICATION))

    processor = SpicesProcessor()
    processor.process()

    logger.info("Application ends.")


