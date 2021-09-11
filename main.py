
from email import encoders
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


 
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "poingshop@gmail.com"
body = "This is an email with attachment sent from Python"
password = input("what is your password of your email? ")


context = ssl.create_default_context()

with open("emails.txt", 'r') as f:
    emlist = f.readlines()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)


    for email in emlist:
        receiver_email = email
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Bcc"] = receiver_email 
        message.attach(MIMEText(body, "plain"))
       
       
        filename="resume.pdf"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)
        text = message.as_string()
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        server.sendmail(sender_email, receiver_email, text )
except Exception as e:
    print(e)
finally:
    server.quit()

    # این پروژه نهاییست