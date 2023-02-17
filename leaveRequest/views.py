from django.shortcuts import render
from .serializers import LeaveRequestSerializers
from .models import LeaveRequest
# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny

class LeaveRequestView(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializers



