#!/usr/bin/env python3
# encoding: utf-8
"""
untitled.py

Created by Jongmin Moon on 2011-06-11.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import json
import code

def walkdir(_path):
  '''
  Since the grabdir function is recursive putting the JSON serializer inside it created an infinite loop (I think. I DONT KNOW DAMN IT)
  
  Keyword arguments:
  path -- relative path from cwd to the target folder (absolute path should work too)
  
  Returns: JSON file in the cwd
  '''
  if '.' in _path:
    raise ValueError('Must specify a directory!')
  else:
    dirlist = grabdir(_path)
  
  if '/' or '.' in _path:
    (dirname, filename) = os.path.split(_path)
    (shortname, extension) = os.path.splitext(filename)
  else:
    shortname = _path
  JSONname = shortname + '_list.json'
  
  with open(JSONname, mode='w', encoding='utf-8') as f:
    json.dump(dirlist, f, indent=2)

def grabdir(_path):
  '''
  Recusively walks a specified directory and grabs all subdirectories and files. Files are added as a list with their own key as a child of the directory.
  This took me way too long. I love and hate you python.
  
  Damn it. Remember to catch if the path being specified isnt a directory. Do something about that.
  
  Keyword arguments:
  path -- relative path from cwd to the target folder
  
  Returns: A dict of the folder specified in the path containing all subfolders and files of all levels.
  '''
  files = []
  dirs = []
  result = {}
  for item in os.listdir(_path):
    itempath = os.path.join(_path, item)
    if os.path.isfile(itempath):
      files.append(item)
    elif os.path.isdir(itempath):
      dirs.append(item)
  if files:
    #print(path)
    if _path in result:
      result[_path].update({'files':files})
    else:
      result[_path] = {'files':files}
  if dirs:
    #print(path)
    for adir in dirs:
      subdirpath = os.path.join(_path, adir)
      if _path in result:
        result[_path].update({adir:grabdir(subdirpath)})
      else:
        result[_path] = {adir:grabdir(subdirpath)}
  return result

if __name__ == '__main__':
  #print os.getcwd()
  _path = raw_input('Please specify a directory (e.g. /Users/~): ')
  if os.path.isdir(_path):
    walkdir(_path)
  else:
    raise ValueError('You must specify a directory.')