from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')

    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', activity_type='Running', duration=10)
        self.assertEqual(activity.activity_type, 'Running')

    def test_leaderboard_creation(self):
        entry = Leaderboard.objects.create(user='Test User', score=50)
        self.assertEqual(entry.score, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
