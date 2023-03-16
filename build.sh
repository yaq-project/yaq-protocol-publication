#!/bin/bash

# manuscript
pdflatex --interaction=nonstopmode paper.tex
bibtex paper.aux
pdflatex --interaction=nonstopmode paper.tex
pdflatex --interaction=nonstopmode paper.tex

# diff
pdflatex --interaction=nonstopmode paper-diff.tex
bibtex paper-diff.aux
pdflatex --interaction=nonstopmode paper-diff.tex
pdflatex --interaction=nonstopmode paper-diff.tex

# SI
pdflatex --interaction=nonstopmode -shell-escape SI.tex
bibtex SI.aux
pdflatex --interaction=nonstopmode -shell-escape SI.tex
pdflatex --interaction=nonstopmode -shell-escape SI.tex
