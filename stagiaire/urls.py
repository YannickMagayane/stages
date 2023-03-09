from django.urls import path
from .views import clear_students,user_login,FiliaireCreateView,user_logout,ProgramView,ProgramListView,FiliaireListView,StudentListViews,user_register,StudentListView, StudentCreateView,generate_card

urlpatterns = [

    path('add_filiaire/',FiliaireCreateView.as_view(),name='filiaire'),
    path('logout/',user_logout,name='logout'),
    path('add_program/',ProgramView.as_view(),name='programme'),
    path('', FiliaireListView.as_view(), name='filiaire_list'),
    path('program/<int:option_id>/', ProgramListView.as_view(), name='program_list'),
    path('student/add/', user_register, name='student_add'),
    path('student/', StudentListView.as_view(), name='student_list'),
    path('student_list/', StudentListViews.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('generate_card/<int:pk>/', generate_card, name='generate_card'),
    path('login/',user_login,name='login'),
    path('clear-students/', clear_students, name='clear_students'),


]