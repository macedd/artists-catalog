from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from artists.models import Artist, Category, Portfolio
from news.models import Article

class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug']
class CategorySerializer(serializers.ModelSerializer):
    parent = ParentCategorySerializer()
    class Meta:
        model = Category
        fields = ['title', 'slug', 'parent']
        # fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'upload_type', 'upload', 'link']

class ArtistListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    photo_thumbnail = serializers.SerializerMethodField()

    def get_photo_thumbnail(self, obj):
        if obj.photo:
            return get_thumbnail(obj.photo, '400x400', crop='center', quality=90).url
    class Meta:
        model = Artist
        fields = ['name', 'slug', 'title', 'photo_thumbnail', 'categories']

class ArtistSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    related = ArtistListSerializer(many=True)
    portfolio = PortfolioSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['name', 'slug', 'title', 'photo',
                  'categories', 'related', 'biography', 'birth_date',
                  'birth_city', 'artistic_kinship', 'groups_affiliation', 'works',
                  'website', 'instagram', 'facebook', 'whatsapp', 'portfolio']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'image', 'created_at']
