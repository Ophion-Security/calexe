import requests, sys
from hunterapi import getEmails

if len(sys.argv) != 3:
	print("Missing parameter. Provide both input and output like: python3 cal.py domain output.txt")
	sys.exit()

input_user = sys.argv[1]


def goThroughEmails(input_user):
	found_emails = open(sys.argv[2], 'a+')
	emails = getEmails(input_user)
	if len(emails) > 0:
		for em in emails:
			url = 'https://calendar.google.com/calendar/htmlembed?src={0}&ctz=American/Los_Angeles'.format(em)
			checkEmail = requests.head(url)
			if checkEmail.status_code == 200:
				found_emails.write(url) # write the url to the file, we will take picture of this url
				found_emails.write('\n')
		found_emails.close()

def goThroughTxt(input_user):
	file = open(input_user, 'r')
	found_emails = open(sys.argv[2], 'a+')
	for line in file:
		url = 'https://calendar.google.com/calendar/htmlembed?src={0}&ctz=American/Los_Angeles'.format(line.strip())
		checkEmailTxt = requests.head(url)
		if checkEmailTxt.status_code == 200:
			found_emails.write(url)
			found_emails.write('\n')
	found_emails.close()

if input_user.split('.')[1] == "txt":
	goThroughTxt(input_user)
else:
	goThroughEmails(input_user)
