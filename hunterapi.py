import requests, sys


def getEmails(domain):
	print(domain)
	emails = []
	domain = domain
	offset = 0
	url = 'https://api.hunter.io/v2/domain-search?domain={0}&api_key=HUNTER_API&limit=100'.format(domain)
	r = requests.get('{0}&offset={1}'.format(url,offset)).json()
	try:
		while len(r['data']['emails']) > 0:
			for em in r['data']['emails']:
				emails.append(em['value'])
			offset += 100
			r = requests.get('{0}&offset={1}'.format(url,offset)).json()
		return emails
	except:
		return emails
