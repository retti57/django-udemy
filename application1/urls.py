from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('<str:topic>', views.news_view),
    path('<int:num_page>', views.num_page_view)
]
