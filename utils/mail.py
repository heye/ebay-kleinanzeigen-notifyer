import traceback
import smtplib
from email.message import EmailMessage

#sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(subject: str, content: str, content_html: str, toAddr: str):

    #receivers = one_mail.get(dbns.mail_outbound.receivers,[]) 
    #toAddr = ", ".join(receivers) 

    mail_server = "wp12381010.mailout.server-he.de"
    mail_port = "587"
    mail_user = "wp12381010-alerts"
    mail_passwd = "#f%fsdfdGFDf45"
    mail_from_addr = "alerts@cloudplan.net"

    msg = EmailMessage() 
    msg.set_content(content) 
    msg.add_alternative(content_html, subtype='html') 
    msg['Subject'] = subject 
    msg['From'] = mail_from_addr 
    msg['To'] = toAddr 

    try: 
        # Send the message via our own SMTP server. 
        conn = smtplib.SMTP(mail_server,mail_port) 
        conn.ehlo() 
        conn.starttls() # enable TLS 
        conn.ehlo() 
        conn.login(mail_user, mail_passwd) 
        conn.send_message(msg) 
        conn.quit() 

    except Exception as e: 
        traceback.print_exc()


def send_sendgrid(subject: str, content: str, content_html: str, toAddr: str):

    api_key = "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"
    mail_from_addr = "info@rimworld.me"

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
    except Exception as e:
        print(e.message)



def main():
    send_sendgrid("testsub", "testtext", "<h2>testhtml</h2>", "heye.everts.1@gmail.com")
        

if __name__ == '__main__':
    main()
