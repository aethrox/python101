# XML Processing

import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "book":
            print("----- BOOK -----")
            print("ID: {}".format(attrs['id']))
    def characters(self, content):
        if self.current == "author":
            self.author = content
        elif self.current == "title":
            self.title = content
        elif self.current == "genre":
            self.genre = content
    def endElement(self, name):
        if self.current == "author":
            print("Author: {}".format(self.author))
        elif self.current == "title":
            print("Title: {}".format(self.title))
        elif self.current == "genre":
            print("Genre: {}".format(self.genre))
        self.current = ""
            

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('books.xml')