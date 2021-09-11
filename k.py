# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
 
# # create message object instance
# msg = MIMEMultipart()
 
 
# message = "Zero To Hero"
 
# # setup the parameters of the message
# password = "09198859723"
# msg['From'] = "siyamak1981@gmail.com"
# msg['To'] = "sirat919@gmail.com"
# msg['Subject'] = "ZTH"
 
# # add in the message body
# msg.attach(MIMEText(message, 'plain'))
 
# #create server
# server = smtplib.SMTP('smtp.gmail.com: 587')
 
# server.starttls()
 
# # Login Credentials for sending the mail
# server.login(msg['From'], password)
 
 
# # send the message via the server.
# server.sendmail(msg['From'], msg['To'], msg.as_string())
 
# server.quit()

# print ("successfully sent email to {}".format(msg['To']))



# import smtplib
# sender = 'siyamak1981@gmail.com'
# receivers = ['sirat919@gmail.com']
# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test
# This is a test e-mail message.
# """
# try:
#    smtpObj = smtplib.SMTP('127.0.0.1')
#    smtpObj.sendmail(sender, receivers, message)         
#    print ("Successfully sent email")
# except BaseException:
#    print("Error: unable to send email")


# import smtplib
# sender = 'siyamak1981@gmail.com'
# receivers = ['sirat919@gmail.com']
# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test
# This is a test e-mail message.
# """
# TEXT = "Testing sending mail using gmail servers"
# username ='siyamak1981@gmail.com'
# password = '09198859723'
# server = smtplib.SMTP('smtp.gmail.com', 587)
# # server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
# server.ehlo()
# server.starttls()
# server.login(username, password)
# BODY = '\r\n'.join(['To: %s' % TO,
#         'From: %s' % username,
#         'Subject: %s' % message,
#         '', TEXT])

# server.sendmail(username, receivers, BODY)
# print ('email sent')


# import smtplib, ssl

# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "siyamak1981@gmail.com"
# receiver_email = "sirat919@gmail.com"
# password = input("Type your password and press enter:")
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)


# import smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# sender_email = "siyamak1981@gmail.com"
# receiver_email = "sirat919@gmail.com"
# password = input("Type your password and press enter:")

# message = MIMEMultipart("alternative")
# message["Subject"] = "multipart test"
# message["From"] = sender_email
# message["To"] = receiver_email

# # Create the plain-text and HTML version of your message
# text = """\
# Hi,
# How are you?
# Real Python has many great tutorials:
# www.realpython.com"""
# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#        How are you?<br>
#        <a href="http://www.realpython.com">Real Python</a> 
#        has many great tutorials.
#     </p>
#   </body>
# </html>
# """

# # Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")

# # Add HTML/plain-text parts to MIMEMultipart message
# # The email client will try to render the last part first
# message.attach(part1)
# message.attach(part2)

# # Create secure connection with server and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(
#         sender_email, receiver_email, message.as_string()
#     )


import smtplib, ssl
import part_1
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "poingshop@gmail.com"
receiver_email =part_1.exmaili
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)








