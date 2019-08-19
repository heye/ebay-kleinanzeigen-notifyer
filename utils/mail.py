import traceback
import smtplib
import os
from email.message import EmailMessage

#sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def get_api_key():
    data = ""

    try:
        file_path = "sendgrid_api_key.txt"

        if not os.path.isfile(file_path):
            return data

        #print("STORAGE READ " + file_path)
    
        with open(file_path, 'r+') as temp_file:
            data = temp_file.read()
    except:
        traceback.print_exc()

    return data.strip()


def send_sendgrid(subject: str, content: str, content_html: str, toAddr: str):

    api_key = get_api_key()
    mail_from_addr = "info@rimworld.me"

    print("MAIL KEY " + api_key)

    message = Mail(
    from_email=mail_from_addr,
    to_emails=toAddr,
    subject=subject,
    html_content=content_html)
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except:
        traceback.print_exc()



def main():
    send_sendgrid("testsub", "testtext", "<h2>testhtml</h2>", "heye.everts.1@gmail.com")
        

if __name__ == '__main__':
    main()
