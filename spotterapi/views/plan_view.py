from rest_framework.viewsets import ViewSet
from spotterapi.models.Profile import Profile
from spotterapi.models.Plan import Plan
from spotterapi.serializers.plan_serializers import PlanSerializer
from spotterapi.serializers.session_serializer import SessionSerializer
from rest_framework import status
from rest_framework.response import Response
from spotterapi.models.Session import Session


class PlanView (ViewSet):
    
    def retrieve(self, pk):
        
        # get the plan thats being requested
        plan = Plan.objects.get(pk = pk)
        
        sessions = Session.objects.filter(plan = plan.id)
        sessions_serializer = SessionSerializer(sessions, many = True)
        
        plan.plan_sessions = sessions_serializer.data
        serializer = PlanSerializer(plan)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def list(self, request):
        
        # gets the profile for the person logged in
        profile = Profile.objects.get(pk = request.auth.user.id)
        
         # gets all of the plans related to the profile thats logged in
        plans = Plan.objects.filter(profile = profile.id )
        
        
        
        for i in range (0, len(plans)):
            sessions = Session.objects.filter(plan = plans[i].id)
            plans[i].plan_sessions = sessions
                
        serializer = PlanSerializer(plans, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)