#!/usr/bin/env python
# encoding: utf-8
"""
classes.py

Created by Jongmin Moon on 2011-05-06.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os

def listdir(targetdir):
	'''Create an extensive list of the specified directory including all the files and subdirectories. Default directory is user HOME directory.
	
	Keyword arguments:
	targetdir -- specify the target directory. can be relative or absolute.
	
	Returns: nothing. just creates a JSON file.
	'''
	masterlist = []
	
	if targetdir == False:
		raise ValueError('Must designate a directory.')
	else:
		for root, dirs, files in os.walk(targetdir):
			splitroot = root.split('/')
			splitroot.reverse()
			dirname = splitroot[0]
			masterlist.append(
				{'directory':
					{'dirname':dirname,
					'path':root,
					'subdirs':dirs,
					'files':getfileinfo(files, root)}})
		with open('listdir.json', mode='w', encoding='utf-8') as f:
				json.dump(masterlist, f, indent=2)

def getfileinfo(afilelist, apath):
  '''Takes a list of files with the path to the files and returns a dictionary containing the filename and metadata
  
  Keyword arguments:
  afilelist -- list of files
  apath -- filepath
  
  Returns: Dictionary list of file metadata.
  '''
  metadatalist = []
  for afile in afilelist:
    themetadata = os.stat(os.path.join(apath,afile))
    metadatalist.append(
      {'filename':afile,'filesize':themetadata.st_size,'accessed':themetadata.st_atime,'modified':themetadata.st_mtime})
  return metadatalist