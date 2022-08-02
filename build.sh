#!/bin/bash
pdflatex --interaction=nonstopmode paper.tex
bibtex paper.aux
pdflatex --interaction=nonstopmode paper.tex
pdflatex --interaction=nonstopmode paper.tex
