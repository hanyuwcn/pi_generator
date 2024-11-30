from pricetag import BAGFilterMachinePricetagReader
from utils import reader_tools
from utils import writer_tools
from enquiry import BAGFilterMachineEnquiryReader
from output import BAGFilterMachinePIWriter, PIWriter
from header import BAGFilterMachineHeaderMaker
from footer import BAGFilterMachineFooterMaker
from quote import BAGFilterMachineQuoteMaker
import config
import numpy as np
import pandas as pd
from processor import BAGFilterMachineProcess

## (TODO) Add log that can export to an txt file
## (TODO) Add python documents to methods and classes, including responsibilities of each modules(on the abstract class)

if __name__ == '__main__':
    processor = BAGFilterMachineProcess()
    processor.process()
