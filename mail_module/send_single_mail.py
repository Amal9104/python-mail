import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(reciptantEmail):
    senderemail = "420"
    senderpassword = "69"
    recipteremail = "evilcosmic@tuta.io"
    smtp_server_address = "smtp.gmail.com"
    smtp_server_port = 587

    subject = "Regurading Project X from User xxxxx"
    message = "Some Message that the user wants to tell"
    # Sending as MIME "Lol"
    MimeMessage = MIMEMultipart()
    MimeMessage["From"] = senderemail
    MimeMessage["To"] = recipteremail
    MimeMessage["Subject"] = subject
    MimeMessage.attach(MIMEText(message,"plain"))
    #attachmentObj = "filename" here we place the upload
    #with open(attachmentObj,'rb') as attachment:
        #part = MIMEBase("application","octet-stream")
        #part.set_payload(attachment.read())
    #encoders.encode_base64(part)
    #part.add_header("Content-Disposition",attachment,filename="")
    finalMessage = MimeMessage.as_string()
    mServer = smtplib.SMTP(host=smtp_server_address,port=smtp_server_port)
    mServer.starttls()
    mServer.login(user=senderemail,password=senderpassword)
    mServer.sendmail(senderemail,recipteremail,finalMessage)
    mServer.quit()