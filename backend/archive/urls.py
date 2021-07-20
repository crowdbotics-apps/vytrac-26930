from django.urls import path, re_path

from archive.views import archive

urlpatterns = [
    path('', archive.Views.as_view(), name='archive'),
    path('<slug:app_label>/<slug:model>/<int:pk>/', archive.View.as_view(), name='archive_acttions'),
]
