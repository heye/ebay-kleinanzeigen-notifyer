import os
import json
import traceback

from utils.mail import send_sendgrid



def get_mail_receivers():
    data = ""

    try:
        file_path = "mail_receivers.txt"

        if not os.path.isfile(file_path):
            return data

        #print("STORAGE READ " + file_path)
    
        with open(file_path, 'r+') as temp_file:
            data = temp_file.read()


        if not data:
            return []

        return json.loads(data)
    except:
        traceback.print_exc()

    return []


def notify_ads(new_ads):
    #say("You have new ads!")
    #say(adname)
    if not new_ads:
        print("NO NEW ADS")
        return

    message = "<h2>Neue Ebay Kleinanzeigen Angebote:</h2>"
    link_prefix = "https://www.ebay-kleinanzeigen.de"


    for one_ad in new_ads:
        ad_link = one_ad.get("link", "")
        ad_title = one_ad.get("descr", "")
        one_ad_text = """<a href='{}'> {} </a><br>""".format(link_prefix + ad_link, ad_title)

        message += one_ad_text

    print("MAIL: " + message)

    mail_receivers = get_mail_receivers()
    for one_mail in mail_receivers:
        send_sendgrid("Neue Angebote!", "", message, one_mail)
