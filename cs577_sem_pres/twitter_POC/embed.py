#!/usr/bin/python

import urllib, Image, StringIO, os, sys

from modules import bmpsteg

def usage():
	print 'usage: python embed.py <url|path to src img> <output file name> <path to command file>'

if __name__ == "__main__":
	try:
		if os.path.isfile(sys.argv[1]):
			img = Image.open(StringIO.StringIO(open(sys.argv[1], 'r').read()))
		else:
			img = Image.open(StringIO.StringIO(urllib.urlopen(sys.argv[1]).read()))

		if not os.path.isfile(sys.argv[3]):
			usage()
			sys.exit(1)

		src = StringIO.StringIO()
		img.save(src, format="BMP")

		dst = StringIO.StringIO()

		msg = StringIO.StringIO(open(sys.argv[3], 'r').read())

		bmpsteg.put(src, dst, msg)

		open(sys.argv[2], 'w').write(dst.getvalue())

	except Exception as e:
		print e
		usage()






