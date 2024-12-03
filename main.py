import config
from processor import SpicesProcessor
from system import logger

## (TODO) Add python documents to methods and classes, including responsibilities of each modules(on the abstract class)

if __name__ == '__main__':
    logger.info("Start application [{application}]...".format(application=config.APPLICATION))

    processor = SpicesProcessor()
    processor.process()

    logger.info("Application ends.")

