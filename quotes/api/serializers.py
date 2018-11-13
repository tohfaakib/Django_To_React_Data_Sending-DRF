from rest_framework import serializers

from quotes.models import Quote, QuoteCategory

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        # ('__all__') for all fields
        # ['']
        fields = ['quote', 'author']



class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory
        fields = ('__all__')
