from django.urls import path

from api.views import main, info, places

urlpatterns = [
    path('', main),  # http://127.0.0.1:8000/api
    path('info', info),  # http://127.0.0.1:8000/api/p1
    path('places', places)  # http://127.0.0.1:8000/api/p2
]