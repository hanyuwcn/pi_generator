from pricetag.pricetag_reader import PricetagReader
from enquiry.enquiry_reader import EnquiryReader
from output.pi_writer import PIWriter

class Process:
    def __init__(self):
        self.enquiry_reader = EnquiryReader()
        self.pricetag_reader = PricetagReader()
        self.pi_writer = PIWriter()

    def read_pricetag(self):
        return self.pricetag_reader.read_pricetag()

    def read_enquiry(self):
        return self.enquiry_reader.read_enquiry()

    def make_header(self):
        pass

    def make_quote(self):
        pass

    def make_footer(self):
        pass

    def write_to_output(self):
        self.pi_writer.write_to_output()

