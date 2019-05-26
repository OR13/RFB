TODO:
	Write command script 

WTF do these python scripts do?

	notify.py   - checks botmaster's twitter for commands from botherder and forwards commands to bots in form of status updates
	embed.py    - embeds a message/command in an image specified by url or path
	retrieve.py - retrieves a command/message hidden in a url or file

WTF is acutally working right now?

	If you are looking at this code, then you can checkout http://twitter.com/#!/tweeebot
	Pick a tweet posted by the notify script and copy the link...
	then use the retrieve script to see whats up: python retrieve.py http://t.co/WnhIK5Tr
	even though the url has been shortened, retrieve is not fooled and tell you straight up: DDOS 127.0.0.1
	The other scripts aside from command are pretty much all working too


Description of Current Algorithm:

	Read DM's with tweepy.
	Load last tweeted DM Command from DB

	For Each DM Command after the last tweeted one do:
		Get Image included in DM command
		Embed command message in image
		Upload image to IMGUR
		Tweet with link to Image
	
	In the future commands should be in the form of DMing or mentioning a link at the Bot Master.
	The Bot Master should then Check each of the images and if they contain a command, 
	use the notify script to forward the command
	
Description of Command Message Syntax:

	C - Command (to be hidden in U)
	M - Message (will be visible in post)
	U - URL to image which will be used
	X - Authentication Token (like a password)

	cmd = {
		'C':'DDOS 127.0.0.1', 
		'M':'#HERP', 
		'U':'http://images.cheezburger.com/avatarstore/5348499/129477805135784822.bmp', 
		'X':'4SCIENCE'
	}


Some Usefull image feeds:

	http://pixdaus.com/rss.php
	http://pipes.yahoo.com/pipes/pipe.run?_id=1ed332df999d6d560ddead48010ae094&_render=json

