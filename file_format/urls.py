from django.urls import path
from file_format.views import FormatDirectoryAPI

urlpatterns = [
    path('<folder>/', FormatDirectoryAPI.as_view()),
]
