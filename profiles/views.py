from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WinePal
from .serializers import WinepalSerializer


class ListWinePals(APIView):
    # List users(winepals)
    def get(self, request):
        profile = WinePal.objects.all()
