.PHONY: all clean generate-publications build-cvs academic industry

all: generate-publications build-cvs

generate-publications:
	python3 cv/scripts/generate_publications.py

build-cvs: academic industry

academic:
	cd cv/academic && pdflatex cv_academic.tex
	cd cv/academic && pdflatex cv_academic.tex
	mkdir -p assets/files
	cp cv/academic/cv_academic.pdf assets/files/CV_Academic_YourName.pdf

industry:
	cd cv/industry && pdflatex cv_industry.tex
	cd cv/industry && pdflatex cv_industry.tex
	mkdir -p assets/files
	cp cv/industry/cv_industry.pdf assets/files/CV_Industry_YourName.pdf

clean:
	rm -f cv/academic/*.aux cv/academic/*.log cv/academic/*.out
	rm -f cv/industry/*.aux cv/industry/*.log cv/industry/*.out