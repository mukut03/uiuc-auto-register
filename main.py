import reademail
import register

while True:
  for i in reademail.listen():
    register.sign_up(i)

