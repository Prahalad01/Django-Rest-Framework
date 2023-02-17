from django.db import models
from account.models import User
# Create your models here.

class LeaveRequest(models.Model):

    Privilege_Leave=1
    Casual_Leave=2
    Sick_Leave=3


    ROLE_CHOICES = (
        (Privilege_Leave, 'Privilege_Leave'),
        (Casual_Leave, 'Casual_Leave'),
        (Sick_Leave, 'Sick_Leave')
    )

    PENDING=0
    APPROVED=1
    REJECT=2

    STATUS_CHOICES=(
        (PENDING,'Pending'),
        (APPROVED,'Approved'),
        (REJECT,'Reject'),
    )

    # STATUS_CHOICES_PENDING=((PENDING,'Pending'),)



    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    leave_type=models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    reason=models.TextField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    leave_days=models.IntegerField()
    leave_status=models.PositiveSmallIntegerField(choices=STATUS_CHOICES,default='Pending') 


   