#!/usr/bin/python

import urllib, Image, StringIO, os, sys

from modules import bmpsteg

	
def usage():
	print 'usage: python retrieve.py <url or path to image>'

if __name__ == "__main__":
	try:
		if os.path.isfile(sys.argv[1]):
			img = Image.open(StringIO.StringIO(open(sys.argv[1], 'r').read()))
		else:
			img = Image.open(StringIO.StringIO(urllib.urlopen(sys.argv[1]).read()))

		src = StringIO.StringIO()
		img.save(src, format="BMP")

		print bmpsteg.get(src)	
	except Exception as e:
		print e
		usage()



