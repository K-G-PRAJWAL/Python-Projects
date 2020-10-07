import re
import pyperclip

# Create regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?    # area code(optional)
(\s|-)    # first separator
\d\d\d    # first 3 digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s|x)  # extension (optional)
 (\d{2,5})))?
)  # extension number part (optional)  
''', re.VERBOSE)

# Create regex for email addresses
emailRegex = re.compile(r'''
# something@something.com

[a-zA-Z0-9_.+]+    # name
@    # @
[a-zA-Z0-9_.+]+    # domain name
''', re.VERBOSE)

# Get the text from the clipboard
text = pyperclip.paste()

# Extract the email & phone number from the clipboard
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted phone numbers & email to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)
