from django.db import models


class Breed(models.Model):
    EAR_TYPE_CHOICES = [('—', 'Unknown'), ('Erect', 'Erect'), ('Lop', 'Lop')
    ]
    YES_NO_CHOICES = (('—', 'Unknown'), ('Yes', 'Yes'), ('No', 'No'))

    breed_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.CharField(max_length=300)
    sizes = models.CharField(max_length=100)
    fur_type = models.CharField(max_length=20)
    ear_type = models.CharField(
        max_length=7,
        choices=EAR_TYPE_CHOICES,
        default='Unknown',
    )
    colors = models.CharField(max_length=100)
    ARBA_recognised = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    BRC_recognised = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    origins = models.CharField(max_length=100)

    def __str__(self):
        return f"Id: {self.breed_id} {self.name}"
