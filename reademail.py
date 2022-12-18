import imaplib2
import email
from email.policy import default as default_policy
import html

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from email.header import decode_header



SUBJECT_STRING = "FW: Section Enrollment Status Update from Course Explorer"
username = "mukutm@outlook.com"
password = "nlp@2025"
imap_server = "outlook.office365.com"


def get_crn(body_):
  crn_index = body_.find("CRN")
  crn = body_[crn_index+5: crn_index+10]
  return crn

def listen():
  mail = imaplib2.IMAP4_SSL(imap_server)
  mail.login(username, password)

  mail.select("inbox")

  status, data = mail.search(None, 'ALL')
  current_emails = len(data[0].split())
  while True:
    status_, data_ = mail.search(None, 'ALL')

    if status_ != "OK":
      print("server error")
      break

    temp = len(data_[0].split())

    if(temp>current_emails):
      result, d_ = mail.uid('search', None, "ALL")
      if(result=="OK"):
        latest_email_uid = d_[0].split()[-1]
        result, d_ = mail.uid('fetch', latest_email_uid, '(RFC822)')
        if(result=='OK'):
          raw_email = d_[0][1]
          msg = email.message_from_bytes(raw_email, policy = default_policy)
          email_from = str(email.header.make_header(email.header.decode_header(msg['From'])))
          email_to = str(email.header.make_header(email.header.decode_header(msg['To'])))
          subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))
          print("from: ", email_from, "to: ", email_to, "subject: ", subject )

          if(subject == SUBJECT_STRING):
            for part in msg.walk():
              if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                body_ = body.decode('utf-8')
                crn = get_crn(body_)
                yield crn

    current_emails = temp
  mail.close()
  mail.logout()


