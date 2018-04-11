#!/usr/bin/env python
import os
import sys
import qrcode
import time

if len(sys.argv) < 2:
	print "usage:%s filename.txt"
	exit()

# You can add prefix if you need
prefix = ''

for line in open(sys.argv[1]):
	if line != '\n':
		# add prefix
		data = prefix+line[0:-1]
		# the filename
		name = line[0:-1] + '.png'
		# print data, len(data), name	
		qrcode_image = qrcode.make(data)
		qrcode_image.save(name)
		print(name + " created.")
		time.sleep(0.1)
