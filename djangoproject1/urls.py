from django.urls import path, include
from .views import main, bio, facts

urlpatterns = [
    path('', main, name='main'),
    path('bio/', bio),
    path('facts/', facts),

    path('api/', include('api.urls')), # !!! api - назва іншого додатку, з якого підтягнуться пыдрозділи
]