from django.urls import path, re_path

from . import views

urlpatterns = [
    path("devices", views.device_list, name="device_list"),
    re_path('devices', views.device_list,name="device"),
    re_path("interfaces", views.device_interfaces_list, name="device_interface_list"),
    re_path("port_chnls", views.device_port_chnl_list, name="device_port_chnl_list"),
    re_path("mclags", views.device_mclag_list, name="device_mclag_list"),
]