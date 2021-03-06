#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Jongmin Moon on 2011-05-27.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import csv
import json

def acsvreader(csvfile):
  '''Opens a CSV file and creates a dictionary list of entries using the first row (header) as the key.
  Assumes each header is unique.
  Creates a JSON file using the same filename
  
  Keyword arguments:
  csvfile -- name/path of csvfile
  
  Returns: nothing.
  '''
  #initialize final list
  masterlist = []
  
  #initilize the csv file
  #keep on wanting to type scv
  reader = csv.reader(open(csvfile, newline=''))
  
  for arow in reader:
    #get keys from first row
    if reader.line_num == 1:
      col_key = arow
      continue
    #initialize temp list
    thelist = {}
    #match keys with column value
    for col_num, col_value in enumerate(arow):
      thelist[col_key[col_num]] = col_value
    masterlist.append({'record':thelist})
  
  #get the filename
  if '/' in csvfile:
    (dirname, filename) = os.path.split(csvfile)
    (shortname, extension) = os.path.splitext(filename)
  else:
    (shortname, extension) = os.path.splitext(csvfile)
  
  #create JSON file using filename
  JSONname = shortname + '.json'
  with open(JSONname, mode='w', encoding='utf-8') as f:
    json.dump(masterlist, f, indent=2)