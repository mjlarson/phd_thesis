#echo 'Remember to grep for "LaTeX Warning: Reference" and "multiply defined"!'
lualatex -interaction=nonstopmode mjlarson_thesis.tex
bibtex8 -W mjlarson_thesis
lualatex -interaction=nonstopmode mjlarson_thesis.tex