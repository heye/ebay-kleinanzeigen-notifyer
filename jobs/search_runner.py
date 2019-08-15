import threading
from typing import Dict, Tuple, List
import time


from jobs.job_mgr import job_mgr
from ebay.Kl import Kl
from utils import item_cache
from utils.print_list import print_list
from utils import notifications


def search_runner(search_string: str):
    filename = search_string.replace(" ", "_")

    while not job_mgr.do_stop:
        items = Kl.search(search_string)
        new_items = item_cache.cache_new(items, filename)

        if new_items:
            print("NEW NEW NEW FOR SEARCH " + filename)
            print_list(new_items)
            notifications.notify_ads(new_items)

        print("WAITING... " + filename + " TOTAL " + str(len(items)))
        time.sleep(60)


def start_search_runners(search_string_list: List[str]):
    threads = []

    for one_search_string in search_string_list:
        print("STARTING " + one_search_string)
        one_thread = threading.Thread(target=search_runner, args=[one_search_string])
        threads.append(one_thread)

        one_thread.start()

