from django.urls import path

from .views import (
    mission_status,
    robot_command,
    emergency_triage,
    communication_action
)


urlpatterns = [
    path("status/", mission_status),
    path("robot-command/", robot_command),
    path("emergency-triage/", emergency_triage),
    path("communication-action/", communication_action),
]