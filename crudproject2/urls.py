from django.contrib import admin
from django.urls import path, include
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddShowView.as_view(), name = 'addandshow'),
    path('<int:i>', views.EditView.as_view(), name='edit'),
    path('delete/<int:i>', views.DeleteView.as_view(), name = 'delete'),
]