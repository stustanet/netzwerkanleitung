OUT := build

.PHONY: stusta_de stusta_en mb67_de mb67_en all clean cleanall

all: stusta_de stusta_en mb67_de mb67_en cleanall

stusta_de: Netzwerkanleitung.pdf
stusta_en: Netzwerkanleitung_EN.pdf
mb67_de: Netzwerkanleitung_mb.pdf
mb67_en: Netzwerkanleitung_EN_mb.pdf

%.pdf: %.tex
	latexmk -interaction=nonstopmode -outdir=$(OUT) -shell-escape -pdf -halt-on-error $*.pdf

cleanall:
	latexmk -C

clean:
	latexmk -c
