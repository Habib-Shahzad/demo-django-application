from django.db import models


class Model1(models.Model):
    f1 = models.IntegerField()
    f2 = models.CharField(max_length=100)
    f3 = models.FloatField()
    f4 = models.FloatField()


class Model2(models.Model):
    f1 = models.IntegerField()
    f2 = models.CharField(max_length=100)
    f3 = models.FloatField()
    f4 = models.FloatField()


class CC1:
    def __init__(self, model1: Model1, model2: Model2):
        self.model1 = model1
        self.model2 = model2

    def get_link1_data(self):
        return {
            'f1': self.model1.f1,
            'f2': self.model1.f2,
            'f3': self.model2.f1,
            'f4': self.model2.f2,
        }

    def get_link2_data(self):
        return {
            'f1': self.model1.f3,
            'f2': self.model1.f4,
            'f3': self.model2.f3,
            'f4': self.model2.f4,
        }
