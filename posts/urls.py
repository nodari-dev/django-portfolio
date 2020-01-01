from django.urls import path

from .views import *

urlpatterns = [
    path('work/', CasePageView.as_view(), name='work'),

]