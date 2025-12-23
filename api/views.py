from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from index.models import Quotes
from .serializers import QuotesSerializer

class QuotesListAPIView(APIView):
    """
    回傳所有 Quotes（可之後加篩選 is_featured=True）
    """
    def get(self, request):
        quotes = Quotes.objects.all()  # 或 .filter(is_featured=True)
        serializer = QuotesSerializer(quotes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)