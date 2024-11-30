from processor import Processor
from enquiry import BAGFilterMachineEnquiryReader
from pricetag import BAGFilterMachinePricetagReader
from header import BAGFilterMachineHeaderMaker
from footer import BAGFilterMachineFooterMaker
from quote import BAGFilterMachineQuoteMaker
from output import BAGFilterMachinePIWriter

from utils import writer_tools

import config

class BAGFilterMachineProcess(Processor):
    def __init__(self):
        super().__init__()
        self.enquiry_reader = BAGFilterMachineEnquiryReader()
        self.pricetag_reader = BAGFilterMachinePricetagReader()
        self.header_maker = BAGFilterMachineHeaderMaker()
        self.footer_maker = BAGFilterMachineFooterMaker()
        self.quote_maker = BAGFilterMachineQuoteMaker()
        self.pi_writer = BAGFilterMachinePIWriter()

    def make_footer(self):
        total_amount = self.quote[config.QUOTE_TOTAL_AMOUNT]
        deposit = writer_tools.get_deposit(total_amount)

        self.footer = self.footer_maker.make_footer({config.QUOTE_TOTAL_AMOUNT: total_amount, config.DEPOSIT_HEADER: deposit})

    def process(self):
        self.read_pricetag()
        self.read_enquiry()
        self.make_header()
        self.make_quote()
        self.make_footer()
        self.write_to_output()