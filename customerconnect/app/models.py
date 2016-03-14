from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.note)
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200,null=True)
    address2 = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    postal_code = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name