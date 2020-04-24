import email, smtplib, ssl
import getpass
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == "__main__":
    sender_email = str(input("Enter your Email Id :"))
    sender_password = getpass.getpass("Enter yor Password (Your password will be hidden for security purpose ) :")
    reciver_email = str(input("Enter to Whom do you want to send Email :"))
    domain = sender_email[sender_email.index("@")+1:sender_email.index(".")]
    smtp_address = str(input("Enter the SMTP Address for "+str(domain)+" :"))
    smtp_port = int(input("Enter the SMTP Port Number for "+str(domain)+" :"))
    subject_mail = str(input("Enter the Subject :"))
    body_mail = str(input("Enter the Message :"))
    sendBulkMail(sender_mail_id=sender_email,sender_password=sender_password,smtp_address=smtp_address,smtp_port=smtp_port,subject=subject_mail,message=body_mail)

def sendBulkMail(sender_mail_id,sender_password,smtp_address,smtp_port,subject,message):
    csvfile = str(input("name of CSV File containing EmailIds of reciver"))