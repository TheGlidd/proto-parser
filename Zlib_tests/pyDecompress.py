#!/usr/bin/env python2.7
 
import zlib
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('rb'))
parser.add_argument('offset', type=int, default=0)
args = parser.parse_args()
 
magic_list = [
               "\x08\x3c", "\x08\x7a", "\x08\xb8", "\x08\xf6",
               "\x18\x38", "\x18\x76", "\x18\xb4", "\x18\x72",
               "\x28\x34", "\x28\x72", "\x28\xb0", "\x28\xee", 
               "\x38\x30", "\x38\x6e", "\x38\xac", "\x38\xea", 
               "\x48\x2c", "\x48\x6a", "\x48\xa8", "\x48\xe6", 
               "\x58\x28", "\x58\x66", "\x58\xa4", "\x58\xe2", 
               "\x68\x24", "\x68\x62", "\x68\xbf", "\x68\xfd",
               "\x78\x01", "\x78\x5e", "\x78\x9c", "\x78\xda"
             ]
 
c_data = args.file.read()
 
done = 0
 
try:
  print zlib.decompress(c_data[args.offset:])
except:
  for m in reversed(magic_list):
    try:
      seek_offset = args.offset
 
      while 1:
        seek_offset += c_data[seek_offset:].index(m)
 
        if seek_offset >= 0:
          try:
            print zlib.decompress(c_data[seek_offset:])
            done = 1
            break
          except:
            seek_offset += 1
 
    except:
      pass
 
    if done:
      break
 
args.file.close()

