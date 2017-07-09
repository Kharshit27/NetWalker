from Spider import spider
from Database import *
from threading import Thread

"""
        Developed by: Prateek Jha, 15 May 2017
"""

linkCount = curCount = 0
i=0
url = "***************"
initialize(linkCount,url)
while(i<5):
    spiderLeg = spider(getNext(curCount))
    curCount += 1
    spiderLeg.crawl()
    linkCount = insertDB(spiderLeg.linknText,spiderLeg.headings,url,linkCount)
    print "Test Completed Successfully!!"
    i+=1