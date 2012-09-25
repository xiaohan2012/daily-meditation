#-*- coding:utf8 -*-
import pprint
from urllib import urlencode

from apiclient.discovery import build


api_key = "AIzaSyARzNbx5Xmu0ZVoMm7MMS_zXntdq4kbYgA"
cx = "014141307287823979686:6egots93ndu"

def search(keyword,start_index = None):
# Build a service object for interacting with the API. Visit
# the Google APIs Console <http://code.google.com/apis/console>
# to get an API key for your own application.
    service = build("customsearch", "v1",
            developerKey=api_key)
    query = {"cx":cx,
            "q":keyword,
            }
    if start_index:#first query does not need `start` parameter
        query["start"] = start_index
    res = service.cse().list(** query).execute()

    #pprint.pprint(res)
    return res

if __name__ == '__main__':
    keyword = u"语不惊人死不休"
    next_index = None
    while True:
        res = search(keyword,next_index)
        for i in res["items"]:
            if keyword in i["title"]:
                print i["link"]
        try:            
            next_index = res["queries"]["nextPage"][0]["startIndex"]
        except KeyError:            
            if not next_page:
                print "no more result"
                break
