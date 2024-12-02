import catalog
from catalog import SpicesCatalogReader
from utils import reader_tools
from utils import writer_tools
from enquiry import SpicesEnquiryReader
from output import SpicesPIWriter, PIWriter
from header import SpicesHeaderMaker
from footer import SpicesFooterMaker
from quote import SpicesQuoteMaker
import config
import numpy as np
import pandas as pd
from processor import SpicesProcessor
from utils import logger
import traceback

## (TODO) Add python documents to methods and classes, including responsibilities of each modules(on the abstract class)

if __name__ == '__main__':
    logger.info("Start application [{application}]...".format(application=config.APPLICATION))

    processor = SpicesProcessor()
    processor.process()

    logger.info("Application ends.")
