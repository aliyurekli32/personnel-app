from django.urls import path
from .views import DepartmentView,PersonnelListCreateView

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel",PersonnelListCreateView.as_view()),
]
