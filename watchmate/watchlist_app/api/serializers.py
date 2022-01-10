from django.core.exceptions import ValidationError
from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"


class WatchlistSerializer(serializers.ModelSerializer):


    class Meta:
        model = Watchlist
        fields = "__all__" # ['id', 'movie_name', 'movie_about']
        # exclude = ['movie_released', 'id']





# def name_length(value):
#     if len(value) < 2:
#         raise ValidationError("Name is too short!")


# class WatchlistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     movie_name = serializers.CharField(validators=[name_length])
#     movie_about = serializers.CharField()
#     movie_released = serializers.BooleanField()

#     def create (self, validated_data):
#         return Watchlist.objects.create(**validated_data)
    
#     def update (self, instance, validated_data):
#         instance.movie_name = validated_data.get('movie_name', instance.movie_name)
#         instance.movie_about = validated_data.get('movie_about', instance.movie_about)
#         instance.movie_released = validated_data.get('movie_released', instance.movie_released)
#         instance.save()
#         return instance
        
#     def validate_movie_name(self, value):

#         if len(value) < 2:
#             raise ValidationError("Name is too short!")
#         else:
#             return value
    
#     def validate(self, data):
#         if data['movie_name'] == data['movie_about']:
#             raise ValidationError("Title and Description cannot be same!")
#         return data