from string import ascii_uppercase, digits
from random import choice

import requests

DOMAINS = [
	'getnada.com', 
	'amail.club', 
	'banit.club',
	'cars2.club',
	'cmail.club',
	'banit.me',
	'duck2.club',
	'nada.email',
	'nada.ltd',
	'wmail.club'
]

GET_INBOX = 'https://getnada.com/api/v1/inboxes/{}'
GET_MESSAGE = 'https://getnada.com/api/v1/messages/{}'

class Nada(object):
	def __init__(self, name=None, domain=None):
		self.name = (name or Nada.id_generator()).lower()
		self.domain = domain or choice(DOMAINS)

	def __str__(self):
		return '{}@{}'.format(self.name, self.domain)

	def get_inbox(self):
		data = None
		try:
			r = requests.get(GET_INBOX.format(self))
			data = r.json()['msgs']
		except:
			pass
		return data

	def get_message(self, uid):
		data = None
		try:
			r = requests.get(GET_MESSAGE.format(uid))
			data = r.json()
		except:
			pass
		return data #[ru, d, f, text, fe, html, s, r, at, rf, ib, uid]

	@staticmethod
	def id_generator(size=6, chars=ascii_uppercase + digits):
		return ''.join( choice(chars) for _ in range(size) )

if __name__ == "__main__":
	n = Nada()
	messages = n.get_inbox()
	message = n.get_message(messages[0]['uid'])