from rest_framework import serializers 
from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet 
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only= True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template':'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly') 
    owner  = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    
    class Meta:
        model =  User 
        fields = ['id', 'username', 'snippets']
    # def create(self, validated_data):
    #     '''Creates and return a new snippet given the instance'''
    #     return Snippet.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     """Update and return a given snippet instance given some valid data"""
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

    
