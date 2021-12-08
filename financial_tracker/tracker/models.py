from django.db import models


class FinancialTracker(models.Model):
    """The Financial Tracker"""
    tracker_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tracker_name

class TrackerItem(models.Model):
    """A representation of each item in the tracker"""
    # the tracker
    tracker = models.ForeignKey(FinancialTracker, on_delete= models.CASCADE)

    # payment title
    pay_title = models.CharField(max_length=25)

    # store numbers up to a billion
    pay_amt = models.DecimalField(max_digits=19, decimal_places=10)

    # type of payment made
    pay_type = models.CharField(max_length=25)

    # brief description of a payment
    pay_description = models.CharField(max_length=100)