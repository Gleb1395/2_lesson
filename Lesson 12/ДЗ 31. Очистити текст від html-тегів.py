from bs4 import BeautifulSoup
import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        soup = BeautifulSoup(html, 'lxml')
        file_writing = open('cleaned.txt', 'w')
        file_writing.write(soup.text)
        file_writing.close()
        return result_file
delete_html_tags('draft.html')


