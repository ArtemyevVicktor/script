# coding: utf8
from PIL import Image
import sys

flag_display_message = "yes"

def convert(source_file,output_file):
	if source_file[-4:len(source_file)]=='.jpg':
		try:
				im = Image.open(source_file)
				if output_file[-4:len(output_file)]!='.pdf':
					output_file = output_file+'.pdf'
				im.save(output_file, save_all=True)
				display_message ("File "+source_file+" convert and save as "+output_file+", success!",flag_display_message)
				im.close()
		except:
				display_message ("Could not open image!",flag_display_message)
	else:
		display_message ("This source file no .jpg or bad name file",flag_display_message)
	
def display_message(text,flag_display_message):
	if flag_display_message != 'no':
		print (text)

if len (sys.argv) >= 4:
	flag_display_message = sys.argv[3]
	convert(sys.argv[1],sys.argv[2])
if len (sys.argv) == 3:
	convert(sys.argv[1],sys.argv[2])
