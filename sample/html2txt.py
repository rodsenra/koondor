import codecs
from glob import glob
import os
import sys
from bs4 import BeautifulSoup

dir_with_news_html = sys.argv[1]
dir_with_news_txt = sys.argv[2]

dirpath = os.path.join(dir_with_news_html, "*.html")
for filename in glob(dirpath):
    html_file = codecs.open(filename, "r", encoding="utf-8")
    soup = BeautifulSoup(html_file.read())
    try:
        print "Converting " + filename
        txt_content = soup.find_all('div', class_='materia-conteudo')[0].text
        txt_content = txt_content.replace('\n', ' ')
        txt_file = os.path.join(dir_with_news_txt, os.path.basename(filename))
        txt_file = txt_file.replace('.html', '.txt')
        codecs.open(txt_file, "wb", encoding="utf-8").write(txt_content)
    except IndexError:
        pass
    html_file.close()
