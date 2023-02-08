from django.db import models

class Event(models.Model):
    class StateChoice(models.TextChoices):
        MadhyaPradesh = 'MadhyaPradesh, MP'
        Gujarat = 'Gujarat, Guj'
        UttarPradesh = 'UttarPradesh, UP'
        Karnataka = 'Karnataka, Kar'
    
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=StateChoice.choices, default=StateChoice.MadhyaPradesh)
    zipcode = models.CharField(max_length=10)
    other = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title