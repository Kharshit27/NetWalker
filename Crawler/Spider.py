from urllib2 import *
from bs4 import BeautifulSoup
from robotparser import RobotFileParser

"""
        Developed by: Prateek Jha, 15 May 2017
"""

class spider(object):
    CurLink = ""
    linknText = []
    headings = []

    def __init__(self, link):
        self.CurLink = link
        self.r = RobotFileParser()

    def crawl(self):
        self.r.set_url(urlparse.unquote(self.CurLink))
        self.r.read()

        self.html = urlopen(self.CurLink).read()
        self.bs = BeautifulSoup(self.html, "lxml")

        for i in self.bs.findAll("h1", text=True):
            self.headings.append(i.text)
        for i in self.bs.findAll("h2", text=True):
            self.headings.append(i.text)
        for i in self.bs.findAll("h3", text=True):
            self.headings.append(i.text)
        for i in self.bs.findAll("h4", text=True):
            self.headings.append(i.text)
        for i in self.bs.findAll("h5", text=True):
            self.headings.append(i.text)
        for i in self.bs.findAll("h6", text=True):
            self.headings.append(i.text)

        for link in self.bs.findAll('a',href=True):
            aLink = urlparse.urljoin(self.CurLink,link['href'])

            if(self.r.can_fetch("*",aLink)):
                self.linknText.append({"URL": aLink,
                              "AnchorText": link.string})