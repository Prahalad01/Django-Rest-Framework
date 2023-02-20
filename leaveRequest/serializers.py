from rest_flex_fields import FlexFieldsModelViewSet, FlexFieldsModelSerializer

from .models import LeaveRequest
from account.serializers import UserSerializers

class LeaveRequestSerializers(FlexFieldsModelSerializer):
    class Meta:
        model=LeaveRequest
        fields="__all__"
    
        expandable_fields = {
        'user': (UserSerializers, {'source': 'user_id'})
    }
