Author: @hanyuw.cn

Created Date: Nov.29.2024


License: for PRIVATE use only

This script is to generate PI based on inquried products and their quotations. It is for personal use and does not apply to commercial circumstances. 


Remarks:
- Input requires `Enquiry.xlsx` and `Catalog.xlsx` respectively to generate `PI of Spices.xlsx`. All files should left on the same folder as the application entrance
- To generate new `main.exe` file, please run `pyinstaller -F main.py` and find `main.exe` in the `dist` directory
- Details for the format of the inputs:
    - Make sure the column names matches with that in the configurations.
    - Catalog must have `Product` and `Price` columns
    - Enquiry must have `Product` and `Quantity` columns
    - Avoid column names duplication
    - Products must have `Product`(name) and `Price`, other columns can be optionally left blank
    - Values matching is case sensitive
