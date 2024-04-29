from django.urls import path
from .views import *

ulpatterns = [
    path['student/register/', RegisterView.as_view()],
    path['student/login/', LoginView.as_view()],
    path['teacher/register/', RegisterTeacherView.as_view()],
    path['teacher/login/', LoginTeacherView.as_view()],
    path['group/', CreateGroupView.as_view()],
    path['group/', EditGroupView.as_view()],
    path['group/<int:id>', EditGroupView.as_view()],
    path['homework/', HomeWork.as_view()],
    path['Hackaton/', HackatonGetView.as_view()]


]