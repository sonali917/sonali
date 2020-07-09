from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

