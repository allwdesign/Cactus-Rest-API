import json
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.exceptions import APIException

from core.models import Topic, Cactus


class BaseTests:
	model = None
	app_name = 'core'
	plural_name = ''

	@classmethod
	def setUpTestData(cls):
		print('='*20, cls.__name__, '='*20)

	@classmethod
	def get_test_url(cls, part):
		return ''.join([cls.app_name, ':', cls.plural_name, part])

	def setUp(self):
		"""
		We create the users, cacti and topics about cacti.
		"""
		# Create a user
		self.test_user_1 = User.objects.create_user(
			username='Bond007',
			password='mi6thisCool007',
			email='bond007@test.com'
		)

		self.test_user_2 = User.objects.create_user(
			username='Moneypenny',
			password='Miss19Money52Penny',
			email='moneypenny@test.com'
		)
		# At this point, the user, as a User object, is stored in the
		# database. We change its attributes.
		self.test_user_1.is_active = True
		self.test_user_2.is_active = True

		self.test_user_1.save()
		self.test_user_2.save()

		self.cactus_1 = Cactus.objects.create(
			owner=self.test_user_1,
			name='First Cactus',)
		self.cactus_2 = Cactus.objects.create(
			owner=self.test_user_2,
			name='Second Cactus',)

		self.cactus_1.save()
		self.cactus_2.save()

		self.topic_1 = Topic.objects.create(
			title='First Topic about Cactus',
			content='LaLalsdfetr eahef',
			cactus=self.cactus_1,
			owner=self.test_user_1)
		self.topic_2 = Topic.objects.create(
			title='Second Topic about Cactus',
			content='Srlkg2qjt[35] eahef',
			cactus=self.cactus_2,
			owner=self.test_user_2)

		self.topic_1.save()
		self.topic_2.save()

		self.token_1 = Token.objects.get(user=self.test_user_1)
		self.token_2 = Token.objects.get(user=self.test_user_2)

		# Include 'Authorization:' header on all requests.
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_1.key)

	def test_get_all_objects(self):
		"""
		Ensure we can get all topic objects.
		"""
		url = reverse(self.get_test_url('-list'))
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_one_object(self, pk):
		"""
		Ensure we can get a sigle topic object.
		"""
		url = reverse(self.get_test_url('-detail'), kwargs={'pk':pk})
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_one_object(self, token_key, data):
		"""
		Ensure we can create a sigle object.
		"""
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token_key)
		url = reverse(self.get_test_url('-list'))
		response = self.client.post(
			url,
			data=data,
			content_type='application/json',
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_update_one_object(self, token_key, data):
		"""
		Ensure we can get a sigle object.
		"""
		# Include 'Authorization:' header on all requests.
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + token_key)

		url = reverse(
			self.get_test_url('-detail'),
			kwargs={'pk': json.loads(data)['id']})
		response = self.client.put(
			url,
			data=data,
			content_type='application/json',
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_one_object(self, pk):
		"""
		Ensure we can delete a sigle object.
		"""
		objects_count_before_del = self.model.objects.count()

		url = reverse(self.get_test_url('-detail'), kwargs={'pk':pk})
		response = self.client.delete(url)

		objects_count_after_del = self.model.objects.count()
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(
			objects_count_before_del - 1,
			objects_count_after_del,
			'Should have delete a single object from the database.',
		)

	def test_ivalid_owner_cannot_update_object(self, inv_owner, data):
		ivalid_owner = inv_owner

		url = reverse(self.get_test_url('-detail'), kwargs={'pk': json.loads(data)['id']})
		response = self.client.put(
			url,
			data=data,
			content_type='application/json',
		)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TopicsTests(BaseTests, APITestCase):
	model = Topic
	plural_name = 'topics'

	def test_get_all_objects(self):
		return super().test_get_all_objects()

	def test_get_one_object(self):
		return super().test_get_one_object(self.topic_1.pk)

	def test_create_one_object(self):
		data = json.dumps({
			'title':'Fourth Topic about Cactus',
			'content':'Foursdfetr eahef',
			'cactus_id': self.cactus_2.pk,
		})
		return super().test_create_one_object(self.token_2.key, data)

	def test_update_one_object(self):
		data = json.dumps({
			'id': self.topic_1.pk,
			'title':'Updated Topic about Cactus',
			'content':'Updated LaLalsdfetr eahef',
			'cactus_id': self.cactus_1.pk,
		})

		return super().test_update_one_object(self.token_1.key, data)

	def test_delete_one_object(self):
		return super().test_delete_one_object(self.topic_1.pk)

	def test_ivalid_owner_cannot_update_object(self):
		ivalid_owner = self.test_user_1

		data = json.dumps({
			'id': self.topic_2.pk,
			'title':'Updated Topic about Cactus',
			'content':'Updated LaLalsdfetr eahef',
			'cactus_id': self.cactus_2.pk,
			'owner_id':ivalid_owner.pk,
		})

		super().test_ivalid_owner_cannot_update_object(ivalid_owner, data)


class CactusTests(BaseTests, APITestCase):
	model = Cactus
	plural_name = 'cacti'

	def test_get_all_objects(self):
		return super().test_get_all_objects()

	def test_get_one_object(self):
		return super().test_get_one_object(self.cactus_1.pk)

	def test_create_one_object(self):
		data = json.dumps({'name': 'New shiny cactus',})
		return super().test_create_one_object(self.token_2.key, data)

	def test_update_one_object(self):
		data = json.dumps({
			'id': self.cactus_2.pk,
			'name': 'Updated Cactus',
		})

		return super().test_update_one_object(self.token_2.key, data)

	def test_delete_one_object(self):
		return super().test_delete_one_object(self.cactus_1.pk)

	def test_ivalid_owner_cannot_update_object(self):
		ivalid_owner = self.test_user_1

		data = json.dumps({
			'id': self.cactus_2.pk,
			'name': 'Updated Cactus',
			'owner_id':ivalid_owner.pk,
		})

		super().test_ivalid_owner_cannot_update_object(ivalid_owner, data)
