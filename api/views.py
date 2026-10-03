from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health_check(request):
    return Response({
        "status": "ok",
        "project": "medium-2-docker-rds-cicd",
        "message": "Deploy automatico con Docker + RDS funcionando"
    })