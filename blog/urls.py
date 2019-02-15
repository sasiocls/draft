from django.urls import path
from .views import *

urlpatterns = [
    names = ['tash', 'umar']
    path('', posts_list, context ={'names':name}),

]