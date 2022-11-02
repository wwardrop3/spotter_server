from rest_framework.serializers import ModelSerializer
from spotterapi.models.Profile import Profile
from spotterapi.models.Plan import Plan


class PlanSerializer(ModelSerializer):
    
    profile = Profile()
    
    class Meta:
        model = Plan
        fields = ("id", "exercises", "profile", "start_date", "public", "plan_sessions")
        
        



