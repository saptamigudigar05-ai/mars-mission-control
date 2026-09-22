from rest_framework.decorators import api_view
from rest_framework.response import Response

from .firebase import db


@api_view(["GET"])
def mission_status(request):
    doc = db.collection("mission").document("status").get()

    if doc.exists:
        return Response(doc.to_dict())

    return Response({
        "error": "Mission status document not found"
    })


@api_view(["POST"])
def robot_command(request):
    robot = request.data.get("robot")
    command = request.data.get("command")

    if not robot or not command:
        return Response({
            "error": "Robot and command are required"
        }, status=400)

    db.collection("robot_commands").add({
        "robot": robot,
        "command": command
    })

    return Response({
        "message": "Command sent successfully",
        "robot": robot,
        "command": command
    })


@api_view(["POST"])
def emergency_triage(request):
    patient = request.data.get("patient")
    severity = request.data.get("severity")
    issue = request.data.get("issue")

    if not patient or not severity or not issue:
        return Response({
            "error": "Patient, severity and issue are required"
        }, status=400)

    db.collection("emergency_cases").add({
        "patient": patient,
        "severity": severity,
        "issue": issue
    })

    return Response({
        "message": "Emergency case recorded",
        "patient": patient,
        "severity": severity,
        "issue": issue
    })


@api_view(["POST"])
def communication_action(request):
    action = request.data.get("action")
    channel = request.data.get("channel")

    if not action or not channel:
        return Response({
            "error": "Action and channel are required"
        }, status=400)

    db.collection("communication_actions").add({
        "action": action,
        "channel": channel
    })

    return Response({
        "message": "Communication recovery action recorded",
        "action": action,
        "channel": channel
    })