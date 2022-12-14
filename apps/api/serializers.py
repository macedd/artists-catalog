from rest_framework import serializers

from artists.models import Artist, Category, Portfolio

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'parent']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'upload_type', 'upload', 'link']

class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'slug', 'title', 'photo',]

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

