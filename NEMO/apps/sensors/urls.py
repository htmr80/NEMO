from django.urls import path, re_path

from NEMO.apps.sensors import views

urlpatterns = [
	path("sensors/", views.sensors, name="sensors"),
	path("sensor_details/<int:sensor_id>/", views.sensor_details, name="sensor_details"),
	re_path(r"sensor_details/(?P<sensor_id>\d+)/(?P<tab>chart|data)/$", views.sensor_details, name="sensor_details"),
	path("sensor_chart_data/<int:sensor_id>/", views.sensor_chart_data, name="sensor_chart_data"),
	path("export_sensor_data/<int:sensor_id>/", views.export_sensor_data, name="export_sensor_data"),
	path("manage_sensor_data/", views.manage_sensor_data, name="manage_sensor_data"),
]
