from rest_framework.serializers import ModelSerializer

from spotterapi.models.Session import Session
from spotterapi.models.Profile import Profile

class SessionSerializer(ModelSerializer):
    
    profile = Profile()
    
    class Meta:
        model = Session
        fields = ("id", "profile", "start_date", "plan")

        
        
class GetSessionSerializer:
    
    profile = Profile()
    
    class Meta:
        model = Session
        fields = ("id", "profile", "start_date", "plan", "exercises")
