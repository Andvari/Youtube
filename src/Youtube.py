'''
Created on 24.04.2012

@author: nemo
'''

import urllib2


content = open("crazy_frog.flv", "wb")

print "Find file"
url = "http://o-o.preferred.comstar-svo1.v1.lscache6.c.youtube.com/videoplayback?upn=w2j-NwTKWFM&sparams=algorithm%2Cburst%2Ccp%2Cfactor%2Cid%2Cip%2Cipbits%2Citag%2Csource%2Cupn%2Cexpire&fexp=904532%2C919303%2C906504&algorithm=throttle-factor&itag=34&ip=62.0.0.0&burst=40&sver=3&signature=D22770A7853159209FBD1B9A71E17E4644685596.CF06F2A9EE23BED4C9CFD4B9A5F93F85956CAA46&source=youtube&expire=1334503953&key=yt1&ipbits=8&factor=1.25&cp=U0hSSVVLUV9KTUNOMl9NRVVKOkV5bHhobnMwSGR2&id=93ce6644faaf31b1&ptk=vevo&ptchn=CrazyFrogVEVO&cm2=1"
req = urllib2.urlopen(url)

page = req.read()

print "File is read"
 
content.write(page)

print "Stop"