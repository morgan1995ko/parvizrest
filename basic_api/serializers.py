from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

python manage.py shell
from basic_api import Article
from basic_api.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
a = Article(title = 'firsr_title', author = 'parwiz', email = 'par@email.com')
a.save()
a = Article(title = 'new_title', author = 'john', email = 'john@email.com')
a.save()
serializer = ArticleSerializer(a)
serializer.data
content = JSONRenderer().render(serializer.data)
