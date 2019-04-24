import tabula
from tabula import convert_into
import os

# Python version 3.7.0
# Microsoft Windows 10 Enterprise version 10.0.15063 Build 15063
# Mac OS Mojave 10.14.3 (18D109)

#///////extract information from table in a pdf and output into excel sheet/////////
#useful blog from creator of tabula-py: https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302
# This script created by Yasmin Stoss and Josh Borycz at Oak Ridge National Lab

inname = input("What is the PDF filename (without .pdf)? ")
outname = input("What is the CSV filename (without .csv)? ")
startpage = input("What is the START page? ")
endpage = input("What is the END page? ")

def extract_budget ():

    # area and columns define the location coordinates of the table in pdf units
    # If an error occurs, compare this years report to the example report to see if the table locations are different
    # pages need to be updated each year
    # useful thread on defining coordinates: https://stackoverflow.com/questions/45457054/tabula-extract-tables-by-area-coordinates
    output = convert_into(filePDF, outpath, guess = False, area = (86.13,43.32,706.71,554.48), columns = (43.32,341.02,405,478.26,554.48), output_format = "csv", pages = '{}-{}'.format(startpage, endpage))
    print("finished")

#//////////// main ///////////////////////

script_dir = os.path.dirname(__file__)

# the filePDF name will need to be updated to match the new pdf name
# outpath should be given a new name
filePDF  = os.path.join(script_dir, '{}.pdf'.format(inname)) # input from PDF, this pdf should be in the same folder as the script
outpath = os.path.join(script_dir, '{}.csv'.format(outname))   # output into CSV, this file will create itself

extract_budget()
