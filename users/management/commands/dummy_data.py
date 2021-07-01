from django.contrib.auth.models import Group
import factory
from factory.django import DjangoModelFactory

# from polls.models import Question as Poll
from Functions.Permissions import perm
from calendars.models import Event, DateType
from patients.models.models import Patient
from users.models import User

import random

from django.db import transaction
from django.core.management.base import BaseCommand


NUM_CLUBS = 10
NUM_THREADS = 12
COMMENTS_PER_THREAD = 25
USERS_PER_CLUB = 8

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = factory.Faker("password")



class DateTypeFacotry(DjangoModelFactory):
    class Meta:
        model = DateType

    name = factory.Faker("name")
    description = factory.Faker("sentence")



class EventFacotry(DjangoModelFactory):
    class Meta:
        model = Event

    title = factory.Faker("sentence")
    description = factory.Faker("sentence")
    date_type = factory.SubFactory(DateTypeFacotry)
    created_by = factory.SubFactory(UserFactory)



def makeSuper(admin):
    admin.is_active = True
    admin.is_admin = True
    admin.is_admin = True
    admin.is_email_verified = True
    admin.is_role_verified = True
    admin.save()


class Command(BaseCommand):
    help = 'create dummy data'

    @transaction.atomic
    def handle(self, *args, **options):




        self.stdout.write("Deleting old data...")
        models = [User,Event,DateType, Group]

        for m in models:
            m.objects.all().delete()

        # Create groups
        groups = []
        Patients = Group.objects.create(name='Patients')

        groups.append(Patients)
        Doctors = Group.objects.create(name='Doctors')
        Doctors.permissions.add(perm('Can view user', User))
        Doctors.permissions.add(perm('Can view patient', Patient))
        Doctors.permissions.add(perm('Can change patient', Patient))
        Doctors.save()

        groups.append(Doctors)
        providers = Group.objects.create(name='providers')
        Patients.permissions.add(perm('Can view user', User))
        Patients.permissions.add(perm('Can change user', User))
        Patients.permissions.add(perm('Can view patient', Patient))
        Patients.permissions.add(perm('Can change patient', Patient))
        Patients.save()
        groups.append(providers)

        admin = User.objects.create_superuser(email='ali@g.com', username='ali', password='password')
        makeSuper(admin)

        self.stdout.write("Creating new data...")
        # Create all the users
        people = []
        for _ in range(25):
            person = UserFactory()
            person.groups.add(random.choice(groups))
            person.is_email_verified = True
            person.is_role_verified = True
            person.is_staff = random.choice([True,False])
            person.save()
            people.append(person)

        for _ in range(25):
            UserFactory()

        # Add some users to clubs
        for _ in range(NUM_CLUBS):
            club = DateTypeFacotry()

            # Create all the threads
        for _ in range(NUM_THREADS):
            creator = random.choice(people)
            thread = EventFacotry(created_by=creator)








