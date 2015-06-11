from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Stocks(models.Model):
        Stk_id = models.CharField(max_length=10)
        Stk_name= models.CharField(max_length=200)

        def __unicode__(self):
            return self.Stk_name

class Holding(models.Model):
        Customer = models.ForeignKey( UserProfile)
        Stock_id = models.ForeignKey( Stocks )
        CP_date =  models.DateField('buy date', blank=True, null=True )
        SP_date =  models.DateField('sell date', blank=True, null=True)
        CP_price = models.IntegerField()
        SP_price = models.IntegerField(blank=True, null=True )
        Qty = models.IntegerField()

        def __unicode__(self):
            return self.Customer.user.username + ' ' +self.Stock_id.Stk_name 