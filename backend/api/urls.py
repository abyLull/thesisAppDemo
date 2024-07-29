from django.contrib import admin
from django.urls import path
from . import views
urlpatterns= [
    path('', views.Home, name = 'home'),
    path('home',views.Home,name = 'home'),
    path('sign-up',views.sign_up,name = 'sign_up'),
    path('logout_user',views.logout_view, name = 'logout_user'),
    path('students-xlsx',views.UploadStudentDataViewXLSX, name = 'students_xlsx' ),
    path('destinations-xlsx',views.UploadDestinationDataViewXLSX, name = 'destinations_xlsx' ),
    path('edit_student/', views.edit_student, name='edit_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('edit_destination/', views.edit_destination, name='edit_destination'),
    path('delete_destination/', views.delete_destination, name='delete_destination'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('destination/<int:id>/', views.view_destination, name='view_destination'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-destination/', views.add_destination, name='add_destination'),
    path('sorted', views.SortedListView, name = 'sorted_list'),
    path('approved', views.ApprovedListView, name = 'approved_list'),
    path('approved/download/xlsx/', views.download_approved_xlsx, name='download_approved_xlsx'),
]