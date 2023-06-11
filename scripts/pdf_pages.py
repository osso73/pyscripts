#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 01/04/2020 11:44

pdf_pages.py - Copies certain pages from a pdf file into new file 
    
@author: opujo
"""

import PyPDF2, os, argparse, logging


def parse_pages(expr, total_pages):
    """evaluates expression and returns a number of pages, taking care
    to eliminate an number above total_pages, or below 1.
    List returned starts at 0, to be used with getPage().
    """
    
    if expr.lower() == 'all':
        return list(range(total_pages))

    initial = expr.replace(' ', '').split(',') # removes spaces and split list
    final = list()
    for elem in initial:
        if '-' in elem:
            i, f = elem.split('-')
        else:
            i = elem
            f = elem
        
        for n in range(int(i), int(f)+1):
            if n > 0 and n <= total_pages:
                final.append(n-1)   # to match list starting with 0
    
    return final

# parsing arguments
DESCRIPTION = 'Copies certain pages from a pdf file into new file. It allows \
for rotation of the pages, encryption/decryption of pdf files, as well as \
changing the order of the pages.'

EPILOG= 'Format of the expression of pages: Pages are indicated by numbers \
separated by commas. A range can be included by separating pages with - \
(dash). Put in the order you want them in the final file. To include all \
pages, use the expression "all". The expression needs to be in "" if it \
contains spaces.'

parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)

parser.add_argument("PDFfile", help="Input pdf file.")
parser.add_argument("pages", help='Pattern of pages to be included. See below \
                    the description of the format.')
parser.add_argument('-o', '--output', metavar='FILE', 
                    help="Name of the output pdf file. If this argument is \
                    not provided, it will use the same input name appending \
                    '_pages' at the end")
parser.add_argument('-r', '--rotate', metavar=('DEG', 'pages'), nargs=2, 
                    action='append', help='Rotate pages clockwise, by DEG \
                    degrees. pages is the list of pages to be rotated (see \
                    below the description of the format). Enter this option \
                    several times if you have pages rotating different \
                    angles. Note that angle has to be multiple of 90º.')
parser.add_argument('-m', '--merge', metavar=('PDFfile2', 'pages2'), 
                    action='append', nargs=2, help='Adds pages from \
                    PDFfile2 as well. This argument can be added several \
                    times to add additional files. These pages will not be \
                    modified by other flags (e.g. -r, or -d).')
parser.add_argument('-d', '--decrypt', metavar='PASSWD', 
                    help='Decrypt input pdf file with the PASSWD password.')
parser.add_argument('-e', '--encrypt', metavar='PASSWD', nargs='?', const=-1, 
                    help='Encrypt output pdf file with the PASSWD password. \
                    Leave PASSWD blank if you want to use the same password \
                    as for decryption.')
parser.add_argument('-l', '--logging', metavar='LEVEL', default='CRITICAL',
                    choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help="Set debugging level to LEVEL. Possible values are: \
                    'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.")

args = parser.parse_args()

# define logging, based on command line argument
logging.basicConfig(level=eval(f'logging.{args.logging}'), 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug(f'arguments: {args}')

# open file, and decrypt if needed
pdfFileObj = open(args.PDFfile, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
if args.decrypt:
    pdfReader.decrypt(args.decrypt)

# get the list of pages to copy, and to rotate
list_pages = parse_pages(args.pages, pdfReader.numPages)

rotate = dict()
if args.rotate:
    for i, each in enumerate(args.rotate):
        rotate[i] = ( int(each[0])//90*90,  # to ensure it's multiple of 90
              parse_pages(each[1], pdfReader.numPages) )

logging.info(f'Pages to include: {list_pages}')
for each in rotate.values():
    logging.info(f'Rotate {each[0]}º pages: {each[1]}')

# add pages to the output from the first file
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in list_pages:
    pageObj = pdfReader.getPage(pageNum)
    
    # rotate the pages as needed (allowing different rotations)
    for each in rotate.values():
        if pageNum in each[1]:
            pageObj.rotateClockwise(each[0])
    
    pdfWriter.addPage(pageObj)

# add pages from additional files (merge)
if args.merge:
    for merged_file in args.merge:
        filename, pags = merged_file
        newFile = open(filename, 'rb')
        pdfMerger = PyPDF2.PdfFileReader(newFile)
        list_pages = parse_pages(pags, pdfMerger.numPages)
        for pageNum in list_pages:
            pageObj = pdfMerger.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        #newFile.close()

# check if it needs encryption
if args.encrypt:
    if args.encrypt == -1:
        args.encrypt = args.decrypt if args.decrypt else ''
    pdfWriter.encrypt(args.encrypt)

# Save the resulting PDF to a file.
outputFile = args.output if args.output else args.PDFfile[:-3] + "_pages.pdf"
pdfOutput = open(outputFile, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
pdfFileObj.close() # closing the original pdf file


print('Done.')