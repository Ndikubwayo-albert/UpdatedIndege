from django.db import models


ACCOUNT_TYPES = (
    ('agent', 'Agent'),
    ('employer', 'Employer')
)

class CustomUser(models.Model):
    username = models.CharField(verbose_name="Username", max_length=250)
    account_type = models.CharField(verbose='Account Type'
                                    , max_length=250, choices=ACCOUNT_TYPES, default='employer')
    email = models.models.EmailField( max_length=254)
