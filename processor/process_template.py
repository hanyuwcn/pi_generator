from catalog import CatalogReader
from enquiry import EnquiryReader
from header import HeaderMaker
from footer import FooterMaker
from quote import QuoteMaker
from output import PIWriter


class Processor:
    """
    The full process from reading the files to exporting an output by calling each component makers.

    Each company, product-line has its own strategy.

    Since all components are handled by their correspondent modules,
    this process is simply use different strategy object to process respectively and integrate them.

    Normally modules are independent of each others,
    but in some cases they have cases such as headers depend on quotations,
    in which cases the process would be of different sequences.

    Process methods are left as abstract.
    All module maker methods are created with parameter-less, they call parameters from object-scoped ones,
    which avoids the problems of different module maker involves various input parameters types.

    Input: enquiry, catalog, header, footer, quote, writer components of each module
    Output: a full process that integrate all components and eventually make the invoice
    """
    def __init__(self):
        """
        Configure all handlers to deal with components.
        """
        self.catalog = None
        self.enquiry = None
        self.header = None
        self.quote = None
        self.footer = None

        self.enquiry_reader = EnquiryReader()
        self.catalog_reader = CatalogReader()
        self.header_maker = HeaderMaker()
        self.footer_maker = FooterMaker()
        self.quote_maker = QuoteMaker()
        self.pi_writer = PIWriter()

    def read_catalog(self):
        """
        Use the Catalog reader to read the Catalog.
        """
        self.catalog = self.catalog_reader.read_catalog()

    def read_enquiry(self):
        """
        Use the Enquiry reader to read the Enquiry.
        """
        self.enquiry = self.enquiry_reader.read_enquiry()

    def make_header(self):
        """
        Use the header maker to make the header.
        """
        self.header = self.header_maker.make_header()

    def make_quote(self):
        """
        Use the quote maker to make the quote.
        """
        self.quote = self.quote_maker.make_quote(self.enquiry, self.catalog)

    def make_footer(self):
        """
        Use the footer maker to make the footer.
        """
        self.footer = self.footer_maker.make_footer(self.quote)

    def write_to_output(self):
        """
        Use the writer to write all contents to output.
        """
        self.pi_writer.write_to_output(self.header, self.quote, self.footer)

    def process(self):
        """
        Full end-to-end process to make the PI.
        """
        self.read_catalog()
        self.read_enquiry()
        self.make_header()
        self.make_quote()
        self.make_footer()
        self.write_to_output()
