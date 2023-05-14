import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# requires 'allow less secure apps' to be turned on
def send_message(address_sender: str, password: str, address_recipient: str, subject: str, message: str):
    # configure SMTP server && login 
    try:
        s = smtplib.SMTP(host="smtp.gmail.com", port=587)
        s.starttls()
        s.login(address_sender, password)
    except:
        return False
    # create message
    msg = MIMEMultipart()
    msg["From"] = address_sender
    msg["To"] = address_recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(message))
    # send Message
    try:
        msg.send
    except:
        return False
    return True

