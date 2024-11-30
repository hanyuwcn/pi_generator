from pricetag import PricetagReader
from enquiry import EnquiryReader
from header import HeaderMaker
from footer import FooterMaker
from quote import QuoteMaker
from output import PIWriter

## the full process from reading to export framework by calling each component makers
## each company, product-line should have their own strategy
## since all components are handled by their correspondent modules,
## this process is simply use different strategy object to process respectively and integrate them
## normally modules are independent of each others,
## but in some cases it has exceptions, such as headers depends on quotations,
## in which cases the process would be of different orders.
## therefore process method is left as abstract
## all module maker methods are created with parameter-less, they call parameters from object-scoped ones,
## this save us from the problems of different module maker involves various input parameters types
## input: enquiry, pricetag, header, footer, quote, writer components of each module
## output: a full process that integrate all components and eventually make the invoice

class Processor:
    def __init__(self):
        self.pricetag = None
        self.enquiry = None
        self.header = None
        self.quote = None
        self.footer = None

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
        self.footer = self.footer_maker.make_footer(self.quote)

    def write_to_output(self):
        self.pi_writer.write_to_output(self.header, self.quote, self.footer)

    def process(self):
        pass
