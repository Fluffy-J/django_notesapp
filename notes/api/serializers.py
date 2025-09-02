from rest_framework import serializers
from notes.models import Title,Body

class Title_textSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id', 'title_text', 'pub_date']


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ['id', 'body_text']