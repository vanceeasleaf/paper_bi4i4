TEX = pdflatex

pdf : paper.tex
	if [ ! -d "bin" ]; then mkdir bin ; fi;
	cd  bin/;$(TEX) ../paper.tex
	 
.PHONY:clean

clean : 
	rm -r bin
