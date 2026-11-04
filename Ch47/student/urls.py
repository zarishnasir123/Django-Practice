from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession, name='setsession'),
    path('get/', views.getsession, name='getsession'),
    path('del/', views.delsession, name='delsession'),
    path('flush/', views.flushsession, name='flushsession'),
    path('clear/', views.sessionclear, name='sessionclear'),
    path('methodsinview/', views.sessionmethodsinview, name='sessionmethodsinview'),
    path('intemplate/', views.sessionmethodsintemplate, name='sessionmethodsintemplate'),
    path('settest/', views.settestcookie, name='settestcookie'),
    path('checktest/', views.checktestcookie, name='checktestcookie'),
    path('deltest/', views.deletetestcookie, name='deletetestcookie'),
]
