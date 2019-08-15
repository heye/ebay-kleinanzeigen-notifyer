
from typing import Dict, Tuple, List
import traceback
import json

from utils.file_storage import FileStorage
from utils.print_list import print_list

#save new ads and return the ones that were not saved before
def cache_new(item_list: List[Dict[any, any]], filename) -> List[Dict[any, any]]:

    if not item_list:
        return 

    saved_items = get_saved_items(filename)

    #print("##### SAVED #####")
    #print_list(saved_items)

    new_ads_tested = []
    for one_ad in item_list:
        ad_link = one_ad.get("link", "")
        ad_title = one_ad.get("descr", "")
        if not has_link(saved_items, ad_link):
            new_ads_tested.append(one_ad)

            #print("NEW AD: " + str(one_ad))

    #print("##### NEW #####")
    #print_list(new_ads_tested)

    write_ads(filename, item_list)

    return new_ads_tested


def write_ads(filename: str, item_list: List[Dict[any, any]]):
    #print("WRITE ADS")
    storage = FileStorage()
    storage.setup(filename)
    storage.write_file(json.dumps(item_list))


def get_saved_items(filename: str):
    try:
        storage = FileStorage()
        storage.setup(filename)
        data = storage.read_file()
        if not data:
            return []

        return json.loads(data)
    except:
        traceback.print_exc()

    return []


def has_link(ads: List[Dict[any, any]], link: str):
    for one_ad in ads:
        if link == one_ad.get("link", ""):
            return True

    return False

