
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
import sys

import setproctitle

from ebay.Kl import Kl
from utils import item_cache
from utils.print_list import print_list
from utils import notifications

from jobs import search_runner
    
def main():

    setproctitle.setproctitle("test")
    
    while True:
        print("WAITING...")
        time.sleep(60)

    return


    search_strings = ["canon ef l defekt",
                      "canon ef usm defekt",
                      "canon ef 85 defekt",
                      "canon 70 200 defekt",
                      "canon ef"]

    search_runner.start_search_runners(search_strings)

    while True:
        #items = Kl.search("canon ef")
        #new_items = item_cache.cache_new(items)

        #if new_items:
        #    notifications.notify_ads(new_items)

        print("WAITING...")
        time.sleep(60)


if __name__ == '__main__':
    main()
