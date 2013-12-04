# Makefile for XGH scripts

clean:
	@echo "Cleaning..."
	@rm -rf news_html
	@rm -rf news_txt

search:
	@./query_es.sh > News.json

fetch:
	@mkdir news_html
	python get_news.py News.json news_html

convert_txt:
	@mkdir news_txt
	python html2txt.py news_html news_txt

all: clean search fetch convert_txt
