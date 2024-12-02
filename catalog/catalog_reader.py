## read catalog from original file
## different company and product-lines have different catalog format(xlsx, pdf, csv, etc) and content format
# (1 table, 2 tables, tables in multiple sheets, etc), some might have to read multiple sources,
# and hence need different strategies
## catalog is a detailed catalog of all products and their attributes, (including product names, attributes, descriptions and prices)
## it does not involve any business logic, nor related with business catalog headers
## input: original file and its path
## output: a pd dataframe with raw data

## (TODO) Rename catalog to catalog
class CatalogReader:
    def read_catalog(self):
        pass