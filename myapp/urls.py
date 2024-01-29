from django.urls import path
from . import views


urlpatterns = [
    path('link1/', views.Link1View.as_view(), name='link1'),
    path('link2/', views.Link2View.as_view(), name='link2'),
]
