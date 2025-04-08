from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='user1@example.com', name='User One'),
            User(id=ObjectId(), email='user2@example.com', name='User Two'),
            User(id=ObjectId(), email='user3@example.com', name='User Three'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(id=ObjectId(), name='Team Alpha')
        team1.save()
        team1.members.set(users[:2])

        team2 = Team(id=ObjectId(), name='Team Beta')
        team2.save()
        team2.members.set(users[2:])

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], activity_type='Running', duration=60, date='2025-04-01'),
            Activity(id=ObjectId(), user=users[1], activity_type='Cycling', duration=45, date='2025-04-02'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=team1, points=100),
            Leaderboard(id=ObjectId(), team=team2, points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Morning Run', description='A quick morning run', duration=30),
            Workout(id=ObjectId(), name='Evening Yoga', description='Relaxing yoga session', duration=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))