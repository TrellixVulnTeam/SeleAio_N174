import email, smtplib, ssl
import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
context = ssl.create_default_context()
server= smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
sender_email = ""
password = ""
filename = ""
def login():
    try:
        server.login(sender_email, password)
    except Exception:
        return("At least one of these two is wrong!!!!")
receiver_email = []
text = ""
def send_text_file():
    for i in receiver_email:



        # Create a multipart message and set headers
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["Subject"] = subject
        message["To"] = i
        message["Bcc"] = i


        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        part1 = MIMEText(text, "plain")

        message.attach(part1)
        message.attach(part2)

        # Add attachment to message and convert message to string
        message.attach(part)
        text1 = message.as_string()

        # Log in to server using secure context and send email

        server.sendmail(sender_email, i, text1)

    server.quit()
def send_text():
    for i in receiver_email:






        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject
        message["To"] = i
        message["Bcc"] = i
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        text1 = message.as_string()
        server.sendmail(sender_email, i, text1)
        server.sendmail(sender_email, i, text1)
    server.quit()
def send_file():
    for i in receiver_email:


        # Create a multipart message and set headers
        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["Subject"] = subject
        message["To"] = i
        message["Bcc"] = i




        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        text1 = message.as_string()

        # Log in to server using secure context and send email

        server.sendmail(sender_email, i, text1)
    server.quit()