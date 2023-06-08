from . import views
from django.urls import path

urlpatterns = [
    path('',views.add_data, name='add_data'),
    path('delete/<int:data_id>/',views.delete_data,name='delete_data'),
    path('update/<int:data_id>/',views.update_data,name='update_data'),
]