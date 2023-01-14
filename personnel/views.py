import statistics
from django.shortcuts import render
from requests import Response
from .models import Department, Personnel
from .serializers import DepartmetSerializer,PersonnelSerializer
from rest_framework import generics,permissions
from .permissions import IsStafforReadOnly


# Create your views here.

class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmetSerializer
    queryset = Department.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsStafforReadOnly]
    
class PersonnelListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
    # permission_classes = [IsAuthenticated, IsStafforReadOnly]
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_staff:
            personnel = self.perform_create(serializer)
            data = {
                "message": f"Personal {personnel.first_name} saved successfully",
                "personnel" : serializer.data
            }
        else:
            data = {
                "message": "Yetkiniz yoktur.."
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        person = serializer.save()
        person.create_user = self.request.user
        person.save()
        return person