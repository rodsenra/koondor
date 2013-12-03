import codecs
from glob import glob 
import os
import sys
from bs4 import BeautifulSoup

dirpath = os.path.join(sys.argv[1], "*.html")
for filename in glob(dirpath):
	html_file = codecs.open(filename, "r", encoding="utf-8")
	soup = BeautifulSoup(html_file.read())
        print soup.find_all('div', class_='materia-conteudo')
	html_file.close()
