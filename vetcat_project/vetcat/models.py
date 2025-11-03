from django.db import models

# Create your models here.


class Breed(models.Model):
    breed_name = models.CharField(max_length=100)
    coat_color = models.CharField(max_length=100)

    class Meta:
        ordering = ['breed_name']
        verbose_lst_name = 'Breed'
        verbose_lst_name_plural = 'Breeds'

    def __str__(self):
        return f"{self.breed_name} {self.coat_color}"


class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16)
    date_of_birth = models.DateField()

    class Meta:
        ordering = ['last_name']
        verbose_lst_name = 'Owner'
        verbose_lst_name_plural = 'Owners'


    def __str__(self):
        return f"{self.last_name} {self.first_name}  {self.phone_number} {self.date_of_birth}"


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=16)
    date_of_birth = models.DateField()

    breed_name = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, blank=True, related_name='cats')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True, related_name='cats')

    class Meta:
        ordering = ['name']
        verbose_lst_name = 'Cat'
        verbose_lst_name_plural = 'Cats'

    def __str__(self):
        return f"{self.name} {self.age} {self.date_of_birth} {self.breed_name} {self.owner}"

#python manage.py makemigrations
#python manage.py migrate
#python manage.py loaddata fixtures_vetcat.json
#python manage.py shell
#from school.models import Breed, Owner, Cat
#Breed.objects.all()
#Owner.objects.all()
#Cat.objects.all()





