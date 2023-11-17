from django.urls import path

from . import views

app_name = "index"

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="index"),
    path("<int:pk>/", view=views.DetailView.as_view(), name="detail")
]