import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from htmlTemplate import returnHtml,returnHtmlMessage
# from htmlApp import returnHtml

def sendMail(receiverEmail ,name,sub=' ',mess=' ',name2=' '):
    sender_email = "incontrol.sys.service@gmail.com"
    # sender_email = "sagieka1@gmail.com"
    receiver_email = receiverEmail
    # receiver_email = "sagieka@gmail.com"
    password = "Aa123456!"
    # password = "Aa5561212"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Message from incontrolSite"
    message["From"] = sender_email
    message["To"] = receiver_email
    test1='ddsssd'
    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    if sub == ' ':
        html=returnHtml(name)
    else:
        html=returnHtmlMessage(name,sub,mess,receiverEmail,name2)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return 0