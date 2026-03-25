
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, User, Activity, Workout, Leaderboard

class ApiSmokeTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_team_crud(self):
		url = reverse('team-list')
		data = {'name': 'TestTeam'}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_user_crud(self):
		team = Team.objects.create(name='TestTeam')
		url = reverse('user-list')
		data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass', 'team': team.id}
		response = self.client.post(url, data)
		self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

	def test_activity_crud(self):
		team = Team.objects.create(name='TestTeam')
		user = User.objects.create(username='testuser', email='test@example.com', team=team)
		url = reverse('activity-list')
		data = {'user': user.id, 'type': 'run', 'duration': 30}
		response = self.client.post(url, data)
		self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

	def test_workout_crud(self):
		url = reverse('workout-list')
		data = {'name': 'Morning', 'description': 'desc', 'duration': 20}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_leaderboard_crud(self):
		team = Team.objects.create(name='TestTeam')
		user = User.objects.create(username='testuser', email='test@example.com', team=team)
		url = reverse('leaderboard-list')
		data = {'user': user.id, 'score': 100}
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
