# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:08:33 2017

@author: mstelmach
"""

# Loading the pyPdf Library
from pyPdf import PdfFileWriter, PdfFileReader

# Creating a routine that appends files to the output file
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

# Creating an object where pdf pages are appended to
output = PdfFileWriter()

# Appending two pdf-pages from two different files
append_pdf(PdfFileReader(open(r"W:\OneDrive\TERRAFORM POWER LLC\HCP - Documents\KWP\Purchasing\FY2018\Reconyx\KWP_HCP_Reconyx_20170821_POR Template_TERP_v0.pdf","rb")),output)
append_pdf(PdfFileReader(open(r"W:\OneDrive\TERRAFORM POWER LLC\HCP - Documents\KWP\Purchasing\FY2018\Reconyx\RECONYX Quote 151940.pdf","rb")),output)

# Writing all the collected pages to a file
output.write(open(r"W:\OneDrive\TERRAFORM POWER LLC\HCP - Documents\KWP\Purchasing\FY2018\Reconyx\KWP_HCP_Reconyx_20170822_POR.pdf","wb"))