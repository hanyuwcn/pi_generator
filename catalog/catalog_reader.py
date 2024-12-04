class CatalogReader:
    """
    Read the catalog from original xlsx file.
    It does not deal with any business logic except validating the format of the dataframe.

    Different company and product-lines have different catalog format(xlsx, pdf, csv, etc.) and content format.
    (e.g. 1 table, 2 tables, tables in multiple sheets, etc.); some might have to read from various sources,
    and hence different strategies are needed.

    A catalog is a collection of all products and their detailed attributes,
    including product names, attributes, descriptions and prices;

    Input: original file by its path
    Output: a dataframe with raw data
    """
    def read_catalog(self):
        """
        Read Catalog from file into a dataframe.
        """
        pass

    def validate(self):
        """
        Validate the Catalog.
        """
        pass