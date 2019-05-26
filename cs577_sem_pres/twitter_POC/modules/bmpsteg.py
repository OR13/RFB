#!/usr/bin/python
"""
modified from: http://johannes.jakeapp.com/blog/category/happy-hacking/200701/python-steganography
no longer requires sys or filesystem access

"""
import StringIO

# all input should be StringIO objects
def put(fin, fout, fmsg):

	if fin.getvalue()[:2] != 'BM':
		print 'No Bitmap!'
		return
	
	offset = fin.getvalue()[10:13]
	offset = ord(offset[0]) + (ord(offset[1])<<8) + (ord(offset[2])<<(8*2))

	header = fin.getvalue()[:offset]
	fout.write(header)
	msg = fmsg.read()
	
	def strbit(txt,j):
		v = txt[j/8]
		b = j%8
		return int(1 << (7-b) & ord(v) != 0)
	
	j = 0
	

	seek = offset
	while 1:
		b = fin.getvalue()[seek:seek+1]
		seek += 1
		if b == '': 
			break
		val = ord(b)
		if(j/8<len(msg)):
			val = (val/2)*2 | strbit(msg,j)
		elif j/8<len(msg)+1:
			val = (val/2)*2 | 0
		fout.write(chr(val))
		j = j + 1
    
# all input should be StringIO objects
def get(fin):
	def dec2bin(b):
		for i in range(8):
			print int(1 << (7-i) & b != 0),
		print '	',b,'	',hex(b), '	',b
	
	if fin.getvalue()[:2] != 'BM':
		print 'No Bitmap!'
		return
	
	offset = fin.getvalue()[10:13]
	
	offset = ord(offset[0]) + (ord(offset[1])<<8) + (ord(offset[2])<<(8*2))
	
	seek = offset
	j = 0
	c = 0
	msg = ''
	while 1:
		b = fin.getvalue()[seek:seek+1]
		seek += 1
		if b == '': 
			break
		if ord(b)%2 == 1:
			c = c |   (1<<(7-j%8))
		if j%8 == 7:
			if c==0: break
			msg = msg + chr(c)
			c = 0
		
		j = j + 1
	return msg





