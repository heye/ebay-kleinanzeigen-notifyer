import threading
from typing import Dict, Tuple, List
import time


from jobs.job_mgr import job_mgr
from ebay.Kl import Kl
from ebay.ebay import ebay

from utils import item_cache
from utils.print_list import print_list
from utils import notifications


def search_runner_kl(search_string: str):
    filename = search_string.replace(" ", "_")
    filename += ".ebay_kl.json"

    headline = "Neue Ebay Kleinanzeigen Angebote"

    while not job_mgr.do_stop:
        items = Kl.search(search_string)
        new_items = item_cache.cache_new(items, filename)

        if new_items:
            print("NEW NEW NEW FOR SEARCH " + filename)
            print_list(new_items)

            notifications.notify_ads(headline, new_items)

        print("WAITING... " + filename + " TOTAL " + str(len(items)))
        time.sleep(60)

def search_runner_ebay(search_string: str):
    filename = search_string.replace(" ", "_")
    filename += ".ebay.json"

    headline = "Neue Ebay Angebote"

    #https://www.ebay.de/sch/i.html?_nkw=canon+ef+defekt&_sop=10

    while not job_mgr.do_stop:
        items = ebay.search(search_string)
        new_items = item_cache.cache_new(items, filename)

        if new_items:
            print("NEW NEW NEW FOR SEARCH " + filename)
            print_list(new_items)
            notifications.notify_ads(headline, new_items)

        print("WAITING... " + filename + " TOTAL " + str(len(items)))
        time.sleep(60)


def start_search_runners(search_string_list: List[str]):
    threads = []

    for one_search_string in search_string_list:
        print("STARTING " + one_search_string)
        one_thread = threading.Thread(target=search_runner_kl, args=[one_search_string])
        threads.append(one_thread)
        one_thread.start()

        #one_thread = threading.Thread(target=search_runner_ebay, args=[one_search_string])
        #threads.append(one_thread)
        #one_thread.start()


