from rest_framework import generics

from quotes.models import Quote, QuoteCategory

from .serializers import QuoteSerializer, QuoteCategorySerializer


class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer