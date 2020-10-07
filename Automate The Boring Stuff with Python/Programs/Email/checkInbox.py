# IMAP protocol

import pyzmail
import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('name@mail.com', 'password')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-AUG-2020'])
print(UIDs)
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')
message.text_part
message.html_part == None
message.text_part.get_payload().decode('UTF-8')
conn.list_folders()
