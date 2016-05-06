#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pdftohtml5canvas.py
A helper module to convert a folder of pdfs into html5 canvas files

This program is free software; you can redistribute it and/or modify
it.
"""
import sys
from sys import platform as _platform
import os
from ink2canvas.main import Ink2Canvas

if _platform == 'win32':
	# Relative path to the command line executable for pdf-to-svg conversion (Windows)
	pdf2svg_exe = os.path.normpath("pdf2svg\dist-32bits\pdf2svg.exe")
elif _platform == 'win64':
	# Relative path to the command line executable for pdf-to-svg conversion (Windows)
	pdf2svg_exe = os.path.normpath("pdf2svg\dist-64bits\pdf2svg.exe")
elif _platform == 'darwin':
	# If on a Mac, install pdf2svg with homebrew: brew install pdf2svg
	pdf2svg_exe = 'pdf2svg'
elif _platform.startswith('linux'):
	pdf2svg_exe = 'pdf2svg'

# If user does not pass in a path to PDFs, assume it is in the current working directory
try:
	dir_of_pdfs = os.path.normpath(sys.argv[1])
except IndexError:
	dir_of_pdfs = os.getcwd()

# Loop through each file in the directory of pdfs
for root, dirs, files in os.walk(dir_of_pdfs):
    for file in files:
        if file.lower().endswith('.pdf'): # use .lower() in case some pdfs are saved w/.PDF extension
        	output_filename = os.path.splitext(file)[0]+'.svg' # Create the output SVG filename
        	output_html = os.path.splitext(file)[0]+'.html' # Create the output html5 canvas filename
        	
        	# Call the pdf2svg executable to convert pdf to SVG
        	os.system('%s "%s" "%s" 1'%(pdf2svg_exe, os.path.join(dir_of_pdfs, file), os.path.join(dir_of_pdfs, output_filename)))

        	# Create an Ink2Canvas object to convert SVG to HTML5 Canvas
        	i2c = Ink2Canvas()
        	# Load in the SVG file and parse
        	i2c.parse(os.path.join(dir_of_pdfs, output_filename))
        	i2c.effect()

        	# Open up an html5 file for writing, output it, then close the file
        	output_file = open(os.path.join(dir_of_pdfs, output_html), 'w')# open(dir_of_pdfs+output_html, 'w')
        	content = i2c.core.canvas.output()
        	output_file.write(content.encode("utf-8"))
        	output_file.close()