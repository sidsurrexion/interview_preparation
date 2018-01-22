from html.parser import HTMLParser
from os.path import expanduser
from os import listdir
from os.path import isfile, join


my_path = expanduser("~") + "/Downloads/Calls"
actual_data = ['q', 'span', 'title']


class Entities(object):
    def __init__(self):
        self.is_body = False
        self.value = []
        self.needs_data = False
        self.actual_data = ['q', 'span', 'abbr']

    def correct_values(self):
        return [i for i in self.value if i]


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attributes):
        if tag == 'body':
            entities.is_body = True
        if entities.is_body:
            if tag in entities.actual_data:
                entities.needs_data = True
            else:
                entities.needs_data = False

    def handle_endtag(self, tag):
        if tag == 'body':
            entities.is_body = False
            print('|'.join(entities.correct_values()))

    def handle_data(self, data):
        if entities.needs_data and entities.is_body:
            data = data.replace(':', '')
            data = data.replace('\n', '')
            entities.value.append(data)

only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
for path in only_files:
    path = my_path + '/' + path
    info = ""
    with open(path, 'r') as file:
        for l in file:
            info += l
    entities = Entities()
    parser = MyHTMLParser()
    parser.feed(info)
