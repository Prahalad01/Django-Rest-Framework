from django.shortcuts import render
from .serializers import LeaveRequestSerializers
from .models import LeaveRequest
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny
from django.db.models import Q


class LeaveRequestView(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'start_date': ['in', 'exact', 'gte', 'lte'],
        'end_date': ['in', 'exact', 'gte', 'lte'],
        }

    def get_queryset(self):
        if self.request.GET.get('date',None):
            date = self.request.GET.get('date')
            # import pdb;pdb.set_trace()
            self.queryset = self.queryset.filter(start_date__lte=date) | self.queryset.filter(end_date__lte=date)
        return self.queryset


