Author: @hanyuw.cn

Created Date: Nov.29.2024


License: for PRIVATE use only

This script is to generate PI based on inquried products and their quotations. It is for personal use and does not apply to commercial circumstances. 


Notes:
1. Input requires `Enquiry.xlsx` and `Catalog.xlsx` respectively to generate `PI of Spices.xlsx`. All files should left on the same folder as the application entrance.
2. Make sure the column names matches with that in the configurations.
3. If quantity in the inquery form is left empty it will be recognized as 1.
4. To generate new exe file, please run `pyinstaller -F main.py` and find 'main.exe' in the `dist` directory.
