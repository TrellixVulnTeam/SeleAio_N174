import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
with open("G:\exmaidi\exmaidi.json") as f:
    content=json.load(f)
([*j])=content.values()
emlist=[]
for i in j:
    for k in i:
        emlist.append(k)
print(emlist)

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "ptestfome@gmail.com"
password = input("password? ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    print('ok')

    for email in emlist:
        receiver_email = email

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Bcc"] = receiver_email  # Recommended for mass emails
        # Add body to email
        message.attach(MIMEText(body, "plain"))
        filename = "document.pdf"  # In same directory as script
        text = """\hey body """
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               <a href="http://www.realbody.com">Real body</a>
               has many great bodies.
            </p>
          </body>
        </html>"""
        # Open PDF file in binary mode
        filename="G:\(abalfazl_attachment).txt"
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

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()
        Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)
        server.sendmail(sender_email, receiver_email, text )
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()