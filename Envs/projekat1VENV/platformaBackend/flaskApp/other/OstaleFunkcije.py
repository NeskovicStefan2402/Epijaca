from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from flaskApp.models.Proizvod import ProizvodModel
import ssl,smtplib
from docx import Document
from docx.shared import Inches
from datetime import datetime,date

class OstaleFunkcije:
    @classmethod
    def posaljiEmail1(cls,data):
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = "steficefi97@gmail.com"
        password = 'Stefan__1998'
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            msg = EmailMessage()
            msg.set_content(data['poruka'])
            msg['subject'] = data['subject']
            msg['From'] = sender_email
            msg['To'] = data['to']
            server.send_message(msg)
        except Exception as e:
            print(e)
        finally:
            server.quit()

    @classmethod
    def posaljiEmail(cls,data):
        email_user = 'steficefi97@gmail.com'
        email_password = 'Stefan__1998'
        email_send = data['to']
        subject = data['subject']
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        body = data['poruka']
        msg.attach(MIMEText(body,'plain'))
        filename=data['file']
        attachment  = open(filename,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= Prijemnica.docx")
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        server.quit()

