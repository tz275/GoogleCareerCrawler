from crawler import crawler
import os
from converter import converter
from standardFormatConverter import standardFormatConverter

if __name__ == "__main__":
    crawler()
    n_convert = len(os.listdir("./raw_data")) + 1
    for i in range(1, n_convert):
        converter(i)
        standardFormatConverter(i)
