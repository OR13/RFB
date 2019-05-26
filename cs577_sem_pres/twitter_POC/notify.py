#!/usr/bin/python

import pycurl, tweepy, urllib, Image, StringIO, base64

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET, TWITTER_USER, IMGUR_API_KEY, IMGUR_API_URL, RFB_AUTH
from modules import bmpsteg

#takes a command returns an image
def hide(cmd):
	try:
		print "loading %s " % cmd['U'],
		img = Image.open(StringIO.StringIO(urllib.urlopen(cmd['U']).read()))
		print "DONE"
	except Exception as e:
		raise Exception("Error loading image from command: %s" % e)
	
	print "converting image to bmp...",
	src = StringIO.StringIO()
	img.save(src, format="BMP")
	print "DONE"

	dst = StringIO.StringIO()
	msg = StringIO.StringIO(cmd['C'])

	print "hiding message in image with bmpsteg...",
	bmpsteg.put(src, dst, msg)
	print "DONE"

	print "confirming message is hidden...",
	assert cmd['C'] == bmpsteg.get(dst)
	print "DONE"
	
	return dst.getvalue()

#takes a image returns a link
def upload(img):
	print "encoding image to base64 and uploading to imgur...",
	c = pycurl.Curl()
	response = StringIO.StringIO()
	values = [("key", IMGUR_API_KEY), ("image", base64.b64encode(img))]
	c.setopt(c.URL, IMGUR_API_URL)
	c.setopt(c.HTTPPOST, values)
	c.setopt(c.WRITEFUNCTION, response.write)
	c.perform()
	c.close()
	response = response.getvalue()
	print "DONE"
	return response[response.index('<original>') + 10:response.index('</original>')]

#tweets a message and a link
def notify(msg, link):
	print "tweet url to image and message if present",

	if len(msg) + len(link) > 138:
		tweet = "%s...%s" % (msg[0: 140 -len(link)-3], link)
	else:
		tweet = "%s: %s" % (msg, link)
	api.update_status(tweet)
	print "DONE"
	return tweet
	
if __name__ == "__main__":
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	#retrive dm's and find command messages
	cmds = [eval(t.text) for t in api.direct_messages() if RFB_AUTH in t.text]

	notifications = []

	for c in cmds:
		img = hide(c)
		link = upload(img)
		notifications.append(notify(c['M'], link))

	print "new notifications:"
	for n in notifications:
		print n
	print "exiting...",







