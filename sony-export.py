import sys
from xml.dom.minidom import parse

# Full path to your cacheExt.xml
if len(sys.argv) != 2:
	sys.stderr.write("usage: " + sys.argv[0] + " <inputfile>")
	sys.exit(1)
 
doml = parse(sys.argv[1])
for text in doml.getElementsByTagName("text"):
	bookFilePath = text.getAttribute("path")
	notes = []
	markups = text.getElementsByTagName("markups")
	if markups:
		for annotation in markups[0].getElementsByTagName("annotation"):
			content = annotation.getAttribute("name")
			date = annotation.getAttribute("date")
			page = annotation.getAttribute('page')
			notes.append((content, page, date))
	if notes:
		print bookFilePath.encode('utf-8')
		for note in notes:
			print "%s\tp%s\t%s" % (note[0].encode('utf-8'),
								  note[1].encode('utf-8'),
								  note[2].encode('utf-8'))
			print