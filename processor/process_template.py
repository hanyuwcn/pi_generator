from email.header import Header

from header import HeaderMaker
from pricetag.pricetag_reader import PricetagReader
from enquiry.enquiry_reader import EnquiryReader
from header import HeaderMaker
from footer import FooterMaker
from quote import QuoteMaker
from output.pi_writer import PIWriter

class Process:
    def __init__(self):
        self.enquiry_reader = EnquiryReader()
        self.pricetag_reader = PricetagReader()
        self.header_maker = HeaderMaker()
        self.footer_maker = FooterMaker()
        self.quote_maker = QuoteMaker()
        self.pi_writer = PIWriter()

    def read_pricetag(self):
        self.pricetag = self.pricetag_reader.read_pricetag()

    def read_enquiry(self):
        self.enquiry = self.enquiry_reader.read_enquiry()

    def make_header(self):
        self.header = self.header_maker.make_header()

    def make_quote(self):
        self.quote = self.quote_maker.make_quote(self.enquiry, self.pricetag)

    def make_footer(self):
        pass

    def write_to_output(self):
        self.pi_writer.write_to_output(self.header, self.quote, self.footer)
