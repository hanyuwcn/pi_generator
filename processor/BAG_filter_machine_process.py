import pandas as pd

from processor import Process
from enquiry import BAGFilterMachineEnquiryReader
from pricetag import BAGFilterMachinePricetagReader
from header import BAGFilterMachineHeaderMaker
from footer import BAGFilterMachineFooterMaker
from quote import BAGFilterMachineQuoteMaker
from output import BAGFilterMachinePIWriter

from utils import reader_tools

import config

class BAGFilterMachineProcess(Process):
    def __init__(self):
        super().__init__()
        self.enquiry_reader = BAGFilterMachineEnquiryReader()
        self.pricetag_reader = BAGFilterMachinePricetagReader()
        self.header_maker = BAGFilterMachineHeaderMaker()
        self.footer_maker = BAGFilterMachineFooterMaker()
        self.quote_maker = BAGFilterMachineQuoteMaker()
        self.pi_writer = BAGFilterMachinePIWriter()
