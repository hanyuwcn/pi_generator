class EnquiryReader:
    """
    Read the enquiry from original xlsx file.
    It does not deal with any business logic except validating the format of the dataframe.

    Different company and product-lines have different enquiry format(xlsx, pdf, csv, etc.) and content format.
    (e.g. 1 table, 2 tables, tables in multiple sheets, etc.); some might have to read from various sources,
    and hence different strategies are needed.

    An enquiry is a collection of required products and their quantity(sometimes omitted when only 1 is needed).

    Input: original file by its path
    Output: a pd dataframe with raw data
    """
    def read_enquiry(self):
        """
        Read Enquiry from file into a dataframe.
        """
        pass

    def validate(self):
        """
        Validate the Enquiry.
        """
        pass