from pymongo import MongoClient

"""
        Developed by: Prateek Jha, 15 May 2017
"""

Client = MongoClient()
db = Client["CrawlData"]
linkData = db["linkData"]
linkList = db["linkList"]

def initialize(linkCount, curURL):
    linksD = {"_id": linkCount,
              "URL": curURL}
    linkList.insert_one(linksD)

def insertDB(linksDetails, heading, curURL, linkCount):
    for i in linksDetails:
        if(linkList.find({"URL":i["URL"]}).count() == 0) and i["URL"]!="javascript:void(0)":
            linkCount += 1
            linksD = {"_id": linkCount,
                      "URL": i["URL"]}
            linkList.insert_one(linksD)

    post = {"URL": curURL,
            "Headings": heading,
            "TotaLinks": len(linksDetails),
            "Anchors": linksDetails
            }
    linkData.insert(post)

    return linkCount

def getNext(curCount):
    l = linkList.find_one({"_id":curCount})
    return l["URL"]