#!/bin/bash
pdflatex --interaction=nonstopmode paper.tex
bibtex paper.aux
pdflatex --interaction=nonstopmode paper.tex
pdflatex --interaction=nonstopmode paper.tex
#
pdflatex --interaction=nonstopmode SI.tex
bibtex SI.aux
pdflatex --interaction=nonstopmode SI.tex
pdflatex --interaction=nonstopmode SI.tex
