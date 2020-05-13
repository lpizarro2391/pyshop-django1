from django.urls import path
from . import views


#/ products
# / productos/1/detail
# / productos/ new, todas las URL seran / products

urlpatterns = [
     path ('', views.index)

]