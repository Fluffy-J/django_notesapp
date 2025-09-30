from rest_framework import serializers
from notes.models import Title,Body,Category

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class Title_textSerializer(serializers.ModelSerializer):
    Category = serializers.SlugRelatedField(slug_field='name',
    queryset=Category.objects.all()
    )


    class Meta:
        model = Title
        fields = ['id', 'title_text', 'pub_date', 'Category']


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ['id', 'body_text']