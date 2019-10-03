#!/usr/bin/env python
import sys # Load in module that accesses the command line
import fileinput # This module gives us the ability to read files
import re # This imports the regex capability
#import pdb

def help():
   print("HELP")
   print("Either add only filename (expres.anal.csv) or add field number and then the file name (expres.anal.csv)")
   print("Enter -f followed by gene ID field number to get the gene name based on the gene ID")
   print("Example: -f2 will replace the gene id in expres.anal.csv with the gene name from Homo_sapiens.GRCh37.75.gtf")


argc = len(sys.argv)
if argc != 2 and argc != 3:
    help()
    sys.exit(1)

filename = ''
field_no = 1
if argc == 2:
     filename = sys.argv[1]
else:
     filename = sys.argv[2]
     match = re.match(r'-f(\d)', sys.argv[1])
     if match:
         field_no = int(match.group(1))
     else:
         help()
         sys.exit(1)

Lookup_geneID={}
#pdb.set_trace()
for each_line_of_text in fileinput.input("Homo_sapiens.GRCh37.75.gtf"):
    fields = re.split('\t', each_line_of_text)
    if len(fields) < 5:
        continue
    else:
        gene_id_matches = re.findall('gene_id \"(.*?)\";',each_line_of_text)
        gene_name_matches = re.findall('gene_name \"(.*?)\";',each_line_of_text)
        if gene_id_matches:
             if gene_name_matches:
                 Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]

for each_line_of_text in fileinput.input(filename):
    text_in_columns = re.split(',',each_line_of_text)
    if text_in_columns[0] == '""':
       print each_line_of_text[:-1]
       continue
    gene_id = re.split('\.',text_in_columns[field_no - 1])[0]
    gene_id = gene_id.strip('"')
    if gene_id in Lookup_geneID:
        print text_in_columns[0] + "," + '"' + Lookup_geneID[gene_id] + '"' + "," + text_in_columns[2] + "," + text_in_columns[3] + "," + text_in_columns[4][:-1]
