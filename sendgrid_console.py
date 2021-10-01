import smtplib
from email.mime.text import MIMEText

port = 25
sender = str(input("Enter your sender email: "))
receiver = str(input("Enter your receiver email: "))
subject = str(input("Enter your subject: "))
body = str(input("Enter your single line message: "))
password = str(input("Enter your sendgrid api key: "))

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver
user = 'apikey'

with smtplib.SMTP("smtp.sendgrid.net", port) as server:
    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")