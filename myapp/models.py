from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location="media/")


class PersonInfo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    age = models.FloatField()

    def __str__(self):
        return str(self.name) + " >> " + str(self.address) + " >> " + str(self.age)


class Song(models.Model):
    title = models.CharField(max_length=250)
    singer = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class User(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(storage=fs, upload_to="users_pic/")

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    name = models.CharField(max_length=250)
    file = models.FileField(upload_to="employee_image/")

    def __str__(self):
        return str(self.name)


class Publisher(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    name = models.CharField(max_length=250)
    about = models.CharField(max_length=250)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return str(self.name)


class MyModel(models.Model):
    file_field = models.FileField()

    def __str__(self):
        return self.file_field.url


class MyModel2(models.Model):
    name = models.CharField(max_length=250)
    image = models.FileField(storage=fs, upload_to='my_photo/')


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=5, max_digits=8)

    def __str__(self):
        return str(self.name)



