from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns=[
    # path('admin/',admin.site.urls),
    # path('',include('base.urls')),
    # path('api/',include('base.api.urls'))

    path('',views.getRoutes),
    path('rooms/',views.getRooms),
    path('rooms/<str:pk>/',views.getRoom),

]