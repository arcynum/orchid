from django.test import TestCase
import datetime
import re
from .views import _generate_activation_hash

# Create your tests here.
class GenerateActivationHashTests(TestCase):
	def test_id_is_negative(self):
		id = -1
		email = 'sample@email.com'
		now = datetime.datetime.now()
		hash = _generate_activation_hash(id, email, now)
		self.assertEqual(len(hash), 128)
		self.assertNotEqual(re.match(r"^[a-f0-9]{128}$", hash), None)

	def test_email_exists(self):
		id = 1
		email = ''
		now = datetime.datetime.now()
		hash = _generate_activation_hash(id, email, now)
		self.assertEqual(len(hash), 128)
		self.assertNotEqual(re.match(r"^[a-f0-9]{128}$", hash), None)