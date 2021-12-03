from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Contract(models.Model):
    
    
    insurer = models.CharField(max_length=255)
    number = models.CharField(verbose_name=_("Number"), max_length=255, null=True, blank=True)
    end_date = models.DateField(
        verbose_name=_("End Date"),
        blank=True,
        null=True,
        help_text=_("If provided, will apply to all policies in the contract."),
    )
    cancellation_date = models.DateField(
        verbose_name=_("Cancellation Date"),
        blank=True,
        null=True,
    )
    publish_date = models.DateField(
        verbose_name=_("Publish Date"),
        blank=True,
        null=True,
    )
    effective_date = models.DateField(
        verbose_name=_("Effective Date"),
        blank=True,
        null=True,
    )
    payment_date = models.DateField(
        verbose_name=_("Payment Date"),
        blank=True,
        null=True,
    )
    
    def __str__(self) -> str:
        return 'Contract'
