from rest_framework import serializers

from artists.models import Artist, Category, Portfolio
from news.models import Article
from library.serializers import SocialMediaField

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
    thumbnail = serializers.SerializerMethodField()
    media = serializers.SerializerMethodField()
    
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'upload_type', 'thumbnail', 'media']

    def get_thumbnail(self, obj: Portfolio):
        if obj.upload:
            if obj.upload_type in ['drawing', 'photo']:
                return obj.get_image_thumbnail('upload', '400x400')
        if obj.link:
            if obj.upload_type in ['drawing', 'photo']:
                return obj.get_image_thumbnail('link', '400x400')

    def get_media(self, obj: Portfolio):
        if obj.upload.name:
            return obj.upload.url
        if obj.link:
            return obj.link

class ArtistListSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    photo_thumbnail = serializers.SerializerMethodField()

    def get_photo_thumbnail(self, obj: Artist):
        return obj.get_image_thumbnail('photo', '400x400')
    
    class Meta:
        model = Artist
        fields = ['name', 'slug', 'title', 'photo_thumbnail', 'categories']

class ArtistSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    related = ArtistListSerializer(many=True)
    portfolio = PortfolioSerializer(many=True, read_only=True)
    photo_thumbnail = serializers.SerializerMethodField()
    
    website = SocialMediaField('http://')
    instagram = SocialMediaField('https://www.instagram.com/', replaces=[['[@]', '']])
    facebook = SocialMediaField('https://www.facebook.com/')
    whatsapp = SocialMediaField('https://wa.me/', prefix='55', replaces=[['[\s\-\(\)]', '']])
    youtube = SocialMediaField('https://www.youtube.com/', prefix='@')

    def get_photo_thumbnail(self, obj: Artist):
        return obj.get_image_thumbnail('photo', '600x600')

    class Meta:
        model = Artist
        fields = ['name', 'slug', 'title', 'photo', 'photo_thumbnail',
                  'categories', 'related', 'biography', 'birth_date',
                  'birth_city', 'artistic_kinship', 'groups_affiliation', 'works',
                  'website', 'instagram', 'facebook', 'whatsapp', 'youtube', 'portfolio']

class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_thumbnail = serializers.SerializerMethodField()

    def get_image(self, obj: Article):
        return obj.get_image_thumbnail('image', '1440')
    def get_image_thumbnail(self, obj: Article):
        return obj.get_image_thumbnail('image', '480')

    class Meta:
        model = Article
        fields = ['title', 'slug', 'image', 'image_thumbnail', 'created_at']
