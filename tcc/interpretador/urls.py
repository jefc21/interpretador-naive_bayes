from django.urls import path
from .import views


app_name='interpretador'

urlpatterns=[
	path('',views.index ,name='indeiceInterpretador')

]
