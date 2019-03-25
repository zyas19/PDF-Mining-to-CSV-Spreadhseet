import tabula
from tabula import convert_into
#Python version 3.7.0
# Microsoft Windows 10 Enterprise version 10.0.15063 Build 15063

#///////extract information from table in a pdf and output into excel sheet/////////
#useful blog from creator of tabula-py: https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302
# This script created by Yasmin Stoss at Oak Ridge National Lab

def extract_budget ():

    #area and columns define the location coordinates of the table in pdf units
    #useful thread on defining coordinates: https://stackoverflow.com/questions/45457054/tabula-extract-tables-by-area-coordinates
    output = convert_into(filePDF, outpath, guess = False, area = (86.13,43.32,706.71,554.48), columns = (43.32,341.02,405,478.26,554.48), output_format = "csv", pages = '5-137')
    print("finished")

#//////////// main ///////////////////////
#if __name__ == '__main__':

filePDF  = '' # input from PDF
outpath = ''   # output into CSV

extract_budget()
