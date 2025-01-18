from .views import DocumentView
from django.urls import path

urlpatterns = [
    path("documents/", DocumentView.as_view(), name="document"),
]
