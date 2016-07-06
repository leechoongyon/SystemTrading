import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders


#Set up crap for the attachments
# files = "/tmp/test/dbfiles"
# filenames = [os.path.join(files, f) for f in os.listdir(files)]
#print filenames


#Set up users for email
gmail_user = "rainmaker5512@gmail.com"
gmail_pwd = "1q2w3e4r5T"
recipients = ['insanelysimple0303@naver.com']

#Create Module
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = ", ".join(recipients)
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

#get all the attachments
#    for file in filenames:
#       part = MIMEBase('application', 'octet-stream')
#       part.set_payload(open(file, 'rb').read())
#       Encoders.encode_base64(part)
#       part.add_header('Content-Disposition', 'attachment; filename="%s"'
#                    % os.path.basename(file))
#       msg.attach(part)
#send it
mail(recipients,"Todays report","Test email", None)