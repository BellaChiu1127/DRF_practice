from rest_framework import serializers
from web1.models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta :
        model = Music
        #fields = '__all__'
        fields = ('id','song','singer','last_modify_date','created')
        
       