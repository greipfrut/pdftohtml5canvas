# Introduction

HTML5 files using canvas elements may sometimes be an easier format to extract useful elements (e.g. time series waveforms).

We found that waveforms embedded in pdfs keep a predictable structure when going from PDF->SVG->HTML5 Canvas.

Previously, this required opening up in Inkscape and saving as an HTML5 Canvas file.  Not bad for a few files, but >5k files, it becomes useful to automate.

# Usage

python pdftohtml5canvas.py DIRECTORYofPDFs