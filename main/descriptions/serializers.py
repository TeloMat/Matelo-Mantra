from rest_framework import serializers

from main.descriptions.models import Description


class DescriptionSerializer(serializers.ModelSerializer):
    traveler = serializers.ImageField()
    picture = serializers.ImageField()
    musician = serializers.ImageField()
    writer = serializers.ImageField()

    class Meta:
        model = Description
        fields = ('text', 'quote', 'quote', 'picture', 'traveler', 'musician', 'writer')
