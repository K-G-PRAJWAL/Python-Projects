# SMTP protocol

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
print(conn.ehlo())
conn.starttls()
print(conn.login('sender@mail.com', 'senderPassword'))
conn.sendmail('sender@mail.com', 'receiver@mail.com',
              'Subject: Learning Python Automation\n\nDear Prajwal, \n\nLove yourself, Stay Strong and Keep Going! Your doing great!\n\n-Praju')
conn.quit()

# In gmail enable 'allow from unknown sources' option while performing this program
