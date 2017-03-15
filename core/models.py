from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(
            default=timezone.now)

    def created_team(self):
        pass

    def create_tournament(self):
        pass

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Tournament(models.Model):
    name = models.CharField(max_length=255)

class Match(models.Model):
    pass
