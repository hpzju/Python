import smtplib, ssl
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
port = 465  # For SSL
user = "hpzjuplus@gmail.com"
password = "hpzju1986@GG"

from_mail = user
to_mails = ["hubert_hao@foxmail.com"]

msg = EmailMessage()
msg.set_content("hello, send from python smtplib, ssl, and email")
msg['Subject'] = 'Automail from Python smtplib, ssl and email'
msg['From'] = from_mail
msg['To'] = ", ".join(to_mails)


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context, timeout=60) as server:
    server.set_debuglevel(1)
    server.login(user, password)
    server.send_message(msg)
    print("MSG Send!")
    server.quit()