import imaplib, pprint

imap_host = 'imap.gmail.com'
imap_user = '<EMAIL>'
imap_pass = '<EMAIL-PASSWORD>'

# Connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## Login to server
imap.login(imap_user, imap_pass)

imap.select('Inbox')

# Lists all folder
pprint.pprint(imap.list())
pprint.pprint(imap.capability())

tmp, data = imap.search(None, 'ALL')

for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1])
	break

imap.close()