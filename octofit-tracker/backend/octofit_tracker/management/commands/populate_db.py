from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30),
            Activity(user='Captain America', activity_type='Cycling', duration=45),
            Activity(user='Wonder Woman', activity_type='Swimming', duration=60),
            Activity(user='Batman', activity_type='Yoga', duration=40),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        leaderboard = [
            Leaderboard(user='Iron Man', score=100),
            Leaderboard(user='Captain America', score=90),
            Leaderboard(user='Wonder Woman', score=110),
            Leaderboard(user='Batman', score=95),
        ]
        for entry in leaderboard:
            entry.save()

        # Workouts
        workouts = [
            Workout(name='Pushups', description='Do 3 sets of 15 pushups', difficulty='Easy'),
            Workout(name='HIIT', description='20 min high intensity interval training', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
