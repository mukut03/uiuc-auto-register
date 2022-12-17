import imaplib2
import email
from email.policy import default as default_policy
import html

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from email.header import decode_header


username = "youremail"
password = "yourpassword"

imap_server = "outlook.office365.com"

# create an IMAP4 class with SSL
mail = imaplib2.IMAP4_SSL(imap_server)
# authenticate
mail.login(username, password)


SUBJECT_STRING = "FW: Section Enrollment Status Update from Course Explorer"

mail.select("inbox")

status, data = mail.search(None, 'ALL')
current_emails = len(data[0].split())

def get_crn(body_):
  # print(type(body_))
  crn_index = body_.find("CRN")
  # print(crn_index)
  crn = body_[crn_index+5: crn_index+10]
  print(crn)




while True:

  status_, data_ = mail.search(None, 'ALL')
  temp = len(data[0].split())

  if status_ != "OK":
    print("server error")
    break
  temp = len(data_[0].split())



  if(temp>current_emails):

  # if(mail.recent()!=None):
    result, d_ = mail.uid('search', None, "ALL")
    if(result=="OK"):
      latest_email_uid = d_[0].split()[-1]
      result, d_ = mail.uid('fetch', latest_email_uid, '(RFC822)')
      if(result=='OK'):
        raw_email = d_[0][1]
        # print(raw_email)
        #print(type(raw_email))
        msg = email.message_from_bytes(raw_email, policy = default_policy)
        #print(msg.keys())
        # body = msg.get_body()
        # print(html.unescape(body))

        email_from = str(email.header.make_header(email.header.decode_header(msg['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(msg['To'])))
        subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))

        print("from: ", email_from, "to: ", email_to, "subject: ", subject )


        if(subject == SUBJECT_STRING):
          for part in msg.walk():
            if part.get_content_type() == "text/plain":
              body = part.get_payload(decode=True)
              body_ = body.decode('utf-8')
              get_crn(body_)
    current_emails = temp
    break #for now




  # if status_ != "OK":
  #   print("server erorr")
  #   break
  # temp = len(data_[0].split())
  #
  #
  #
  # if(temp>current_emails):
  #   current_emails = temp
  #   print("new email received")
  #   print(mail.message(rec_.split()[-1]))


  # wait for new emails to be received
  # while True:
  #   print('inside second while')
  #   # check for new emails and exit the loop if none are found
  #
  #   status, data = mail.check()
  #   print("1",data)
  #   print("2",data[0])
  #   found = False
  #   if not data[0]:
  #     break
  #
  #   # search for emails with the specified subject
  #   status, data = mail.search(None, f'SUBJECT "{SUBJECT_STRING}"')
  #   print("3",data)
  #   # iterate over the matching emails and print their bodies
  #
  #   for num in data[0].split():
  #     print('inside matching loop')
  #     status, data = mail.fetch(num, "(RFC822)")
  #     email_ = email.message_from_bytes(data[0][1])
  #     for payload in email_.get_payload():
  #       print(payload.get_payload())
  #     found = True
  #     break
  #   break




# close the connection to the server

mail.close()
mail.logout()

