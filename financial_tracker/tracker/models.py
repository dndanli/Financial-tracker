from django.db import models
from django.contrib.auth.models import User


class FinancialTracker(models.Model):
    """The Financial Tracker"""
    tracker_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="financialtracker",null=True)
    tracker_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tracker_name

class TrackerItem(models.Model):
    """A representation of each item in the tracker"""
    # the tracker
    tracker = models.ForeignKey(FinancialTracker, on_delete=models.CASCADE)

    # payment title
    pay_title = models.CharField(max_length=25)

    pay_amt = models.DecimalField(max_digits=6, decimal_places=2)

    # type of payment made
    pay_type = models.CharField(max_length=25)

    # brief description of a payment
    pay_description = models.CharField(max_length=100)


    def __str__(self):
        return (f"title: {self.pay_title} | amount: {self.pay_amt} | "
                f"type: {self.pay_type} | description: {self.pay_description}")
