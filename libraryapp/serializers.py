from rest_framework import serializers
from libraryapp.models import Books


class BookSerializers(serializers.ModelSerializer):
    Title=serializers.CharField()
    Author=serializers.CharField()
    Category=serializers.CharField()
    Price=serializers.DecimalField(max_digits=10,decimal_places=10)
    Publishes_year=serializers.IntegerField()
    Available=serializers.BooleanField()

