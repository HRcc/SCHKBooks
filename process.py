#	Image is a part of external library PIP
import Image

#	Initial config
cols = 2
rows = 3
pages = 150
# 	/END

#	Folder for source images
input_dir = "input/"

#	2D list to store images
parts = [["" for x in xrange(cols)] for x in xrange(rows)]

#	For every page we want to create...
for pages_id in xrange(1,pages+1):

	page_width = 0
	page_height = 0

	#	... get all the pieces...
	for cols_id in xrange(0,cols):
		for rows_id in xrange(0,rows):
			parts[rows_id][cols_id] = Image.open(input_dir + "l=4&r=" +str(rows_id)+ "&c=" +str(cols_id)+ "&date=20080101&pub_id=93&iss_id=7995&pageno=" +str(pages_id)+ "&s=182f58059c916d47ced08804afb859e3.jpg")

	#	... and it's dimensions ...
	for index in xrange(0,cols):
	 	page_width += parts[0][index].size[0]

	for index in xrange(0,rows):
		page_height += parts[index][0].size[1]

	# 	... to be able to create complete page ...
	new_page = Image.new("RGB", (page_width, page_height))

	x = 0
	y = 0

	#	... filled with image parts.
	for cols_id in xrange(0,cols):
		for rows_id in xrange(0,rows):
			new_page.paste(parts[rows_id][cols_id], (x,y))
			y += parts[rows_id][cols_id].size[1]
		x += parts[rows_id][cols_id].size[0]
		y = 0

	#	Save & profit ...
	new_page.save("output/page%03d.jpg" % pages_id)

	print "Page %3d out of %d" % (pages_id, pages)
