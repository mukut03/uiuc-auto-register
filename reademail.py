import imapclient
import imaplib2
import email
from imapclient import IMAPClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from email.header import decode_header
import webbrowser
import os

username = "yourusername"
password = "yourpassword"

imap_server = "outlook.office365.com"

# create an IMAP4 class with SSL
mail = imaplib2.IMAP4_SSL(imap_server)
# authenticate
mail.login(username, password)

# status, messages = imap.select("INBOX")
# messages = int(messages[0])
# print(messages)
SUBJECT_STRING = "FW: Section Enrollment Notification from Course Explorer"
#mail.select("inbox")
#status, data = mail.search(None, f'SUBJECT "{SUBJECT_STRING}"')



while True:
  # select the inbox folder and enter the "idle" state
  print('inside first while')
  mail.select("inbox")
  mail.idle()

  # wait for new emails to be received
  while True:
    print('inside second while')
    # check for new emails and exit the loop if none are found

    status, data = mail.check()
    print("1",data)
    print("2",data[0])
    found = False
    if not data[0]:
      break

    # search for emails with the specified subject
    status, data = mail.search(None, f'SUBJECT "{SUBJECT_STRING}"')
    print("3",data)
    # iterate over the matching emails and print their bodies

    for num in data[0].split():
      print('inside matching loop')
      status, data = mail.fetch(num, "(RFC822)")
      email_ = email.message_from_bytes(data[0][1])
      for payload in email_.get_payload():
        print(payload.get_payload())
      found = True
      break
    break


# exit the "idle" state and close the connection to the server
mail.idle_done()
mail.close()
mail.logout()

