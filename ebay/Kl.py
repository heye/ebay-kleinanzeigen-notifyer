
import urllib
import os
from typing import Dict, Tuple, List
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from socket import timeout
import traceback
import urllib.error
import re
import json
import time

from utils.print_list import print_list


class Kl:
    #returns an array of documents representing one ad each
    # TODO: describe structure of docs
    @classmethod
    def search(cls, search_string: str) -> Dict[any, any]:
        
        html = cls.read_page(cls.make_url(search_string))
        html_items = cls.split_html(html)
    
        link_prefix = "https://www.ebay-kleinanzeigen.de"

        #deconstruct each ad html into link and description
        addocs = []
        for one_item in html_items:
            addoc = cls.parse_ad(one_item)
            if addoc and addoc.get("link", "").startswith("/s-anzeige"):
                new_link = link_prefix + addoc.get("link", "")
                addoc.update({"link": new_link})
                addocs.append(addoc)
                if len(addocs) >= 10:
                    break

        #print("#### PARSED ####")
        #print_list(addocs)

        return addocs



    @classmethod
    def make_url(cls, search_string: str) -> str:
        search_string_mod = search_string.replace(" ", "-")
        #print(search_string_mod)
        return "http://www.ebay-kleinanzeigen.de/s-" + search_string_mod + "/k0"


    @classmethod
    def read_page(cls, url: str):    
        html = ""
        try:        
            request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})         
            html = urlopen(request, timeout=5).read().decode('utf-8', errors='ignore')
        except :        
            traceback.print_exc()

        if not html:
            print("COULD NOT READ " + url)

        return html

    #get html for each ad element  
    @classmethod
    def split_html(cls, html: str) -> List[str]:
        if not html:
            return {}

        found_ad = False
        ad_begin = "<article class=\"aditem\""
        ad_end = "</article>"
        items = []
        addocs = []
        one_item = ""
        
        #get html for each ad
        for one_line in html.splitlines():
            if not found_ad and ad_begin in one_line:
                found_ad = True
                
            if found_ad:
                one_item += one_line + "\n"

            if found_ad and ad_end in one_line:
                found_ad = False
                items.append(one_item)
                one_item = ""
        #print("FOUND " + str(len(addocs)) + " ADS")

        return items

    @classmethod
    def parse_ad(cls, one_item: str):
        try:
            start = one_item.find("<a ")
            end = one_item.find("</a>")
            descr_start = one_item.find(">", start + 3) + 1
            link_start = one_item.find("href=\"") + 6
            link_end = one_item.find("\"", link_start)
            #print("LINK " + one_item[link_start: link_end])
            #print("DESCR " + one_item[descr_start: end])

            return {"link": one_item[link_start: link_end],
                    "descr": one_item[descr_start: end]}
        except:
            traceback.print_exc()

        return {}