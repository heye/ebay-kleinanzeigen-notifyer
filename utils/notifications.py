
from utils.mail import send_sendgrid


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

    send_sendgrid("Neue Angebote!", "", message, "heye.everts.1@gmail.com")
