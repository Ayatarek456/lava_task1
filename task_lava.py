# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:48:53 2021

@author: CompuLand
"""

""
import hashlib
import glob
read_files = glob.glob("*.yml")

with open("result.yml", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
  #this file finalllllllllllllll to eliminate ant duplication          
output_file_path=open(r"C:\Users\CompuLand\Downloads\translations\translations\translate_one.yml","w") 
#output_file_path="C:\\Users\CompuLand\Downloads\translations\translations\result.yml") 
#input_file_path ="C:\\Users\CompuLand\Downloads\translations\translations\all_yml.yml")
completed_lines_hash = set()
#input_file=input_file_path
#output_file = open(output_file_path, "w") 
for line in open(r"C:\Users\CompuLand\Downloads\translations\translations\result.yml","r"):
  #5
  if (str(' http_code')) in line:
        output_file_path.writelines(line)
        continue

    
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file_path.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file_path.close()